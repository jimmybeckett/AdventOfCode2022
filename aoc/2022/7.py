import re
import utils


# Represents a directory if file_size is None, and a file otherwise
class Item:
    def __init__(self, name, parent_dir, file_size):
        self.name = name
        self.parent_dir = parent_dir
        self.contents = None if file_size else dict()
        self.file_size = file_size

    def size(self, cache) -> int:
        if self.file_size:
            return self.file_size
        return cache.setdefault(self.path(), sum(item.size(cache) for _, item in self.contents.items()))

    def path(self):
        return (self.parent_dir.path() if self.parent_dir else "") + self.name + ("/" if self.parent_dir else "")


def make_cache():
    with utils.get_input(2022, 7) as f:
        cd_re = re.compile(r"\$ cd (.+)")
        ls_re = re.compile(r"\$ ls")
        dir_re = re.compile(r"dir (.+)")
        file_re = re.compile(r"(\d+) (.+)")

        curr = root = Item("/", None, None)
        for line in f:
            if match := cd_re.match(line):
                match match.group(1):
                    case "..":
                        curr = curr.parent_dir
                    case "/":
                        curr = root
                    case val:
                        curr = curr.contents[val]
            elif ls_re.match(line):
                pass
            elif match := dir_re.match(line):
                if (dir_name := match.group(1)) not in curr.contents:
                    curr.contents[dir_name] = Item(dir_name, curr, None)
            elif match := file_re.match(line):
                size, name = int(match.group(1)), match.group(2)
                if name not in curr.contents:
                    curr.contents[name] = Item(name, curr, size)
            else:
                assert False
        root.size(cache := dict())
        return cache


def part_1(cache):
    return sum(size for size in cache.values() if size <= 100000)


def part_2(cache):
    capacity, update_size = 70000000, 30000000
    sizes = sorted(cache.values(), reverse=True)
    while sizes[0] - sizes[-1] + update_size > capacity:
        sizes.pop()
    return sizes[-1]


cache = make_cache()
print(part_1(cache))
print(part_2(cache))
