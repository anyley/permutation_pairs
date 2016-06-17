import sys
import itertools


class permutate_pairs:
    def __init__(self, array=[]):
        self.origin = array.copy()

    def __iter__(self):
        self.idx = -1
        self.array = self.origin.copy()
        self.cache = {}
        self.cache[tuple(self.array)] = 2
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == 0:
            return self.array
        key = tuple(self.array)
        while self.cache[key] < len(self.array) - 1:
            offset = self.cache[key]
            tmp = self.array.copy()
            tmp[0:2], tmp[offset:offset+2] = tmp[offset:offset+2], tmp[0:2]

            if tuple(tmp) in self.cache:
                self.cache[key] += 1
                continue
            else:
                self.array = tmp
                self.cache[tuple(tmp)] = 2
                return tmp
        raise StopIteration

    def max_permutations(self):
        posible = len(list(self))
        imposible = len(list(itertools.permutations(self.array))) - posible
        return posible, imposible

    def try_to_sort(self):
        for item in self:
            if item == [1, 2, 3, 4, 5, 6]:
                return self.idx
        return None


def main():
    # Обработка аргументов командной строки
    if len(sys.argv) > 1:
        # python3 p1.py 123456
        # >>> array = [1, 2, 3, 4, 5, 6]
        array = list(map(int, list(sys.argv[1])))
        it1 = permutate_pairs(array)
        sorted_index = it1.try_to_sort()
        if sorted_index is not None:
            print("Для сортировки потребовалось итераций:", sorted_index)
        else:
            print("Попарная сортировка невозможна")
    else:
        imposible = 0
        posible = 0
        for array in itertools.permutations([1,2,3,4,5,6]):
            it1 = permutate_pairs(list(array))
            result = it1.try_to_sort()
            if result != None:
                posible += 1
                print(array, "=>", (1, 2, 3, 4, 5, 6), "перестановок:", result)
            else:
                imposible += 1
        print("Сортируемых комбинаций", posible)
        print("Невозможно отсортировать", imposible, "комбинаций")


if __name__ == "__main__":
    main()
