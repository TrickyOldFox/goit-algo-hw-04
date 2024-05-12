import random
import timeit

from insertion_sort import insertion_sort
from merge_sort import merge_sort


def test_sorting(n: int) -> dict:
    def run_for_n(func, n: int) -> list:
        arr = random.sample(range(1, n + 1), n)
        return func(arr)

    results = {}
    results['Insertion Sort'] = timeit.timeit(
        lambda: run_for_n(insertion_sort, n),
        number=10_000
    )
    results['Merge Sort'] = timeit.timeit(
        lambda: run_for_n(merge_sort, n),
        number=10_000
    )
    results['Sorted'] = timeit.timeit(
        lambda: run_for_n(sorted, n),
        number=10_000
    )

    return results


def main():
    if __name__ == "__main__":
        for i in range(12):
            results = test_sorting(2**i)
            print(
                f'Results for n - {2**i}\n'
                f'{", ".join(f"{k}: {v}" for k, v in results.items())}'
            )


if __name__ == '__main__':
    main()
