import math
import timeit

from judge_prime_number import judge_prime_number as c_judge_prime_number


def judge_prime_number(number):
    end = int(math.sqrt(number)) + 1
    for n in range(2, end):
        if number % n == 0:
            return False
    return True


if __name__ == '__main__':
    number = 999999996015611
    loop = 5
    result1 = timeit.timeit('judge_prime_number(number)', globals=globals(), number=loop)
    result2 = timeit.timeit('c_judge_prime_number(number)', globals=globals(), number=loop)
    print('result1:', result1 / loop)
    print('result2:', result2 / loop)
