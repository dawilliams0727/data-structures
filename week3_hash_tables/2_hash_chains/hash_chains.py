# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor_:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        result = 'yes' if was_found else 'no'
        print(result)
        return result

    def write_chain(self, chain):
        result = ' '.join(chain)
        print(result)
        return result

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            return self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                return self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else: # query was "del"
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        result = 'yes' if was_found else 'no'
        print(result)
        return result

    def write_chain(self, chain):
        result = ' '.join(chain)
        print(result)
        return result

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            return self.write_chain(cur for cur in self.elems[query.ind])
        else:

            ind = self._hash_func(query.s)
            if query.type == 'find':
                chain: list[str] = self.elems[ind]
                result: bool = False
                for s in chain:
                    if s == query.s:
                        result = True
                return self.write_search_result(result)
            elif query.type == 'add':
                if query.s not in self.elems[ind]:
                    temp: list[str] = list(reversed(self.elems[ind]))
                    temp.append(query.s)
                    self.elems[ind] = list(reversed(temp))

            else: # query was "del"
                try:
                    self.elems[ind].remove(query.s)
                except ValueError:
                    pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
