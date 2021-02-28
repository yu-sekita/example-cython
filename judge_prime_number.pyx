import cython


cdef extern from "c_judge_prime_number.h":
    bint c_judge_prime_number(long number)


def judge_prime_number(number):
    return c_judge_prime_number(number)