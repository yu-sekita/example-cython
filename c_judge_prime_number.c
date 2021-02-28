#include "c_judge_prime_number.h"


bool c_judge_prime_number(long number) {
    long end;
    end = (long)sqrt(number) + 1;
    for (long n = 2; n <= end; n++) {
        if (number % n) {
            return false;
        }
    }
    return true;
}