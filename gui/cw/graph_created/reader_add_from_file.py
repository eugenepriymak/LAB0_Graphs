from user_exception.user_exception import UserError


class KeywordObject:
    def __init__(self, reader, kw, react):
        self.reader = reader
        self.kw = kw
        self.react = react


class KeywordNodesObject(KeywordObject):
    def __init__(self, reader):
        super().__init__(reader=reader, kw="NODES", react=self.react)

    def react(self):
        nodes = self.delete_nodes_from_buffer()
        self.reader.result.nodes += nodes

    def delete_nodes_from_buffer(self):
        nodes = []
        while not self.reader.is_kw_next() and not self.reader.is_eof_next():
            n_spaces = self.skip(spaces=True, start_ind=0)
            n_non_spaces = self.skip(spaces=False, start_ind=n_spaces)
            node = self.reader.buffer.get()[n_spaces:n_spaces + n_non_spaces]
            nodes.append(node)
            self.reader.buffer.delete(n_spaces + n_non_spaces)
        return nodes

    def skip(self, spaces, start_ind):
        reader = self.reader
        if not reader.is_there_something_to_read():
            return None
        while start_ind >= len(reader.buffer.get()):
            if reader.buffer.expand() == 0:
                return None
        n_skipped, buff_ind = 0, start_ind
        while reader.buffer.get()[buff_ind].isspace() if spaces else not reader.buffer.get()[buff_ind].isspace():
            n_skipped += 1
            buff_ind += 1
            if buff_ind >= len(reader.buffer.get()):
                if reader.buffer.expand() == 0:
                    break
        return n_skipped


class KeywordEdgesObject(KeywordObject):
    def __init__(self, reader):
        super().__init__(reader=reader, kw="EDGES", react=self.react)

    def react(self):
        edges = self.delete_edges_from_buffer()
        self.reader.result.edges += edges

    def delete_edges_from_buffer(self):
        edges = []
        while True:
            if self.reader.is_kw_next() or self.reader.is_eof_next():
                break
            n_spaces = self.skip(spaces=True, start_ind=0)
            n_non_spaces = self.skip(spaces=False, start_ind=n_spaces)
            node_1st = self.reader.buffer.get()[n_spaces:n_spaces + n_non_spaces]
            self.reader.buffer.delete(n_spaces + n_non_spaces)

            if self.reader.is_kw_next() or self.reader.is_eof_next():
                # TODO: it's necessary to warn that the last edge is not created
                return edges
            n_spaces = self.skip(spaces=True, start_ind=0)
            n_non_spaces = self.skip(spaces=False, start_ind=n_spaces)
            node_2nd = self.reader.buffer.get()[n_spaces:n_spaces + n_non_spaces]
            self.reader.buffer.delete(n_spaces + n_non_spaces)

            edges.append((node_1st, node_2nd))
        return edges

    def skip(self, spaces, start_ind):
        reader = self.reader
        if not reader.is_there_something_to_read():
            return None
        while start_ind >= len(reader.buffer.get()):
            if reader.buffer.expand() == 0:
                return None
        n_skipped, buff_ind = 0, start_ind
        while reader.buffer.get()[buff_ind].isspace() if spaces else not reader.buffer.get()[buff_ind].isspace():
            n_skipped += 1
            buff_ind += 1
            if buff_ind >= len(reader.buffer.get()):
                if reader.buffer.expand() == 0:
                    break
        return n_skipped


class Buffer:
    def __init__(self, file, buff_size):
        self.content = None
        self.buff_size = buff_size
        self.file = file

    def is_empty(self):
        return True if self.content is None else False

    def make_empty(self):
        self.content = None

    def get(self):
        return self.content if not self.is_empty() else None

    def rewrite(self):
        new_data = self.file.read(self.buff_size)
        if new_data == "":
            self.make_empty()
            return 0
        else:
            self.content = new_data
            return len(new_data)

    def expand(self):
        if self.is_empty():
            return self.rewrite()
        else:
            new_data = self.file.read(self.buff_size)
            self.content += new_data
            return len(new_data)

    def delete(self, n_syms):
        if not self.is_empty():
            left_content = self.content[n_syms:]
            if left_content == "":
                self.make_empty()
            else:
                self.content = left_content


class Result:
    def __init__(self):
        self.nodes = []
        self.edges = []


class Reader:
    def __init__(self, file, buff_size):
        self.result = Result()
        self.buffer = Buffer(file, buff_size)
        self.kw_objs = [KeywordNodesObject(reader=self), KeywordEdgesObject(reader=self)]

    def read_file(self):
        self.react_to_kws()
        return self.result.nodes, self.result.edges

    def react_to_kws(self):
        while not self.is_eof_next():
            if self.is_kw_next():
                kw = self.delete_kw_from_buffer()
                self.get_kw_obj(kw).react()
            else:
                raise UserError("You've used non-space characters outside a keyword's domain")

    def get_kws(self):
        kws = []
        for kw_obj in self.kw_objs:
            kws.append(kw_obj.kw)
        return kws

    def get_kw_obj(self, kw):
        for kw_obj in self.kw_objs:
            if kw == kw_obj.kw:
                return kw_obj
        return None

    def is_there_something_to_read(self):
        if not self.buffer.is_empty():
            return True
        else:
            return False if self.buffer.rewrite() == 0 else True

    def is_kw_next(self):
        if not self.is_there_something_to_read():
            return False
        n_spaces = self.skip(spaces=True, start_ind=0)
        n_non_spaces = self.skip(spaces=False, start_ind=n_spaces)
        kw = self.buffer.get()[n_spaces:n_spaces + n_non_spaces]
        return True if kw in self.get_kws() else False

    def is_eof_next(self):
        if not self.is_there_something_to_read():
            return True
        n_skipped = self.skip(spaces=True, start_ind=0)
        return False if n_skipped < len(self.buffer.get()) else True

    def delete_kw_from_buffer(self):
        if not self.is_kw_next() or self.is_eof_next():
            return None
        n_spaces_before = self.skip(spaces=True, start_ind=0)
        n_non_spaces = self.skip(spaces=False, start_ind=n_spaces_before)
        n_spaces_after = self.skip(spaces=True, start_ind=n_spaces_before + n_non_spaces)
        kw = self.buffer.get()[n_spaces_before:n_spaces_before + n_non_spaces]
        self.buffer.delete(n_spaces_before + n_non_spaces + n_spaces_after)
        return kw

    def skip(self, spaces, start_ind):
        if not self.is_there_something_to_read():
            return None
        while start_ind >= len(self.buffer.get()):
            if self.buffer.expand() == 0:
                return None
        n_skipped, buff_ind = 0, start_ind
        while self.buffer.get()[buff_ind].isspace() if spaces else not self.buffer.get()[buff_ind].isspace():
            n_skipped += 1
            buff_ind += 1
            if buff_ind >= len(self.buffer.get()):
                if self.buffer.expand() == 0:
                    break
        return n_skipped
