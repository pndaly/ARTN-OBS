#!/usr/bin/env python3


# +
# import(s)
# -
from src import *


# +
# initialize
# -
INVALID_INPUTS = [
    # NoneType
    None,
    # str
    get_hash(),
    # dict
    {get_hash(): OBS_LOG_MAX_BYTES},
    # list
    [OBS_LOG_MAX_BYTES],
    # tuple
    (OBS_LOG_MAX_BYTES,),
    # float
    math.nan,
    # int
    -OBS_LOG_MAX_BYTES
]


# +
# function: get_random_times()
# -
def get_random_times():
    """ return tuple of date/time values """
    _year = random.randint(1800, 2500)
    _month = random.randint(1, 12)
    _day = random.randint(1, 31)
    if _month == 2:
        _day = random.randint(1, 29)
    elif _month in (4, 6, 9, 11):
        _day = random.randint(1, 30)
    _degree = random.randint(0, 89)
    _hour = random.randint(0, 23)
    _minute = random.randint(0, 59)
    _second = random.randint(0, 59)
    _usec = random.randint(0, 999999)
    return _year, _month, _day, _degree, _hour, _minute, _second, _usec


# +
# OBS_DEC_PATTERN(s)
# -
def test_dec_0():
    """" dd:mm:ss(.ssssss)? """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(re.match(OBS_DEC_PATTERN, _k) is not None for _k in [
        # no sign
        f'{_degree:02d}:{_minute:02d}:{_second:02d}',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:01d}',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:02d}',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:03d}',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:04d}',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:05d}',
        f'{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:06d}',
        # + sign
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:01d}',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:02d}',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:03d}',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:04d}',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:05d}',
        f'+{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:06d}',
        # - sign
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:01d}',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:02d}',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:03d}',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:04d}',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:05d}',
        f'-{_degree:02d}:{_minute:02d}:{_second:02d}.{_usec:06d}'
    ])


def test_dec_1():
    """" dec range (no sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'{_d:02d}:{_minute:02d}:{_second:02d}.{_usec}') is not None for _d in range(0, 89))


def test_dec_2():
    """" dec range (+ sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'+{_d:02d}:{_minute:02d}:{_second:02d}.{_usec}') is not None for _d in range(0, 89))


def test_dec_3():
    """" dec range (- sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'-{_d:02d}:{_minute:02d}:{_second:02d}.{_usec}') is not None for _d in range(0, 89))


def test_dec_10():
    """ invalid input(s) """
    assert all(re.match(OBS_DEC_PATTERN, str(_k)) is None for _k in INVALID_INPUTS)


def test_dec_11():
    """ degree out of range (no sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'{_d:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None for _d in range(90, 99))


def test_dec_12():
    """ degree out of range (+ sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'+{_d:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None for _d in range(90, 99))


def test_dec_13():
    """ degree out of range (- sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'-{_d:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None for _d in range(90, 99))


def test_dec_14():
    """ minute out of range (no sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'{_degree:02d}:{_m:02d}:{_second:02d}.{_usec}') is None for _m in range(60, 99))


def test_dec_15():
    """ minute out of range (+ sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'+{_degree:02d}:{_m:02d}:{_second:02d}.{_usec}') is None for _m in range(60, 99))


def test_dec_16():
    """ minute out of range (- sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'-{_degree:02d}:{_m:02d}:{_second:02d}.{_usec}') is None for _m in range(60, 99))


def test_dec_17():
    """ second out of range (no sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'{_degree:02d}:{_minute:02d}:{_s:02d}.{_usec}') is None for _s in range(60, 99))


def test_dec_18():
    """ second out of range (+ sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'+{_degree:02d}:{_minute:02d}:{_s:02d}.{_usec}') is None for _s in range(60, 99))


def test_dec_19():
    """ second out of range (- sign) """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_DEC_PATTERN, f'-{_degree:02d}:{_minute:02d}:{_s:02d}.{_usec}') is None for _s in range(60, 99))


# +
# OBS_ISO_PATTERN(s)
# -
def test_iso_20():
    """" YYYY-MM-DDThh:mm:ss.ssssss """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:01d}',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:02d}',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:03d}',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:04d}',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:05d}',
        f'{_year:04d}-{_month:02d}-{_day:02d}T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:06d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:01d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:02d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:03d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:04d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:05d}',
        f'{_year:04d}-{_month:02d}-{_day:02d} {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:06d}'
    ])


def test_iso_30():
    """ invalid input(s) """
    assert all(re.match(OBS_ISO_PATTERN, str(_k)) is None for _k in INVALID_INPUTS)


def test_iso_31():
    """" month(s) without 31 days """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(re.match(OBS_ISO_PATTERN, _k) is None for _k in [
        f'{_year:04d}-02-30T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-02-31T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-04-31T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-06-31T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-09-31T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-11-31T{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-02-30 {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-02-31 {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-04-31 {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-06-31 {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-09-31 {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}',
        f'{_year:04d}-11-31 {_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}'
    ])


def test_iso_32():
    """ month out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    _t = random.choice([' ', 'T'])
    assert all(
        re.match(
            OBS_ISO_PATTERN,
            f'{_year:04d}-{_mm:02d}-{_day:02d}{_t}{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None
        for _mm in range(13, 99))


def test_iso_33():
    """ day out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    _t = random.choice([' ', 'T'])
    assert all(
        re.match(
            OBS_ISO_PATTERN,
            f'{_year:04d}-{_month:02d}-{_dd:02d}{_t}{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None
        for _dd in range(32, 99))


def test_iso_34():
    """ hour out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    _t = random.choice([' ', 'T'])
    assert all(
        re.match(
            OBS_ISO_PATTERN,
            f'{_year:04d}-{_month:02d}-{_day:02d}{_t}{_h:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None
        for _h in range(24, 99))


def test_iso_35():
    """ minute out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    _t = random.choice([' ', 'T'])
    assert all(
        re.match(
            OBS_ISO_PATTERN,
            f'{_year:04d}-{_month:02d}-{_day:02d}{_t}{_hour:02d}:{_m:02d}:{_second:02d}.{_usec}') is None
        for _m in range(60, 99))


def test_iso_36():
    """ second out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    _t = random.choice([' ', 'T'])
    assert all(
        re.match(
            OBS_ISO_PATTERN,
            f'{_year:04d}-{_month:02d}-{_day:02d}{_t}{_hour:02d}:{_minute:02d}:{_s:02d}.{_usec}') is None
        for _s in range(60, 99))


# +
# OBS_RA_PATTERN(s)
# -
def test_ra_40():
    """" hh:mm:ss(.ssssss)? """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(re.match(OBS_RA_PATTERN, _k) is not None for _k in [
        f'{_hour:02d}:{_minute:02d}:{_second:02d}',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:01d}',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:02d}',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:03d}',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:04d}',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:05d}',
        f'{_hour:02d}:{_minute:02d}:{_second:02d}.{_usec:06d}'
    ])


def test_ra_41():
    """" ra range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_RA_PATTERN, f'{_h:02d}:{_minute:02d}:{_second:02d}.{_usec}') is not None
        for _h in range(0, 23))


def test_ra_50():
    """ invalid input(s) """
    assert all(re.match(OBS_RA_PATTERN, str(_k)) is None for _k in INVALID_INPUTS)


def test_ra_51():
    """ hour out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_RA_PATTERN, f'{_h:02d}:{_minute:02d}:{_second:02d}.{_usec}') is None
        for _h in range(24, 99))


def test_ra_52():
    """ minute out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_RA_PATTERN, f'{_hour:02d}:{_m:02d}:{_second:02d}.{_usec}') is None for _m in range(60, 99))


def test_ra_53():
    """ second out of range """
    _year, _month, _day, _degree, _hour, _minute, _second, _usec = get_random_times()
    assert all(
        re.match(OBS_RA_PATTERN, f'{_hour:02d}:{_minute:02d}:{_s:02d}.{_usec}') is None for _s in range(60, 99))
