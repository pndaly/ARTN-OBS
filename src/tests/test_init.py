#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src import *

import glob
import re


# +
# constant(s)
# -
INVALID_INPUTS = [None, get_hash(), {}, [], ()]


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_init.py
"""


# +
# test: Logger()
# -
def test_logger_1():
    """ test Logger() for correct input(s) """
    assert isinstance(Logger(get_hash()[:8]).logger, logging.Logger) in OBS_TRUE_VALUES


def test_logger_2():
    """ test Logger() for correct input(s) """
    _s = get_hash()[:8]
    _l = Logger(_s).logger
    assert os.path.exists(os.path.abspath(os.path.expanduser(f"{os.getenv('OBS_LOGS', os.getcwd())}/{_s}.log"))) in OBS_TRUE_VALUES


# +
# test: get_isot()
# -
def test_get_isot_1():
    """ tests get_isot() for incorrect input(s) """
    assert all(get_isot(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_get_isot_2():
    """ tests get_isot() for incorrect input(s) """
    assert re.match(OBS_ISO_PATTERN, get_isot(0, None)) is not None


def test_get_isot_3():
    """ tests get_isot() returns correctly formatted string """
    assert re.match(OBS_ISO_PATTERN, get_isot()) is not None


def test_get_isot_4():
    """ tests get_isot() returns correctly formatted string for random offset """
    assert re.match(OBS_ISO_PATTERN, get_isot(random.randint(-1000, 1000), False)) is not None


def test_get_isot_5():
    """ tests get_isot() returns correctly formatted string for random offset and utc """
    assert re.match(OBS_ISO_PATTERN, get_isot(random.randint(-1000, 1000), True)) is not None


def test_get_isot_6():
    """ test get_isot() for utc offset """
    _iso_jd = isot_to_jd(get_isot(0, False))
    _utc_jd = isot_to_jd(get_isot(0, True))
    assert math.isclose(abs(_utc_jd - _iso_jd), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.0001)


# +
# test: get_jd()
# -
def test_get_jd_1():
    """ tests get_jd() for incorrect input(s) """
    assert all(get_jd(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_get_jd_2():
    """ tests get_jd() for incorrect input(s) """
    assert get_jd(-1000000) is math.nan


def test_get_jd_3():
    """ tests get_jd() for correct input(s) """
    _jd = get_jd()
    assert isinstance(_jd, float) in OBS_TRUE_VALUES and _jd is not math.nan


def test_get_jd_4():
    """ tests get_jd() for correct random input(s) """
    _jd = get_jd(random.randint(-1000, 1000))
    assert isinstance(_jd, float) in OBS_TRUE_VALUES and _jd > 0.0


# +
# test: isot_to_ephem()
# -
def test_isot_to_ephem_1():
    """ tests isot_to_ephem() for incorrect input(s) """
    assert all(isot_to_ephem(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_isot_to_ephem_2():
    """ tests isot_to_ephem() for correct input(s) """
    assert isinstance(isot_to_ephem(get_isot(0, True)), ephem.Date) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_isot_to_ephem_3():
    """ tests isot_to_ephem() for correct random input(s) """
    assert isinstance(isot_to_ephem(get_isot(random.randint(-1000, 1000))), ephem.Date) in OBS_TRUE_VALUES


# +
# test: ephem_to_isot()
# -
def test_ephem_to_isot_1():
    """ tests ephem_to_isot() for incorrect input(s) """
    assert all(ephem_to_isot(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_ephem_to_isot_2():
    """ tests ephem_to_isot() for correct input(s) """
    _date = isot_to_ephem(get_isot(0, True))
    assert re.match(OBS_ISO_PATTERN, ephem_to_isot(_date)) is not None


def test_ephem_to_isot_3():
    """ tests ephem_to_isot() for correct random input(s) """
    _date = isot_to_ephem(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, ephem_to_isot(_date)) is not None


# +
# test: isot_to_jd()
# -
def test_isot_to_jd_1():
    """ tests isot_to_jd() for incorrect input(s) """
    assert all(isot_to_jd(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_isot_to_jd_2():
    """ tests isot_to_jd() for incorrect input(s) """
    assert isot_to_jd(get_isot(-1000000)) is math.nan


def test_isot_to_jd_3():
    """ tests isot_to_jd() for correct input(s) """
    _jd = isot_to_jd(get_isot())
    assert isinstance(_jd, float) in OBS_TRUE_VALUES and _jd is not math.nan


def test_isot_to_jd_4():
    """ tests isot_to_jd() for correct random input(s) """
    _jd = isot_to_jd(get_isot(random.randint(-1000, 1000)))
    assert isinstance(_jd, float) in OBS_TRUE_VALUES and _jd > 0.0


# +
# test: isot_to_mjd()
# -
def test_isot_to_mjd_1():
    """ tests isot_to_mjd() for incorrect input(s) """
    assert all(isot_to_mjd(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_isot_to_mjd_2():
    """ tests isot_to_mjd() for incorrect input(s) """
    assert isot_to_mjd(get_isot(-1000000)) is math.nan


def test_isot_to_mjd_3():
    """ tests isot_to_mjd() for correct input(s) """
    _mjd = isot_to_mjd(get_isot())
    assert isinstance(_mjd, float) in OBS_TRUE_VALUES and _mjd is not math.nan


def test_isot_to_mjd_4():
    """ tests isot_to_mjd() for correct random input(s) """
    _mjd = isot_to_mjd(get_isot(random.randint(-1000, 1000)))
    assert isinstance(_mjd, float) in OBS_TRUE_VALUES and _mjd > 0.0


# +
# test: jd_to_isot()
# -
def test_jd_to_isot_1():
    """ tests jd_to_isot() for incorrect input(s) """
    assert all(jd_to_isot(_k) is None for _k in [None, get_hash(), {}]) in OBS_TRUE_VALUES


def test_jd_to_isot_2():
    """ tests jd_to_isot() for incorrect input(s) """
    assert jd_to_isot(-1000000.0) is None


def test_jd_to_isot_3():
    """ tests jd_to_isot() for correct input(s) """
    _jd = isot_to_jd(get_isot())
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd)) is not None


def test_jd_to_isot_4():
    """ tests jd_to_isot() for correct random input(s) """
    _jd = isot_to_jd(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd)) is not None


# +
# test: jd_to_mjd()
# -
def test_jd_to_mjd_1():
    """ tests jd_to_mjd() for incorrect input(s) """
    assert all(jd_to_mjd(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_jd_to_mjd_2():
    """ tests jd_to_mjd() for correct input(s) """
    assert jd_to_mjd(0.0) == -OBS_MJD_OFFSET


def test_jd_to_mjd_3():
    """ tests jd_to_mjd for correct input(s) """
    _jd_iso = isot_to_jd(get_isot(0, False))
    _jd_utc = isot_to_jd(get_isot(0, True))
    assert math.isclose(abs(jd_to_mjd(_jd_utc) - jd_to_mjd(_jd_iso)), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.00001)


# +
# test: mjd_to_isot()
# -
def test_mjd_to_isot_1():
    """ tests mjd_to_isot() for incorrect input(s) """
    assert all(mjd_to_isot(_k) is None for _k in [None, get_hash(), {}]) in OBS_TRUE_VALUES


def test_mjd_to_isot_2():
    """ tests mjd_to_isot() for incorrect input(s) """
    assert mjd_to_isot(math.nan) is None


def test_mjd_to_isot_3():
    """ tests mjd_to_isot() for correct input(s) """
    _mjd = isot_to_mjd(get_isot())
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd)) is not None


def test_mjd_to_isot_4():
    """ tests mjd_to_isot() for correct random input(s) """
    _mjd = isot_to_mjd(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd)) is not None


# +
# test: mjd_to_jd()
# -
def test_mjd_to_jd_1():
    """ tests mjd_to_jd() for incorrect input(s) """
    assert all(mjd_to_jd(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_mjd_to_jd_2():
    """ tests mjd_to_jd() for correct input(s) """
    assert mjd_to_jd(0.0) == OBS_MJD_OFFSET


def test_mjd_to_mjd_3():
    """ tests mjd_to_mjd for correct input(s) """
    _mjd_iso = isot_to_mjd(get_isot(0, False))
    _mjd_utc = isot_to_mjd(get_isot(0, True))
    assert math.isclose(abs(mjd_to_jd(_mjd_utc) - mjd_to_jd(_mjd_iso)), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.00001)


# +
# test: isot_to_nid()
# -
def test_isot_to_nid_1():
    """ tests isot_to_nid() for incorrect input(s) """
    assert all(isot_to_nid(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_isot_to_nid_2():
    """ tests isot_to_mjd() for incorrect input(s) """
    assert isot_to_nid(get_isot(-1000000)) is None


def test_isot_to_nid_3():
    """ tests isot_to_nid() for correct input(s) """
    _nid = isot_to_nid(get_isot())
    assert isinstance(_nid, int) in OBS_TRUE_VALUES


def test_isot_to_nid_4():
    """ tests isot_to_nid() for correct input(s) """
    assert isot_to_nid(OBS_ZERO_NID) == 0


def test_isot_to_nid_5():
    """ tests isot_to_nid() for correct random input(s) """
    _nid = isot_to_nid(get_isot(random.randint(1, 1000)))
    assert isinstance(_nid, int) in OBS_TRUE_VALUES and _nid > 0


def test_isot_to_nid_6():
    """ tests isot_to_nid() for correct random input(s) """
    _nid = isot_to_nid(get_isot(random.randint(-10000, -1000)))
    assert isinstance(_nid, int) in OBS_TRUE_VALUES and _nid < 0


# +
# test: nid_to_isot()
# -
def test_nid_to_isot_1():
    """ tests nid_to_isot() for incorrect input(s) """
    assert all(nid_to_isot(_k) is None for _k in [None, get_hash(), {}]) in OBS_TRUE_VALUES


def test_nid_to_isot_2():
    """ tests nid_to_isot() for incorrect input(s) """
    assert nid_to_isot(get_isot(-1000000)) is None


def test_nid_to_isot_3():
    """ tests nid_to_isot() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, nid_to_isot(0)) is not None


def test_nid_to_isot_4():
    """ tests nid_to_isot() for correct input(s) """
    assert nid_to_isot(0) == OBS_ZERO_NID


def test_nid_to_isot_5():
    """ tests nid_to_isot() for correct random input(s) """
    _nid = nid_to_isot(random.randint(1, 1000))
    assert isot_to_jd(_nid) - isot_to_jd(OBS_ZERO_NID) > 0.0


def test_nid_to_isot_6():
    """ tests nid_to_isot() for correct random input(s) """
    _nid = nid_to_isot(random.randint(-10000, -1000))
    assert isot_to_jd(_nid) - isot_to_jd(OBS_ZERO_NID) < 0.0


# +
# test: get_hash()
# -
def test_get_hash_1():
    """ tests get_hash() for incorrect input(s) """
    assert all(isinstance(get_hash(_k), str) for _k in [None, {}, [], ()]) in OBS_FALSE_VALUES


def test_get_hash_2():
    """ tests get_hash() for correct input(s) """
    assert isinstance(get_hash(), str) in OBS_TRUE_VALUES


def test_get_hash_3():
    """ tests get_hash() for correct input(s) """
    assert len(get_hash()) == 64


def test_get_hash_4():
    """ tests get_hash() for correct input(s) """
    assert get_hash(get_isot()) != get_hash(get_isot())


# +
# test: get_semester()
# -
def test_get_semester_1():
    """ test get_semester() for incorrect input(s) """
    with ptr(Exception):
        get_semester(random.choice(INVALID_INPUTS))


def test_get_semester_2():
    """ test get_semester() for correct input(s) """
    _q = get_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_semester_3():
    """ test get_semester() for correct input(s) """
    _q = get_semester(get_isot())
    assert all(isinstance(_k, re.Match) for _k in
               [re.match(OBS_ISO_PATTERN, _q[2]),
                re.match(OBS_ISO_PATTERN, _q[3]),
                re.match(OBS_ISO_PATTERN, _q[4])]) in OBS_TRUE_VALUES


def test_get_semester_4():
    """ test get_semester() for correct random input(s) """
    _d = get_isot(random.randint(-1000, 1000))
    assert get_semester(_d)[3] == _d


# +
# test: get_last_semester()
# -
def test_get_last_semester_1():
    """ test get_last_semester() for incorrect input(s) """
    with ptr(Exception):
        get_last_semester(random.choice(INVALID_INPUTS))


def test_get_last_semester_2():
    """ test get_last_semester() for correct input(s) """
    _q = get_last_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_last_semester_3():
    """ test get_last_semester() for correct input(s) """
    _q = get_last_semester(get_isot())
    assert all(isinstance(_k, re.Match) for _k in
               [re.match(OBS_ISO_PATTERN, _q[2]),
                re.match(OBS_ISO_PATTERN, _q[3]),
                re.match(OBS_ISO_PATTERN, _q[4])]) in OBS_TRUE_VALUES


def test_get_last_semester_4():
    """ test get_last_semester() for correct random input(s) """
    _d = get_isot(random.randint(-1000, 1000))
    assert get_last_semester(_d)[3] == _d


def test_get_last_semester_5():
    """ test get_last_semester() for correct random input(s) """
    _n = random.randint(-1000, 1000)
    _q1, _c1, _s1, _d1, _e1 = get_semester(get_isot(_n))
    _q2, _c2, _s2, _d2, _e2 = get_last_semester(get_isot(_n))
    assert (_q1 - _q2) in [-1, 1]


# +
# test: get_next_semester()
# -
def test_get_next_semester_1():
    """ test get_next_semester() for incorrect input(s) """
    with ptr(Exception):
        get_next_semester(random.choice(INVALID_INPUTS))


def test_get_next_semester_2():
    """ test get_next_semester() for correct input(s) """
    _q = get_next_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_next_semester_3():
    """ test get_next_semester() for correct input(s) """
    _q = get_next_semester(get_isot())
    assert all(isinstance(_k, re.Match) for _k in
               [re.match(OBS_ISO_PATTERN, _q[2]),
                re.match(OBS_ISO_PATTERN, _q[3]),
                re.match(OBS_ISO_PATTERN, _q[4])]) in OBS_TRUE_VALUES


def test_get_next_semester_4():
    """ test get_next_semester() for correct random input(s) """
    _d = get_isot(random.randint(-1000, 1000))
    assert get_next_semester(_d)[3] == _d


def test_get_next_semester_5():
    """ test get_next_semester() for correct (random) input """
    _n = random.randint(-1000, 1000)
    _q1, _c1, _s1, _d1, _e1 = get_semester(get_isot(_n))
    _q2, _c2, _s2, _d2, _e2 = get_next_semester(get_isot(_n))
    assert (_q2 - _q1) in [-1, 1]


# +
# test: ra_to_decimal()
# -
def test_ra_to_decimal_1():
    """ test ra_to_decimal() for incorrect input(s) """
    assert all(ra_to_decimal(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_ra_to_decimal_2():
    """ test ra_to_decimal() for correct input(s) """
    assert math.isclose(abs(ra_to_decimal()), 202.47083, rel_tol=0.00001)


def test_ra_to_decimal_3():
    """ test ra_to_decimal() for correct random input(s) """
    _h = random.randint(1, 23)
    _m = random.randint(1, 59)
    _s = random.randint(1, 59)
    assert ra_to_decimal(f'{_h}:{_m}:{_s} hours') is not math.nan


# +
# test: ra_to_hms()
# -
def test_ra_to_hms_1():
    """ test ra_to_hms() for incorrect input(s) """
    assert all(ra_to_hms(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_ra_to_hms_2():
    """ test ra_to_hms() for correct input(s) """
    assert '13:29:5' in ra_to_hms(202.47083)


def test_ra_to_hms_3():
    """ test ra_to_hms() for correct random input(s) """
    _ra = random.uniform(0.0, 360.0)
    assert ra_to_hms(_ra) is not None


# +
# test: ra_from_decimal()
# -
def test_ra_from_decimal_1():
    """ tests ra_from_decimal() for incorrect input(s) """
    assert all(ra_from_decimal(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_ra_from_decimal_2():
    """ test ra_from_decimal() for correct input(s) """
    assert '13:29:5' in ra_to_hms(202.47083)


def test_ra_from_decimal_3():
    """ test ra_from_decimal() for correct random input(s) """
    _ra = random.uniform(0.0, 360.0)
    assert ra_from_decimal(_ra) is not None


# +
# test: dec_to_decimal()
# -
def test_dec_to_decimal_1():
    """ tests dec_to_decimal() for incorrect input(s) """
    assert all(dec_to_decimal(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_dec_to_decimal_2():
    """ tests dec_to_decimal() for correct input(s) """
    assert math.isclose(abs(dec_to_decimal()), 47.19528, rel_tol=0.00001)


def test_dec_to_decimal_3():
    """ test dec_to_decimal() for random input(s) """
    _d = random.randint(-90, 90)
    _m = random.randint(1, 59)
    _s = random.randint(1, 59)
    assert dec_to_decimal(f'{_d}:{_m}:{_s} degrees') is not math.nan


# +
# test: dec_from_decimal()
# -
def test_dec_from_decimal_1():
    """ tests dec_from_decimal() for incorrect input(s) """
    assert all(dec_from_decimal(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_dec_from_decimal_2():
    """ test dec_from_decimal() for correct input(s) """
    assert math.isclose(dec_to_decimal(dec_from_decimal(47.19528)), 47.19528, rel_tol=0.00001)


def test_dec_from_decimal_3():
    """ test dec_from_decimal() for correct random input(s) """
    _dec = random.uniform(0.0, 360.0)
    assert dec_from_decimal(_dec) is not math.nan


# +
# test: dec_to_dms()
# -
def test_dec_to_dms_1():
    """ tests dec_to_dms() for incorrect input(s) """
    assert all(dec_to_dms(_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_dec_to_dms_2():
    """ test dec_to_dms() for correct input(s) """
    assert '+47:11:43.0' in dec_to_dms(47.19528)


def test_dec_to_hms_3():
    """ test dec_to_dms() for correct random input(s) """
    _dec = random.uniform(0.0, 360.0)
    assert dec_to_dms(_dec) is not None


# +
# test: degree_to_radian()
# -
def test_degree_to_radian_1():
    """ test degree_to_radian() for incorrect input(s) """
    assert all(degree_to_radian(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_degree_to_radian_2():
    """ test degree_to_radian() for correct input(s) """
    assert math.isclose(degree_to_radian(90.0), math.pi/2.0, rel_tol=0.000001)


def test_degree_to_radian_3():
    """ test degree_to_radian() for correct input(s) """
    assert math.isclose(degree_to_radian(180.0), math.pi, rel_tol=0.000001)


def test_degree_to_radian_4():
    """ test degree_to_radian() for correct input(s) """
    assert math.isclose(degree_to_radian(270.0), 3.0*math.pi/2.0, rel_tol=0.000001)


# +
# test: radian_to_degree()
# -
def test_radian_to_degree_1():
    """ test radian_to_degree() for incorrect input(s) """
    assert all(radian_to_degree(_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_radian_to_degree_2():
    """ test radian_to_degree() for correct input(s) """
    assert math.isclose(radian_to_degree(math.pi/2.0), 90.0, rel_tol=0.000001)


def test_radian_to_degree_3():
    """ test radian_to_degree() for correct input(s) """
    assert math.isclose(radian_to_degree(math.pi), 180.0, rel_tol=0.000001)


def test_radian_to_degree_4():
    """ test radian_to_degree() for correct input(s) """
    assert math.isclose(radian_to_degree(3.0*math.pi/2.0), 270.0, rel_tol=0.000001)


# +
# test: get_astropy_coords()
# -
def test_get_astropy_coords_1():
    """ test get_astropy_coords() for incorrect input(s) """
    assert all(get_astropy_coords(_k)[0] is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_get_astropy_coords_2():
    """ test get_astropy_coords() for incorrect input(s) """
    assert all(get_astropy_coords(_k)[0] is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_get_astropy_coords_3():
    """ tests get_astropy_coords() for correct input(s) """
    assert math.isclose(abs(get_astropy_coords()[0]), 202.47083, rel_tol=0.00001)


def test_get_astropy_coords_4():
    """ tests get_astropy_coords() for correct input(s) """
    assert math.isclose(abs(get_astropy_coords()[1]), 47.19528, rel_tol=0.00001)


# +
# test: decode_verboten()
# -
def test_decode_verboten_1():
    """ tests decode_verboten for incorrect input(s) """
    assert all(decode_verboten(_k) is _k for _k in [None, {}, [], ()]) in OBS_TRUE_VALUES


def test_decode_verboten_2():
    """ tests decode_verboten() for correct input(s) """
    assert isinstance(decode_verboten(get_hash()), str) in OBS_TRUE_VALUES


def test_decode_verboten_3():
    """ tests decode_verboten() for correct input(s) """
    _str = get_hash()
    assert decode_verboten(encode_verboten(_str)) == _str


# +
# test: encode_verboten()
# -
def test_encode_verboten_1():
    """ tests encode_verboten for incorrect input(s) """
    assert all(encode_verboten(_k) is _k for _k in [None, {}, [], ()]) in OBS_TRUE_VALUES


def test_encode_verboten_2():
    """ tests encode_verboten() for correct input(s) """
    assert isinstance(encode_verboten(get_hash()), str) in OBS_TRUE_VALUES


def test_encode_verboten_3():
    """ tests encode_verboten() for correct input(s) """
    _str = get_hash()
    assert encode_verboten(decode_verboten(_str)) == _str


# +
# test: read_png()
# -
def test_read_png_1():
    """ test read_png() for incorrect input(s) """
    assert all(read_png(_k) is None for _k in [None, {}, [], ()]) in OBS_TRUE_VALUES


def test_read_png_2():
    """ test read_png() for correct input """
    _res = read_png(glob.glob(f"{os.getenv('OBS_PNG')}/*.png")[0])
    assert isinstance(_res, str) and _res.strip() != ''


# +
# test: get_iers()
# -
def test_get_iers_1():
    """ test get_iers() for incorrect input(s)"""
    with ptr(Exception):
        get_iers(random.choice(INVALID_INPUTS))


def test_get_iers_2():
    """ test get_iers() for correct input(s) """
    _res = get_iers().strip().lower()
    assert _res == 'astroplan' or _res == 'astropy'
