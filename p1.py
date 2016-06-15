import sys
import itertools


class permutate_pairs:
    def __init__(self, array=[]):
        self.origin = array.copy()

    def __iter__(self):
        self.idx = -1
        self.array = self.origin.copy()
        self.cache = {}
        self.cache[tuple(self.array)] = True
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == 0:
            return self.array

        for i in range(2, len(self.array) - 1):
            tmp = self.array.copy()
            tmp[0:2], tmp[i:i+2] = tmp[i:i+2], tmp[0:2]

            if tuple(tmp) in self.cache:
                continue
            else:
                self.array = tmp
                self.cache[tuple(tmp)] = True
                return tmp.copy()

        raise StopIteration

    def max_permutations(self):
        posible = len(list(self))
        imposible = len(list(itertools.permutations(self.array))) - posible
        return posible, imposible

    def try_to_sort(self):
        for item in self:
            print("#{index}: {array}".format(index=self.idx, array=item))
            if item == [1, 2, 3, 4, 5, 6]:
                return self.idx
        return None


def main():
    # Обработка аргументов командной строки
    if len(sys.argv) > 1:
        # python3 p1.py 123456
        # >>> array = [1, 2, 3, 4, 5, 6]
        array = list(map(int, list(sys.argv[1])))
    else:
        # default array
        array = [5, 6, 3, 4, 1, 2]

    it1 = permutate_pairs(array)
    posible, imposible = it1.max_permutations()
    sorted_index = it1.try_to_sort()
    print("Argument list: {arg}".format(arg=array))
    print("Posible: {0}\nImposible: {1}".format(posible, imposible))

    # Выводит порядковый номер комбинации при сортировке
    # Если sorted index is None, сортировка невозможна
    print("Permutation sorted index: ", sorted_index)


if __name__ == "__main__":
    main()
