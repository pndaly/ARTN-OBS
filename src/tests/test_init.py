#!/usr/bin/env python3


# +
# import(s)
# -
from . import *
from pytest import raises as ptr
from src import *

import glob


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_init.py
"""


# +
# Logger()
# -
def test_logger_0():
    assert isinstance(Logger(get_hash()[:8]).logger, logging.Logger)


def test_logger_1():
    _s = get_hash()[:8]
    _l = Logger(_s).logger
    assert os.path.exists(os.path.abspath(os.path.expanduser(f"{os.getenv('OBS_LOGS', os.getcwd())}/{_s}.log")))


# +
# get_isot()
# -
def test_get_isot_0():
    assert all(get_isot(_k) is None for _k in TEST_INVALID_INPUTS)


def test_get_isot_1():
    assert re.match(OBS_ISO_PATTERN, get_isot(0, None)) is not None


def test_get_isot_2():
    assert re.match(OBS_ISO_PATTERN, get_isot()) is not None


def test_get_isot_3():
    assert re.match(OBS_ISO_PATTERN, get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False)) is not None


def test_get_isot_4():
    assert re.match(OBS_ISO_PATTERN, get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True)) is not None


def test_get_isot_5():
    _iso_jd = isot_to_jd(get_isot(0, False))
    _utc_jd = isot_to_jd(get_isot(0, True))
    assert math.isclose(abs(_utc_jd - _iso_jd), abs(OBS_UTC_OFFSET/24.0), rel_tol=TEST_TOLERANCE['3dp'])


# +
# get_jd()
# -
def test_get_jd_0():
    assert all(get_jd(_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_get_jd_1():
    assert get_jd(TEST_BYTES) is math.nan


def test_get_jd_2():
    _jd = get_jd()
    assert isinstance(_jd, float) and _jd is not math.nan


def test_get_jd_3():
    _jd = get_jd(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND))
    assert isinstance(_jd, float) and _jd > 0.0


# +
# isot_to_ephem()
# -
def test_isot_to_ephem_0():
    assert all(isot_to_ephem(_k) is None for _k in TEST_INVALID_INPUTS)


def test_isot_to_ephem_1():
    # noinspection PyUnresolvedReferences
    assert isinstance(isot_to_ephem(get_isot(0, True)), ephem.Date)


def test_isot_to_ephem_2():
    # noinspection PyUnresolvedReferences
    assert isinstance(isot_to_ephem(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND))), ephem.Date)


# +
# ephem_to_isot()
# -
def test_ephem_to_isot_0():
    assert all(ephem_to_isot(_k) is None for _k in TEST_INVALID_INPUTS)


def test_ephem_to_isot_1():
    _date = isot_to_ephem(get_isot(0, True))
    assert re.match(OBS_ISO_PATTERN, ephem_to_isot(_date)) is not None


def test_ephem_to_isot_2():
    _date = isot_to_ephem(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)))
    assert re.match(OBS_ISO_PATTERN, ephem_to_isot(_date)) is not None


# +
# isot_to_jd()
# -
def test_isot_to_jd_0():
    assert all(isot_to_jd(_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_isot_to_jd_1():
    assert isot_to_jd(get_isot(TEST_BYTES)) is math.nan


def test_isot_to_jd_2():
    _jd = isot_to_jd(get_isot())
    assert isinstance(_jd, float) and _jd is not math.nan


def test_isot_to_jd_3():
    _jd = isot_to_jd(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)))
    assert isinstance(_jd, float) and _jd > 0.0


# +
# isot_to_mjd()
# -
def test_isot_to_mjd_0():
    assert all(isot_to_mjd(_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_isot_to_mjd_1():
    assert isot_to_mjd(get_isot(TEST_BYTES)) is math.nan


def test_isot_to_mjd_2():
    _mjd = isot_to_mjd(get_isot())
    assert isinstance(_mjd, float) and _mjd is not math.nan


def test_isot_to_mjd_3():
    _mjd = isot_to_mjd(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)))
    assert isinstance(_mjd, float) and _mjd > 0.0


# +
# jd_to_isot()
# -
def test_jd_to_isot_0():
    assert all(jd_to_isot(_k) is None for _k in TEST_INVALID_INPUTS)


def test_jd_to_isot_1():
    assert jd_to_isot(float(TEST_BYTES)) is None


def test_jd_to_isot_2():
    _jd = isot_to_jd(get_isot())
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd)) is not None


def test_jd_to_isot_3():
    _jd = isot_to_jd(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)))
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd)) is not None


# +
# jd_to_mjd()
# -
def test_jd_to_mjd_0():
    assert all(jd_to_mjd(_k) is math.nan for _k in TEST_INVALID_INPUTS[:-2])


def test_jd_to_mjd_1():
    assert jd_to_mjd(0.0) == -OBS_MJD_OFFSET


def test_jd_to_mjd_2():
    _jd_iso = isot_to_jd(get_isot(0, False))
    _jd_utc = isot_to_jd(get_isot(0, True))
    assert math.isclose(abs(jd_to_mjd(_jd_utc) - jd_to_mjd(_jd_iso)), abs(OBS_UTC_OFFSET/24.0),
                        rel_tol=TEST_TOLERANCE['3dp'])


# +
# mjd_to_isot()
# -
def test_mjd_to_isot_0():
    assert all(mjd_to_isot(_k) is None for _k in TEST_INVALID_INPUTS)


def test_mjd_to_isot_1():
    assert mjd_to_isot(math.nan) is None


def test_mjd_to_isot_2():
    _mjd = isot_to_mjd(get_isot())
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd)) is not None


def test_mjd_to_isot_3():
    _mjd = isot_to_mjd(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)))
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd)) is not None


# +
# mjd_to_jd()
# -
def test_mjd_to_jd_0():
    assert all(mjd_to_jd(_k) is math.nan for _k in TEST_INVALID_INPUTS[:-2])


def test_mjd_to_jd_1():
    assert mjd_to_jd(0.0) == OBS_MJD_OFFSET


def test_mjd_to_mjd_2():
    _mjd_iso = isot_to_mjd(get_isot(0, False))
    _mjd_utc = isot_to_mjd(get_isot(0, True))
    assert math.isclose(abs(mjd_to_jd(_mjd_utc) - mjd_to_jd(_mjd_iso)), abs(OBS_UTC_OFFSET/24.0),
                        rel_tol=TEST_TOLERANCE['3dp'])


# +
# isot_to_nid()
# -
def test_isot_to_nid_0():
    assert all(isot_to_nid(_k) is None for _k in TEST_INVALID_INPUTS)


def test_isot_to_nid_1():
    assert isot_to_nid(get_isot(TEST_BYTES)) is None


def test_isot_to_nid_2():
    _nid = isot_to_nid(get_isot())
    assert isinstance(_nid, int)


def test_isot_to_nid_3():
    assert isot_to_nid(OBS_ZERO_NID) == 0


def test_isot_to_nid_4():
    _nid = isot_to_nid(get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)))
    assert isinstance(_nid, int)


def test_isot_to_nid_5():
    _nid = isot_to_nid(get_isot(random.randint(TEST_LOWER_BOUND, TEST_LOWER_BOUND)))
    assert abs(_nid) > 0


# +
# nid_to_isot()
# -
def test_nid_to_isot_0():
    assert all(nid_to_isot(_k) is None for _k in TEST_INVALID_INPUTS)


def test_nid_to_isot_1():
    assert nid_to_isot(get_isot(TEST_BYTES)) is None


def test_nid_to_isot_2():
    assert re.match(OBS_ISO_PATTERN, nid_to_isot(0)) is not None


def test_nid_to_isot_3():
    assert nid_to_isot(0) == OBS_ZERO_NID


def test_nid_to_isot_4():
    _nid = nid_to_isot(random.randint(1, TEST_UPPER_BOUND))
    assert isot_to_jd(_nid) - isot_to_jd(OBS_ZERO_NID) > 0.0


def test_nid_to_isot_5():
    _nid = nid_to_isot(random.randint(TEST_LOWER_BOUND, 0))
    assert isot_to_jd(_nid) - isot_to_jd(OBS_ZERO_NID) < 0.0


# +
# get_hash()
# -
def test_get_hash_0():
    assert all(isinstance(get_hash(_k), str) for _k in [None, TEST_INVALID_INPUTS[2:]]) in OBS_FALSE_VALUES


def test_get_hash_1():
    assert isinstance(get_hash(), str)


def test_get_hash_2():
    assert len(get_hash()) == 64


def test_get_hash_3():
    assert get_hash(get_isot()) != get_hash(get_isot())


# +
# get_semester()
# -
def test_get_semester_0():
    with ptr(Exception):
        get_semester(random.choice(TEST_INVALID_INPUTS))


def test_get_semester_1():
    _q = get_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_semester_2():
    _q = get_semester(get_isot())
    assert all(isinstance(_k, re.Match) for _k in
               [re.match(OBS_ISO_PATTERN, _q[2]), re.match(OBS_ISO_PATTERN, _q[3]), re.match(OBS_ISO_PATTERN, _q[4])])


def test_get_semester_3():
    _d = get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND))
    assert get_semester(_d)[3] == _d


# +
# get_last_semester()
# -
def test_get_last_semester_0():
    with ptr(Exception):
        get_last_semester(random.choice(TEST_INVALID_INPUTS))


def test_get_last_semester_1():
    _q = get_last_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_last_semester_2():
    _q = get_last_semester(get_isot())
    assert all(isinstance(_k, re.Match) for _k in
               [re.match(OBS_ISO_PATTERN, _q[2]), re.match(OBS_ISO_PATTERN, _q[3]), re.match(OBS_ISO_PATTERN, _q[4])])


def test_get_last_semester_3():
    _d = get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND))
    assert get_last_semester(_d)[3] == _d


def test_get_last_semester_4():
    _n = random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)
    _q1, _c1, _s1, _d1, _e1 = get_semester(get_isot(_n))
    _q2, _c2, _s2, _d2, _e2 = get_last_semester(get_isot(_n))
    assert (_q1 - _q2) in [-1, 1]


# +
# get_next_semester()
# -
def test_get_next_semester_0():
    with ptr(Exception):
        get_next_semester(random.choice(TEST_INVALID_INPUTS))


def test_get_next_semester_1():
    _q = get_next_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_next_semester_2():
    _q = get_next_semester(get_isot())
    assert all(isinstance(_k, re.Match) for _k in
               [re.match(OBS_ISO_PATTERN, _q[2]), re.match(OBS_ISO_PATTERN, _q[3]), re.match(OBS_ISO_PATTERN, _q[4])])


def test_get_next_semester_3():
    _d = get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND))
    assert get_next_semester(_d)[3] == _d


def test_get_next_semester_4():
    _n = random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND)
    _q1, _c1, _s1, _d1, _e1 = get_semester(get_isot(_n))
    _q2, _c2, _s2, _d2, _e2 = get_next_semester(get_isot(_n))
    assert (_q2 - _q1) in [-1, 1]


# +
# ra_to_decimal()
# -
def test_ra_to_decimal_0():
    assert all(ra_to_decimal(_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_ra_to_decimal_1():
    assert math.isclose(abs(ra_to_decimal()), 202.47083, rel_tol=TEST_TOLERANCE['3dp'])


def test_ra_to_decimal_2():
    _h = random.randint(1, 23)
    _m = random.randint(1, 59)
    _s = random.randint(1, 59)
    assert ra_to_decimal(f'{_h}:{_m}:{_s} hours') is not math.nan


# +
# ra_to_hms()
# -
def test_ra_to_hms_0():
    assert all(ra_to_hms(_k) is None for _k in TEST_INVALID_INPUTS[:-1])


def test_ra_to_hms_1():
    assert '13:29:5' in ra_to_hms(202.47083)


def test_ra_to_hms_2():
    _ra = random.uniform(-360.0, 360.0)
    assert ra_to_hms(_ra) is not None


# +
# ra_from_decimal()
# -
def test_ra_from_decimal_0():
    assert all(ra_from_decimal(_k) is None for _k in TEST_INVALID_INPUTS[:-1])


def test_ra_from_decimal_1():
    assert '13:29:5' in ra_to_hms(202.47083)


def test_ra_from_decimal_2():
    _ra = random.uniform(-360.0, 360.0)
    assert ra_from_decimal(_ra) is not None


# +
# dec_to_decimal()
# -
def test_dec_to_decimal_0():
    assert all(dec_to_decimal(_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_dec_to_decimal_1():
    assert math.isclose(abs(dec_to_decimal()), 47.19528, rel_tol=TEST_TOLERANCE['3dp'])


def test_dec_to_decimal_2():
    _d = random.randint(-90, 90)
    _m = random.randint(1, 59)
    _s = random.randint(1, 59)
    assert dec_to_decimal(f'{_d}:{_m}:{_s} degrees') is not math.nan


# +
# dec_from_decimal()
# -
def test_dec_from_decimal_0():
    assert all(dec_from_decimal(_k) is None for _k in TEST_INVALID_INPUTS)


def test_dec_from_decimal_1():
    assert math.isclose(dec_to_decimal(dec_from_decimal(47.19528)), 47.19528, rel_tol=TEST_TOLERANCE['3dp'])


def test_dec_from_decimal_2():
    _dec = random.uniform(-360.0, 360.0)
    assert dec_from_decimal(_dec) is not math.nan


# +
# dec_to_dms()
# -
def test_dec_to_dms_0():
    assert all(dec_to_dms(_k) is None for _k in TEST_INVALID_INPUTS[:-1])


def test_dec_to_dms_1():
    assert '+47:11:43.0' in dec_to_dms(47.19528)


def test_dec_to_hms_2():
    _dec = random.uniform(-360.0, 360.0)
    assert dec_to_dms(_dec) is not None


# +
# degree_to_radian()
# -
def test_degree_to_radian_0():
    assert all(degree_to_radian(_k) is math.nan for _k in TEST_INVALID_INPUTS[:-2])


def test_degree_to_radian_1():
    assert math.isclose(degree_to_radian(90.0), math.pi/2.0, rel_tol=TEST_TOLERANCE['4dp'])


def test_degree_to_radian_2():
    assert math.isclose(degree_to_radian(180.0), math.pi, rel_tol=TEST_TOLERANCE['4dp'])


def test_degree_to_radian_3():
    assert math.isclose(degree_to_radian(270.0), 3.0*math.pi/2.0, rel_tol=TEST_TOLERANCE['4dp'])


# +
# radian_to_degree()
# -
def test_radian_to_degree_0():
    assert all(radian_to_degree(_k) is math.nan for _k in TEST_INVALID_INPUTS[:-2])


def test_radian_to_degree_1():
    assert math.isclose(radian_to_degree(math.pi/2.0), 90.0, rel_tol=TEST_TOLERANCE['4dp'])


def test_radian_to_degree_2():
    assert math.isclose(radian_to_degree(math.pi), 180.0, rel_tol=TEST_TOLERANCE['4dp'])


def test_radian_to_degree_3():
    assert math.isclose(radian_to_degree(3.0*math.pi/2.0), 270.0, rel_tol=TEST_TOLERANCE['4dp'])


# +
# get_astropy_coords()
# -
def test_get_astropy_coords_0():
    assert all(get_astropy_coords(_k)[0] is math.nan for _k in TEST_INVALID_INPUTS)


def test_get_astropy_coords_1():
    assert all(get_astropy_coords(_k)[0] is math.nan for _k in TEST_INVALID_INPUTS)


def test_get_astropy_coords_2():
    assert math.isclose(abs(get_astropy_coords()[0]), 202.47083, rel_tol=TEST_TOLERANCE['3dp'])


def test_get_astropy_coords_3():
    assert math.isclose(abs(get_astropy_coords()[1]), 47.19528, rel_tol=TEST_TOLERANCE['3dp'])


# +
# decode_verboten()
# -
def test_decode_verboten_0():
    assert all(decode_verboten(_k) is _k for _k in TEST_INVALID_INPUTS)


def test_decode_verboten_1():
    assert isinstance(decode_verboten(get_hash()), str)


def test_decode_verboten_2():
    _str = get_hash()
    assert decode_verboten(encode_verboten(_str)) == _str


# +
# encode_verboten()
# -
def test_encode_verboten_0():
    assert all(encode_verboten(_k) is _k for _k in TEST_INVALID_INPUTS)


def test_encode_verboten_1():
    assert isinstance(encode_verboten(get_hash()), str)


def test_encode_verboten_2():
    _str = get_hash()
    assert encode_verboten(decode_verboten(_str)) == _str


# +
# read_png()
# -
def test_read_png_0():
    assert all(read_png(_k) is None for _k in TEST_INVALID_INPUTS)


def test_read_png_1():
    _res = read_png(glob.glob(f"{os.getenv('OBS_PNG')}/*.png")[0])
    assert isinstance(_res, str) and _res.strip() != ''


# +
# get_iers()
# -
def test_get_iers_0():
    with ptr(Exception):
        get_iers(random.choice(TEST_INVALID_INPUTS))


def test_get_iers_1():
    _res = get_iers().strip().lower()
    assert _res == 'astroplan' or _res == 'astropy'
