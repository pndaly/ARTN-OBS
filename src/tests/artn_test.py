#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.models.Models import *
from src.telescopes.factory import *
from src.instruments.factory import *

import astroplan
import astropy
import glob
import sqlalchemy


# +
# doc string(s)
# -
__doc__ = """
  % python3 -m pytest obs_test.py
"""


# +
# test: Logger(name='', level='DEBUG')
# -
# noinspection PyUnresolvedReferences
def test_logger_1():
    """ test Logger() class returns correct class """
    assert isinstance(Logger('ARTN-OBS').logger, logging.Logger) is True


def test_logger_2():
    """ test Logger() class returns file """
    _l = Logger('ARTN-OBS').logger
    _f = os.path.abspath(os.path.expanduser(f"{os.getenv('OBS_LOGS', os.getcwd())}/ARTN-OBS.log"))
    assert os.path.exists(_f) is True


# +
# test: get_isot(ndays=0, utc=False)
# -
def test_get_isot_1():
    """ tests get_isot() returns correctly formatted string """
    assert re.match(OBS_ISO_PATTERN, get_isot()) is not None


def test_get_isot_2():
    """ tests get_isot() returns correctly formatted string for random offset """
    assert re.match(OBS_ISO_PATTERN, get_isot(random.randint(-1000, 1000), False)) is not None


def test_get_isot_3():
    """ tests get_isot() returns correctly formatted string for random offset and utc """
    assert re.match(OBS_ISO_PATTERN, get_isot(random.randint(-1000, 1000), True)) is not None


def test_get_isot_4():
    """ tests get_isot() returns None for incorrect format output """
    assert re.match(OBS_ISO_PATTERN, get_isot().replace('T', get_hash()[random.randint(1, 63)].lower())) is None


def test_get_isot_5():
    """ tests get_isot() for incorrect offset data type """
    assert get_isot(None) is None


def test_get_isot_6():
    """ tests get_isot() for incorrect utc type """
    assert re.match(OBS_ISO_PATTERN, get_isot(0, None)) is not None


def test_get_isot_7():
    """ test get_isot() for utc offset """
    _iso_jd = isot_to_jd(get_isot(0, False))
    _utc_jd = isot_to_jd(get_isot(0, True))
    assert math.isclose(abs(_utc_jd - _iso_jd), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.0001)


# +
# test: get_jd(ndays=0)
# -
def test_get_jd_1():
    """ tests get_jd() for correct input """
    _jd = get_jd()
    assert isinstance(_jd, float) is True and _jd is not math.nan


def test_get_jd_2():
    """ tests get_jd() returns correct value for random offset """
    _jd = get_jd(random.randint(-1000, 1000))
    assert isinstance(_jd, float) is True and _jd > 0.0


def test_get_jd_3():
    """ tests get_jd() for incorrect input """
    assert get_jd(None) is math.nan


def test_get_jd_4():
    """ tests get_jd() for correct non-Julian calendar """
    assert get_jd(-1000000) is math.nan


# +
# test: isot_to_ephem(isot=get_isot())
# -
# noinspection PyUnresolvedReferences
def test_isot_to_ephem_1():
    """ tests isot_to_ephem() for correct input """
    assert isinstance(isot_to_ephem(get_isot(0, True)), ephem.Date) is True


def test_isot_to_ephem_2():
    """ tests isot_to_ephem() for correct random input """
    assert isinstance(isot_to_ephem(get_isot(random.randint(-1000, 1000))), ephem.Date) is True


def test_isot_to_ephem_3():
    """ tests isot_to_ephem() for incorrect input """
    assert isot_to_ephem(None) is None


# +
# test: ephem_to_isot(date=None)
# -
def test_ephem_to_isot_1():
    """ tests ephem_to_isot() for correct input """
    _date = isot_to_ephem(get_isot(0, True))
    assert re.match(OBS_ISO_PATTERN, ephem_to_isot(_date)) is not None


def test_ephem_to_isot_2():
    """ tests ephem_to_isot() for correct random input """
    _date = isot_to_ephem(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, ephem_to_isot(_date)) is not None


def test_ephem_to_isot_3():
    """ tests ephem_to_isot() for incorrect input """
    assert ephem_to_isot(None) is None


# +
# test: isot_to_jd(isot=get_isot())
# -
def test_isot_to_jd_1():
    """ tests isot_to_jd() for correct input """
    _jd = isot_to_jd(get_isot())
    assert isinstance(_jd, float) is True and _jd is not math.nan


def test_isot_to_jd_2():
    """ tests isot_to_jd() returns correct value for random offset """
    _jd = isot_to_jd(get_isot(random.randint(-1000, 1000)))
    assert isinstance(_jd, float) is True and _jd > 0.0


def test_isot_to_jd_3():
    """ tests isot_to_jd() for incorrect input """
    assert isot_to_jd(None) is math.nan


def test_isot_to_jd_4():
    """ tests isot_to_jd() for correct non-Julian calendar """
    assert isot_to_jd(get_isot(-1000000)) is math.nan


# +
# test: isot_to_mjd(isot=get_isot())
# -
def test_isot_to_mjd_1():
    """ tests isot_to_mjd() for correct input """
    _mjd = isot_to_mjd(get_isot())
    assert isinstance(_mjd, float) is True and _mjd is not math.nan


def test_isot_to_mjd_2():
    """ tests isot_to_mjd() returns correct value for random offset """
    _mjd = isot_to_mjd(get_isot(random.randint(-1000, 1000)))
    assert isinstance(_mjd, float) is True and _mjd > 0.0


def test_isot_to_mjd_3():
    """ tests isot_to_mjd() for incorrect input """
    assert isot_to_mjd(None) is math.nan


def test_isot_to_mjd_4():
    """ tests isot_to_mjd() for correct non-Julian calendar """
    assert isot_to_mjd(get_isot(-1000000)) is math.nan


# +
# test: jd_to_isot(jd=math.nan)
# -
def test_jd_to_isot_1():
    """ tests jd_to_isot() for correct input """
    _jd = isot_to_jd(get_isot())
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd)) is not None


def test_jd_to_isot_2():
    """ tests jd_to_isot() returns correct value for random offset """
    _jd = isot_to_jd(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd)) is not None


def test_jd_to_isot_3():
    """ tests jd_to_isot() for incorrect input """
    _jd = isot_to_jd(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, jd_to_isot(_jd).replace('T', get_hash())) is None


def test_jd_to_isot_4():
    """ tests jd_to_isot() for correct non-Julian calendar """
    assert jd_to_isot(math.nan) is None


# +
# test: mjd_to_isot(mjd=math.nan)
# -
def test_mjd_to_isot_1():
    """ tests mjd_to_isot() for correct input """
    _mjd = isot_to_mjd(get_isot())
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd)) is not None


def test_mjd_to_isot_2():
    """ tests mjd_to_isot() returns correct value for random offset """
    _mjd = isot_to_mjd(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd)) is not None


def test_mjd_to_isot_3():
    """ tests mjd_to_isot() for incorrect input """
    _mjd = isot_to_mjd(get_isot(random.randint(-1000, 1000)))
    assert re.match(OBS_ISO_PATTERN, mjd_to_isot(_mjd).replace('T', get_hash())) is None


def test_mjd_to_isot_4():
    """ tests mjd_to_isot() for correct non-Julian calendar """
    assert mjd_to_isot(math.nan) is None


# +
# test: mjd_to_jd(mjd=math.nan)
# -
def test_mjd_to_jd_1():
    """ tests mjd_to_jd() for incorrect input """
    assert mjd_to_jd(None) is math.nan


def test_mjd_to_jd_2():
    """ tests mjd_to_jd() for correct input """
    assert mjd_to_jd(0.0) == OBS_MJD_OFFSET


def test_mjd_to_jd_3():
    """ tests mjd_to_jd for correct offset """
    _mjd_iso = isot_to_mjd(get_isot(0, False))
    _mjd_utc = isot_to_mjd(get_isot(0, True))
    assert math.isclose(abs(mjd_to_jd(_mjd_utc) - mjd_to_jd(_mjd_iso)), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.00001)


# +
# test: jd_to_mjd(jd=math.nan)
# -
def test_jd_to_mjd_1():
    """ tests jd_to_mjd() for incorrect input """
    assert jd_to_mjd(None) is math.nan


def test_jd_to_mjd_2():
    """ tests jd_to_mjd() for correct input """
    assert jd_to_mjd(0.0) == -OBS_MJD_OFFSET


def test_jd_to_mjd_3():
    """ tests jd_to_mjd for correct offset """
    _jd_iso = isot_to_jd(get_isot(0, False))
    _jd_utc = isot_to_jd(get_isot(0, True))
    assert math.isclose(abs(jd_to_mjd(_jd_utc) - jd_to_mjd(_jd_iso)), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.00001)


# +
# test: isot_to_nid(isot=get_isot())
# -
def test_isot_to_nid_1():
    """ tests isot_to_nid() for correct input """
    _nid = isot_to_nid(get_isot())
    assert isinstance(_nid, int) is True


def test_isot_to_nid_2():
    """ tests isot_to_nid() returns correct value for random offset """
    _nid = isot_to_nid(get_isot(random.randint(1, 1000)))
    assert isinstance(_nid, int) is True and _nid > 0


def test_isot_to_nid_3():
    """ tests isot_to_nid() returns correct value for random offset """
    _nid = isot_to_nid(get_isot(random.randint(-10000, -1000)))
    assert isinstance(_nid, int) is True and _nid < 0


def test_isot_to_nid_4():
    """ tests isot_to_nid() for incorrect input """
    assert isot_to_nid(None) is None


def test_isot_to_nid_5():
    """ tests isot_to_nid() for correct non-Julian calendar """
    assert isot_to_nid(get_isot(-1000000)) is None


def test_isot_to_nid_6():
    """ tests isot_to_nid() for correct input """
    assert isot_to_nid(OBS_ZERO_NID) == 0


# +
# test: nid_to_isot(nid=0)
# -
def test_nid_to_isot_1():
    """ tests isot_to_nid() for correct input """
    assert re.match(OBS_ISO_PATTERN, nid_to_isot(0)) is not None


def test_nid_to_isot_2():
    """ tests isot_to_nid() returns correct value for random offset """
    _nid = nid_to_isot(random.randint(1, 1000))
    assert isot_to_jd(_nid) - isot_to_jd(OBS_ZERO_NID) > 0.0


def test_nid_to_isot_3():
    """ tests nid_to_isot() returns correct value for random offset """
    _nid = nid_to_isot(random.randint(-10000, -1000))
    assert isot_to_jd(_nid) - isot_to_jd(OBS_ZERO_NID) < 0.0


def test_nid_to_isot_4():
    """ tests nid_to_isot() for incorrect input """
    assert nid_to_isot(None) is None


def test_nid_to_isot_5():
    """ tests nid_to_isot() for correct non-Julian calendar """
    assert nid_to_isot(get_isot(-1000000)) is None


def test_nid_to_isot_6():
    """ tests nid_to_isot() for correct input """
    assert nid_to_isot(0) == OBS_ZERO_NID


# +
# test: get_hash(seed=get_isot())
# -
def test_get_hash_1():
    """ tests get_hash() returns a string """
    assert isinstance(get_hash(), str) is True


def test_get_hash_2():
    """ tests get_hash() returns string of correct length """
    assert len(get_hash()) == 64


def test_get_hash_3():
    """ tests get_hash() returns string of correct (random) length """
    _len = random.randint(1, 64)
    assert len(get_hash()[:_len]) == _len


def test_get_hash_4():
    """ tests get_hash() does not return duplicate string """
    assert get_hash(get_isot()) != get_hash(get_isot())


def test_get_hash_5():
    """ tests get_hash() for incorrect input """
    assert get_hash(None) is None


# +
# test: get_semester(date=get_isot())
# -
def test_get_semester_1():
    """ test get_semester() for correct input """
    _q = get_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_semester_2():
    """ test get_semester() for correct input """
    _q = get_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[2]) is not None


def test_get_semester_3():
    """ test get_semester() for correct input """
    _q = get_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[3]) is not None


def test_get_semester_4():
    """ test get_semester() for correct input """
    _q = get_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[4]) is not None


def test_get_semester_5():
    """ test get_semester() for correct (random) input """
    _d = get_isot(random.randint(-1000, 1000))
    assert get_semester(_d)[3] == _d


def test_get_semester_6():
    """ test get_semester() for incorrect input """
    with ptr(Exception):
        get_semester(None)


# +
# test: get_last_semester(date=get_isot())
# -
def test_get_last_semester_1():
    """ test get_last_semester() for correct input """
    _q = get_last_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_last_semester_2():
    """ test get_last_semester() for correct input """
    _q = get_last_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[2]) is not None


def test_get_last_semester_3():
    """ test get_last_semester() for correct input """
    _q = get_last_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[3]) is not None


def test_get_last_semester_4():
    """ test get_last_semester() for correct input """
    _q = get_last_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[4]) is not None


def test_get_last_semester_5():
    """ test get_last_semester() for correct (random) input """
    _d = get_isot(random.randint(-1000, 1000))
    assert get_last_semester(_d)[3] == _d


def test_get_last_semester_6():
    """ test get_last_semester() for incorrect input """
    with ptr(Exception):
        get_last_semester(None)


def test_get_last_semester_7():
    """ test get_last_semester() for correct (random) input """
    _n = random.randint(-1000, 1000)
    _q1, _c1, _s1, _d1, _e1 = get_semester(get_isot(_n))
    _q2, _c2, _s2, _d2, _e2 = get_last_semester(get_isot(_n))
    assert (_q1 - _q2) in [-1, 1]


# +
# test: get_next_semester(date=get_isot())
# -
def test_get_next_semester_1():
    """ test get_next_semester() for correct input """
    _q = get_next_semester(get_isot())
    assert _q[0] in [1, 2]


def test_get_next_semester_2():
    """ test get_next_semester() for correct input """
    _q = get_next_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[2]) is not None


def test_get_next_semester_3():
    """ test get_next_semester() for correct input """
    _q = get_next_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[3]) is not None


def test_get_next_semester_4():
    """ test get_next_semester() for correct input """
    _q = get_next_semester(get_isot())
    assert re.match(OBS_ISO_PATTERN, _q[4]) is not None


def test_get_next_semester_5():
    """ test get_next_semester() for correct (random) input """
    _d = get_isot(random.randint(-1000, 1000))
    assert get_next_semester(_d)[3] == _d


def test_get_next_semester_6():
    """ test get_next_semester() for incorrect input """
    with ptr(Exception):
        get_next_semester(None)


def test_get_next_semester_7():
    """ test get_next_semester() for correct (random) input """
    _n = random.randint(-1000, 1000)
    _q1, _c1, _s1, _d1, _e1 = get_semester(get_isot(_n))
    _q2, _c2, _s2, _d2, _e2 = get_next_semester(get_isot(_n))
    assert (_q2 - _q1) in [-1, 1]


# +
# test: ra_to_decimal(ra='13:29:53 hours')
# -
def test_ra_to_decimal_1():
    """ tests ra_to_decimal() for incorrect input """
    assert ra_to_decimal(None) is math.nan


def test_ra_to_decimal_2():
    """ test ra_to_decimal() for correct input """
    assert math.isclose(abs(ra_to_decimal()), 202.47083, rel_tol=0.00001)


def test_ra_to_decimal_3():
    """ test ra_to_decimal() for random input """
    _h = random.randint(1, 23)
    _m = random.randint(1, 59)
    _s = random.randint(1, 59)
    assert ra_to_decimal(f'{_h}:{_m}:{_s} hours') is not math.nan


# +
# test: ra_to_hms(ra=math.nan)
# -
def test_ra_to_hms_1():
    """ tests ra_to_hms() for incorrect input """
    assert ra_to_hms(None) is None


def test_ra_to_hms_2():
    """ test ra_to_hms() for correct input """
    assert '13:29:5' in ra_to_hms(202.47083)


def test_ra_to_hms_3():
    """ test ra_to_hms() for random input """
    _ra = random.uniform(0.0, 360.0)
    assert ra_to_hms(_ra) is not None


# +
# test: ra_from_decimal(ra=math.nan)
# -
def test_ra_from_decimal_1():
    """ tests ra_from_decimal() for incorrect input """
    assert ra_from_decimal(None) is None


def test_ra_from_decimal_2():
    """ test ra_from_decimal() for correct input """
    assert '13:29:5' in ra_to_hms(202.47083)


def test_ra_from_decimal_3():
    """ test ra_from_decimal() for random input """
    _ra = random.uniform(0.0, 360.0)
    assert ra_from_decimal(_ra) is not None


# +
# test: dec_to_decimal(dec='47:11:43 degrees')
# -
def test_dec_to_decimal_1():
    """ tests dec_to_decimal() for incorrect input """
    assert dec_to_decimal(None) is math.nan


def test_dec_to_decimal_2():
    """ tests dec_to_decimal() for correct input """
    assert math.isclose(abs(dec_to_decimal()), 47.19528, rel_tol=0.00001)


def test_dec_to_decimal_3():
    """ test dec_to_decimal() for random input """
    _d = random.randint(-90, 90)
    _m = random.randint(1, 59)
    _s = random.randint(1, 59)
    assert dec_to_decimal(f'{_d}:{_m}:{_s} degrees') is not math.nan


# +
# test: dec_from_decimal(dec=math.nan)
# -
def test_dec_from_decimal_1():
    """ tests dec_from_decimal() for incorrect input """
    assert dec_from_decimal(None) is None


def test_dec_from_decimal_2():
    """ test dec_from_decimal() for correct input """
    assert math.isclose(dec_to_decimal(dec_from_decimal(47.19528)), 47.19528, rel_tol=0.00001)


def test_dec_from_decimal_3():
    """ test dec_from_decimal() for random input """
    _dec = random.uniform(0.0, 360.0)
    assert dec_from_decimal(_dec) is not math.nan


# +
# test: dec_to_dms(dec=math.nan)
# -
def test_dec_to_dms_1():
    """ tests dec_to_dms() for incorrect input """
    assert dec_to_dms(None) is None


def test_dec_to_dms_2():
    """ test dec_to_dms() for correct input """
    assert '+47:11:43.0' in dec_to_dms(47.19528)


def test_dec_to_hms_3():
    """ test dec_to_dms() for random input """
    _dec = random.uniform(0.0, 360.0)
    assert dec_to_dms(_dec) is not None


# +
# test: degree_to_radian(deg=math.nan)
# -
def test_degree_to_radian_1():
    """ test degree_to_radian() for incorrect input(s) """
    assert degree_to_radian(None) is math.nan


def test_degree_to_radian_2():
    """ test degree_to_radian() for incorrect input(s) """
    assert math.isclose(degree_to_radian(90.0), math.pi/2.0, rel_tol=0.000001)


def test_degree_to_radian_3():
    """ test degree_to_radian() for incorrect input(s) """
    assert math.isclose(degree_to_radian(180.0), math.pi, rel_tol=0.000001)


def test_degree_to_radian_4():
    """ test degree_to_radian() for incorrect input(s) """
    assert math.isclose(degree_to_radian(270.0), 3.0*math.pi/2.0, rel_tol=0.000001)


# +
# test: radian_to_degree(rad=math.nan)
# -
def test_radian_to_degree_1():
    """ test radian_to_degree() for incorrect input(s) """
    assert radian_to_degree(None) is math.nan


def test_radian_to_degree_2():
    """ test radian_to_degree() for incorrect input(s) """
    assert math.isclose(radian_to_degree(math.pi/2.0), 90.0, rel_tol=0.000001)


def test_radian_to_degree_3():
    """ test radian_to_degree() for incorrect input(s) """
    assert math.isclose(radian_to_degree(math.pi), 180.0, rel_tol=0.000001)


def test_radian_to_degree_4():
    """ test radian_to_degree() for incorrect input(s) """
    assert math.isclose(radian_to_degree(3.0*math.pi/2.0), 270.0, rel_tol=0.000001)


# +
# test: get_astropy_coords(name='M51')
# -
def test_get_astropy_coords_1():
    """ tests get_astropy_coords() for correct inputs """
    assert math.isclose(abs(get_astropy_coords()[0]), 202.47083, rel_tol=0.00001)


def test_get_astropy_coords_2():
    """ tests get_astropy_coords() for correct inputs """
    assert math.isclose(abs(get_astropy_coords()[1]), 47.19528, rel_tol=0.00001)


def test_get_astropy_coords_3():
    """ test get_astropy_coords() for incorrect input """
    assert get_astropy_coords(get_hash()) == (math.nan, math.nan)


def test_get_astropy_coords_4():
    """ test get_astropy_coords() for incorrect input """
    assert get_astropy_coords(None) == (math.nan, math.nan)


# +
# test: decode_verboten(string='The.ws.Quick.ws.Brown.ws.Fox.ws.Jumped.ws.Over.ws.The.ws.Lazy.ws.Dog', decode=None)
# -
def test_decode_verboten_1():
    """ tests decode_verboten() for correct inputs """
    assert isinstance(decode_verboten(get_hash()), str) is True


def test_decode_verboten_2():
    """ tests decode_verboten() for correct inputs """
    _str = get_hash()
    assert decode_verboten(encode_verboten(_str)) == _str


def test_decode_verboten_3():
    """ tests decode_verboten for incorrect input """
    assert decode_verboten(None) is None


# +
# test: encode_verboten(string='The Quick Brown Fox Jumped Over The Lazy Dog', encode=None)
# -
def test_encode_verboten_1():
    """ tests encode_verboten() for correct inputs """
    assert isinstance(encode_verboten(get_hash()), str) is True


def test_encode_verboten_2():
    """ tests encode_verboten() for correct inputs """
    _str = get_hash()
    assert encode_verboten(decode_verboten(_str)) == _str


def test_encode_verboten_3():
    """ tests encode_verboten for incorrect input """
    assert encode_verboten(None) is None


# +
# test: connect_database(connection_string='')
# -
def test_connect_database_1():
    """ test connect_database() for incorrect inputs """
    assert connect_database(None) is None


# noinspection PyUnresolvedReferences
def test_connect_database_2():
    """ test connect_database() for correct inputs """
    assert isinstance(connect_database(), sqlalchemy.orm.session.sessionmaker) is True


# noinspection PyUnresolvedReferences
def test_connect_database_3():
    """ test connect_database() for correct inputs """
    assert isinstance(connect_database()(), sqlalchemy.orm.session.Session) is True


# +
# test: disconnect_database(session=None)
# -
def test_disconnect_database_1():
    """ test disconnect_database() for incorrect inputs """
    assert disconnect_database(None) is None


def test_disconnect_database_2():
    """ test disconnect_database() for correct inputs """
    assert disconnect_database(connect_database()) is None


# +
# test: read_png(file='')
# -
def test_read_png_1():
    """ test read_png() for incorrect input """
    assert read_png(None) is None


def test_read_png_2():
    """ test read_png() for correct input """
    _res = read_png(glob.glob(f"{os.getenv('OBS_PNG')}/*.png")[0])
    assert isinstance(_res, str) and _res.strip() != ''


# +
# test: get_iers(_url=OBS_ASTROPLAN_IERS_URL)
# -
def test_get_iers_1():
    """ test get_iers() for incorrect input """
    with ptr(Exception):
        get_iers(None)


def test_get_iers_2():
    """ test get_iers() for incorrect input """
    with ptr(Exception):
        get_iers(get_hash())


def test_get_iers_3():
    """ test get_iers() for incorrect input """
    _res = get_iers().strip().lower()
    assert _res == 'astroplan' or _res == 'astropy'


# +
# test: Instrument(name='', log=None)
# -
def test_instrument_0():
    """ tests INS__ structures """
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [INS__BINNING, INS__DITHER, INS__FILTERS, INS__FLAT__EXPOSURE__TIMES, INS__INSTRUMENTS, INS__NAME,
                INS__NODES, INS__READOUT, INS__READOUT__TIMES, INS__SLITS, INS__SUPPORTED, INS__TELESCOPE,
                INS__TELESCOPES, INS__TYPE]) is True


# noinspection PyUnresolvedReferences
def test_instrument_1():
    """ test Instrument() class returns correct class """
    assert isinstance(Instrument(), instruments.factory.Instrument) is True


# +
# test: Telescope(name='', log=None)
# -
def test_telescope_0():
    """ tests TEL__ structures """
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [TEL__AKA, TEL__ALTITUDE, TEL__ASTRONOMICAL__DAWN, TEL__CIVIL__DAWN, TEL__ASTRONOMICAL__DUSK,
                TEL__CIVIL__DUSK, TEL__DEC__LIMIT, TEL__DOME__SLEW__RATE, TEL__INSTRUMENTS,
                TEL__LATITUDE, TEL__LONGITUDE, TEL__MAX__AIRMASS, TEL__MAX__MOONEX, TEL__MIN__AIRMASS,
                TEL__MIN__MOONEX, TEL__NAME, TEL__NAUTICAL__DUSK, TEL__NAUTICAL__DAWN, TEL__NODES,
                TEL__SLEW__RATE, TEL__SUPPORTED, TEL__TELESCOPES]) is True


# noinspection PyUnresolvedReferences
def test_telescope_1():
    """ test Telescope() class returns correct class """
    assert isinstance(Telescope(), telescopes.factory.Telescope) is True


# noinspection PyUnresolvedReferences
def test_telescope_2():
    """ test Telescope() returns correct class structures """
    assert isinstance(Telescope().observer, astroplan.observer.Observer) is True


# noinspection PyUnresolvedReferences
def test_telescope_3():
    """ test Telescope() returns correct class structures """
    assert isinstance(Telescope().observatory, astropy.coordinates.earth.EarthLocation) is True


def test_telescope_4():
    """ test Telescope().moon_rise() returns correct data """
    assert re.match(OBS_ISO_PATTERN, Telescope().moon_rise()) is not None


def test_telescope_5():
    """ test Telescope().moon_rise() returns correct data """
    _jd1 = isot_to_jd(Telescope().moon_rise(utc=False))
    _jd2 = isot_to_jd(Telescope().moon_rise(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_6():
    """ test Telescope().moon_set() returns correct data """
    assert re.match(OBS_ISO_PATTERN, Telescope().moon_set()) is not None


def test_telescope_7():
    """ test Telescope().moon_set() returns correct data """
    _jd1 = isot_to_jd(Telescope().moon_set(utc=False))
    _jd2 = isot_to_jd(Telescope().moon_set(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_8():
    """ test Telescope().sun_rise() returns correct data """
    assert re.match(OBS_ISO_PATTERN, Telescope().sun_rise()) is not None


def test_telescope_9():
    """ test Telescope().sun_rise() returns correct data """
    _jd1 = isot_to_jd(Telescope().sun_rise(utc=False))
    _jd2 = isot_to_jd(Telescope().sun_rise(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_10():
    """ test Telescope().sun_set() returns correct data """
    assert re.match(OBS_ISO_PATTERN, Telescope().sun_set()) is not None


def test_telescope_11():
    """ test Telescope().sun_set() returns correct data """
    _jd1 = isot_to_jd(Telescope().sun_set(utc=False))
    _jd2 = isot_to_jd(Telescope().sun_set(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_12():
    """ test Telescope().moon_rise() returns incorrect data """
    assert Telescope().moon_rise(obs_time=None) is None


def test_telescope_13():
    """ test Telescope().moon_set() returns incorrect data """
    assert Telescope().moon_set(obs_time=None) is None


def test_telescope_14():
    """ test Telescope().sun_rise() returns incorrect data """
    assert Telescope().sun_rise(obs_time=None) is None


def test_telescope_15():
    """ test Telescope().sun_set() returns incorrect data """
    assert Telescope().sun_set(obs_time=None) is None


def test_telescope_16():
    """ test Telescope.is_night() for incorrect input """
    assert Telescope().is_night(obs_time=None) is None


def test_telescope_17():
    """ test Telescope.is_night() for correct input """
    _ans = Telescope().is_night()
    assert _ans in OBS_TRUE_VALUES or _ans in OBS_FALSE_VALUES


def test_telescope_18():
    """ test Telescope.midnight() for incorrect input """
    assert Telescope().midnight(obs_time=None) is None


def test_telescope_19():
    """ test Telescope.midnight() for correct input """
    assert re.match(OBS_ISO_PATTERN, Telescope().midnight()) is not None


def test_telescope_20():
    """ test Telescope.midday() for incorrect input """
    assert Telescope().midday(obs_time=None) is None


def test_telescope_21():
    """ test Telescope.midday() for correct input """
    assert re.match(OBS_ISO_PATTERN, Telescope().midday()) is not None


def test_telescope_22():
    """ test Telescope().moon_alt() returns correct data """
    assert isinstance(Telescope().moon_alt(), float) is True


def test_telescope_23():
    """ test Telescope().moon_alt() returns correct data """
    assert (-90.0 <= Telescope().moon_alt() <= 90.0) in OBS_TRUE_VALUES


def test_telescope_24():
    """ test Telescope().moon_alt() returns incorrect data """
    assert Telescope().moon_alt(None) is math.nan


def test_telescope_25():
    """ test Telescope().moon_az() returns correct data """
    assert isinstance(Telescope().moon_az(), float) is True


def test_telescope_26():
    """ test Telescope().moon_az() returns correct data """
    assert (-360.0 <= Telescope().moon_az() <= 360.0) in OBS_TRUE_VALUES


def test_telescope_27():
    """ test Telescope().moon_az() returns incorrect data """
    assert Telescope().moon_az(None) is math.nan


def test_telescope_28():
    """ test Telescope().moon_distance() returns correct data """
    assert isinstance(Telescope().moon_distance(), float) is True


def test_telescope_29():
    """ test Telescope().moon_distance() returns incorrect data """
    assert Telescope().moon_distance(None) is math.nan


# noinspection PyUnresolvedReferences
def test_telescope_30():
    """ test Telescope().moon_coord() returns correct data """
    assert isinstance(Telescope().moon_coord(), astropy.coordinates.sky_coordinate.SkyCoord) is True


def test_telescope_31():
    """ test Telescope().moon_coord() returns incorrect data """
    assert Telescope().moon_coord(None) is None


def test_telescope_32():
    """ test Telescope().sun_alt() returns correct data """
    assert isinstance(Telescope().sun_alt(), float) is True


def test_telescope_33():
    """ test Telescope().sun_alt() returns correct data """
    assert (-90.0 <= Telescope().sun_alt() <= 90.0) in OBS_TRUE_VALUES


def test_telescope_34():
    """ test Telescope().sun_alt() returns incorrect data """
    assert Telescope().sun_alt(None) is math.nan


def test_telescope_35():
    """ test Telescope().sun_az() returns correct data """
    assert isinstance(Telescope().sun_az(), float) is True


def test_telescope_36():
    """ test Telescope().sun_az() returns correct data """
    assert (-360.0 <= Telescope().sun_az() <= 360.0) in OBS_TRUE_VALUES


def test_telescope_37():
    """ test Telescope().sun_az() returns incorrect data """
    assert Telescope().sun_az(None) is math.nan


# noinspection PyUnresolvedReferences
def test_telescope_38():
    """ test Telescope() returns correct data """
    assert isinstance(Telescope().sun_coord(), astropy.coordinates.sky_coordinate.SkyCoord) is True


def test_telescope_39():
    """ test Telescope().sun_coord() returns incorrect data """
    assert Telescope().sun_coord(None) is None


def test_telescope_40():
    """ test Telescope.dawn() for correct input """
    assert re.match(OBS_ISO_PATTERN, Telescope().dawn()) is not None


def test_telescope_41():
    """ test Telescope.dawn() for random input """
    assert re.match(OBS_ISO_PATTERN, Telescope().dawn(which=random.choice(AST__WHICH))) is not None


def test_telescope_42():
    """ test Telescope.dawn() for correct input """
    assert re.match(OBS_ISO_PATTERN, Telescope().dawn(twilight=random.choice(AST__TWILIGHT))) is not None


def test_telescope_43():
    """ test Telescope().dawn() returns incorrect data """
    assert Telescope().dawn(None) is None


def test_telescope_44():
    """ test Telescope.dusk() for correct input """
    assert re.match(OBS_ISO_PATTERN, Telescope().dusk()) is not None


def test_telescope_45():
    """ test Telescope.dusk() for random input """
    assert re.match(OBS_ISO_PATTERN, Telescope().dusk(which=random.choice(AST__WHICH))) is not None


def test_telescope_46():
    """ test Telescope.dusk() for correct input """
    assert re.match(OBS_ISO_PATTERN, Telescope().dusk(twilight=random.choice(AST__TWILIGHT))) is not None


def test_telescope_47():
    """ test Telescope().dusk() returns incorrect data """
    assert Telescope().dusk(None) is None


def test_telescope_48():
    """ test Telescope().is_observable() returns incorrect data """
    assert Telescope().is_observable(None) is None


def test_telescope_49():
    """ test Telescope().is_observable() returns incorrect data """
    assert Telescope().is_observable(obs_name=None) is None


def test_telescope_50():
    """ test Telescope().is_observable() returns incorrect data """
    _x = Telescope(name=random.choice(TEL__TELESCOPES))
    _t = _x.midnight()
    _n = 'Polaris' if TEL__LATITUDE[_x.name] >= 0.0 else 'Sigma Octantis'
    assert _x.is_observable(obs_time=_t, obs_name=_n) is True


def test_telescope_51():
    """ test Telescope().moon_civil() returns incorrect data """
    assert Telescope().moon_civil('') is None


def test_telescope_52():
    """ test Telescope().moon_civil() returns correct data """
    assert Telescope().moon_civil() in MOON__CIVIL.values()


def test_telescope_53():
    """ tests Telescope.moon_civil() structures """
    assert all([Telescope().moon_civil('2020-06-05T12:00:00.000000') == 'full',
                Telescope().moon_civil('2020-06-12T12:00:00.000000') == 'last quarter',
                Telescope().moon_civil('2020-06-20T12:00:00.000000') == 'new',
                Telescope().moon_civil('2020-06-28T12:00:00.000000') == 'first quarter',
                Telescope().moon_civil('2020-07-04T12:00:00.000000') == 'full']) is True
