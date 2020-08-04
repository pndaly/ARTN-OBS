#!/usr/bin/env python3


# +
# import(s)
# -
from src.telescopes.factory import *


# +
# constant(s)
# -
TEST_BYTES = 9223372036854775807
TEST_INVALID_INPUTS = [None, get_hash(), {get_hash(): TEST_BYTES}, [TEST_BYTES], (TEST_BYTES,), math.nan, -TEST_BYTES]
TEST_LOWER_BOUND = random.randint(-1000, 0)
TEST_NDAYS = random.randint(1, 5)
TEST_NUM = random.randint(1, AST__5__MINUTES - 1)
TEST_TOLERANCE = {'1dp': 0.1, '2dp': 0.01, '3dp': 0.001, '4dp': 0.0001, '5dp': 0.00001, '6dp': 0.000001}
TEST_UPPER_BOUND = random.randint(0, 1000)
