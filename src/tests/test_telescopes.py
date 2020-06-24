#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.telescopes.factory import *

import astroplan
import astropy


# +
# doc string(s)
# -
__doc__ = """
  % python3 -m pytest test_telescopes.py
"""


# +
# variable(s)
# -
_tel = Telescope(random.choice(TEL__TELESCOPES))


# +
# test: Telescope()
# -
def test_telescope_1():
    """ tests TEL__ structures """
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [TEL__AKA, TEL__ALTITUDE, TEL__ASTRONOMICAL__DAWN, TEL__CIVIL__DAWN, TEL__ASTRONOMICAL__DUSK,
                TEL__CIVIL__DUSK, TEL__DEC__LIMIT, TEL__DOME__SLEW__RATE, TEL__INSTRUMENTS,
                TEL__LATITUDE, TEL__LONGITUDE, TEL__MAX__AIRMASS, TEL__MAX__MOONEX, TEL__MIN__AIRMASS,
                TEL__MIN__MOONEX, TEL__NAME, TEL__NAUTICAL__DUSK, TEL__NAUTICAL__DAWN, TEL__NODES,
                TEL__SLEW__RATE, TEL__SUPPORTED, TEL__TELESCOPES]) in OBS_TRUE_VALUES


def test_telescope_2():
    """ test Telescope() for incorrect input(s) """
    with ptr(Exception):
        Telescope(name=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_telescope_3():
    """ test Telescope() for correct input(s) """
    assert isinstance(_tel, telescopes.factory.Telescope) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_4():
    """ test Telescope() returns correct attribute(s) """
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [_a for _a in dir(_tel) if '__' not in _a]) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_5():
    """ test Telescope() returns correct class structures """
    assert isinstance(_tel.observer, astroplan.observer.Observer) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_6():
    """ test Telescope() returns correct class structures """
    assert isinstance(_tel.observatory, astropy.coordinates.earth.EarthLocation) in OBS_TRUE_VALUES


def test_telescope_7():
    """ test Telescope().moon_rise() returns correct data """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_rise()) is not None


def test_telescope_8():
    """ test Telescope().moon_rise() returns correct data """
    _jd1 = isot_to_jd(_tel.moon_rise(utc=False))
    _jd2 = isot_to_jd(_tel.moon_rise(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_9():
    """ test Telescope().moon_set() returns correct data """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_set()) is not None


def test_telescope_10():
    """ test Telescope().moon_set() returns correct data """
    _jd1 = isot_to_jd(_tel.moon_set(utc=False))
    _jd2 = isot_to_jd(_tel.moon_set(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_11():
    """ test Telescope().sun_rise() returns correct data """
    assert re.match(OBS_ISO_PATTERN, _tel.sun_rise()) is not None


def test_telescope_12():
    """ test Telescope().sun_rise() returns correct data """
    _jd1 = isot_to_jd(_tel.sun_rise(utc=False))
    _jd2 = isot_to_jd(_tel.sun_rise(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)

def test_telescope_13():
    """ test Telescope().sun_set() returns correct data """
    assert re.match(OBS_ISO_PATTERN, _tel.sun_set()) is not None


def test_telescope_14():
    """ test Telescope().sun_set() returns correct data """
    _jd1 = isot_to_jd(_tel.sun_set(utc=False))
    _jd2 = isot_to_jd(_tel.sun_set(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


def test_telescope_15():
    """ test Telescope().moon_rise() returns incorrect data """
    assert Telescope(random.choice(TEL__TELESCOPES)).moon_rise(obs_time=None) is None


def test_telescope_16():
    """ test Telescope().moon_set() returns incorrect data """
    assert _tel.moon_set(obs_time=None) is None


def test_telescope_17():
    """ test Telescope().sun_rise() returns incorrect data """
    assert _tel.sun_rise(obs_time=None) is None


def test_telescope_18():
    """ test Telescope().sun_set() returns incorrect data """
    assert _tel.sun_set(obs_time=None) is None


def test_telescope_19():
    """ test Telescope.is_night() for incorrect input """
    assert _tel.is_night(obs_time=None) is None


def test_telescope_20():
    """ test Telescope.is_night() for correct input """
    assert _tel.is_night() in OBS_TRUE_VALUES or _tel.is_night() in OBS_FALSE_VALUES


def test_telescope_21():
    """ test Telescope.midnight() for incorrect input """
    assert _tel.midnight(obs_time=None) is None


def test_telescope_22():
    """ test Telescope.midnight() for correct input """
    assert re.match(OBS_ISO_PATTERN, _tel.midnight()) is not None


def test_telescope_23():
    """ test Telescope.midday() for incorrect input """
    assert _tel.midday(obs_time=None) is None


def test_telescope_24():
    """ test Telescope.midday() for correct input """
    assert re.match(OBS_ISO_PATTERN, _tel.midday()) is not None


def test_telescope_25():
    """ test Telescope().moon_alt() returns correct data """
    assert isinstance(_tel.moon_alt(), float) is True


def test_telescope_26():
    """ test Telescope().moon_alt() returns correct data """
    assert (-90.0 <= _tel.moon_alt() <= 90.0) in OBS_TRUE_VALUES


def test_telescope_27():
    """ test Telescope().moon_alt() returns incorrect data """
    assert _tel.moon_alt(None) is math.nan


def test_telescope_28():
    """ test Telescope().moon_az() returns correct data """
    assert isinstance(_tel.moon_az(), float) is True


def test_telescope_29():
    """ test Telescope().moon_az() returns correct data """
    assert (-360.0 <= _tel.moon_az() <= 360.0) in OBS_TRUE_VALUES


def test_telescope_31():
    """ test Telescope().moon_az() returns incorrect data """
    assert _tel.moon_az(None) is math.nan


def test_telescope_32():
    """ test Telescope().moon_distance() returns correct data """
    assert isinstance(_tel.moon_distance(), float) is True


def test_telescope_33():
    """ test Telescope().moon_distance() returns incorrect data """
    assert _tel.moon_distance(None) is math.nan


# noinspection PyUnresolvedReferences
def test_telescope_34():
    """ test Telescope().moon_coord() returns correct data """
    assert isinstance(_tel.moon_coord(), astropy.coordinates.sky_coordinate.SkyCoord) is True


def test_telescope_35():
    """ test Telescope().moon_coord() returns incorrect data """
    assert _tel.moon_coord(None) is None


def test_telescope_36():
    """ test Telescope().sun_alt() returns correct data """
    assert isinstance(_tel.sun_alt(), float) is True


def test_telescope_37():
    """ test Telescope().sun_alt() returns correct data """
    assert (-90.0 <= _tel.sun_alt() <= 90.0) in OBS_TRUE_VALUES


def test_telescope_38():
    """ test Telescope().sun_alt() returns incorrect data """
    assert _tel.sun_alt(None) is math.nan


def test_telescope_39():
    """ test Telescope().sun_az() returns correct data """
    assert isinstance(_tel.sun_az(), float) is True


def test_telescope_40():
    """ test Telescope().sun_az() returns correct data """
    assert (-360.0 <= _tel.sun_az() <= 360.0) in OBS_TRUE_VALUES


def test_telescope_41():
    """ test Telescope().sun_az() returns incorrect data """
    assert _tel.sun_az(None) is math.nan


# noinspection PyUnresolvedReferences
def test_telescope_42():
    """ test Telescope() returns correct data """
    assert isinstance(_tel.sun_coord(), astropy.coordinates.sky_coordinate.SkyCoord) is True


def test_telescope_43():
    """ test Telescope().sun_coord() returns incorrect data """
    assert _tel.sun_coord(None) is None


def test_telescope_44():
    """ test Telescope.dawn() for correct input """
    assert re.match(OBS_ISO_PATTERN, _tel.dawn()) is not None


def test_telescope_45():
    """ test Telescope.dawn() for random input """
    assert re.match(OBS_ISO_PATTERN, _tel.dawn(which=random.choice(AST__WHICH))) is not None


def test_telescope_46():
    """ test Telescope.dawn() for correct input """
    assert re.match(OBS_ISO_PATTERN, _tel.dawn(twilight=random.choice(AST__TWILIGHT))) is not None


def test_telescope_47():
    """ test Telescope().dawn() returns incorrect data """
    assert _tel.dawn(None) is None


def test_telescope_48():
    """ test Telescope.dusk() for correct input """
    assert re.match(OBS_ISO_PATTERN, _tel.dusk()) is not None


def test_telescope_49():
    """ test Telescope.dusk() for random input """
    assert re.match(OBS_ISO_PATTERN, _tel.dusk(which=random.choice(AST__WHICH))) is not None


def test_telescope_50():
    """ test Telescope.dusk() for correct input """
    assert re.match(OBS_ISO_PATTERN, _tel.dusk(twilight=random.choice(AST__TWILIGHT))) is not None


def test_telescope_51():
    """ test Telescope().dusk() returns incorrect data """
    assert _tel.dusk(None) is None


def test_telescope_52():
    """ test Telescope().is_observable() returns incorrect data """
    assert _tel.is_observable(None) is None


def test_telescope_53():
    """ test Telescope().is_observable() returns incorrect data """
    assert _tel.is_observable(obs_name=None) is None


def test_telescope_54():
    """ test Telescope().is_observable() returns incorrect data """
    _n = 'Polaris' if TEL__LATITUDE[_tel.name] >= 0.0 else 'Sigma Octantis'
    assert _tel.is_observable(obs_time=_tel.midnight(), obs_name=_n) is True


def test_telescope_55():
    """ test Telescope().moon_civil() returns incorrect data """
    assert _tel.moon_civil('') is None


def test_telescope_56():
    """ test Telescope().moon_civil() returns correct data """
    assert _tel.moon_civil() in MOON__CIVIL.values()


def test_telescope_57():
    """ tests Telescope.moon_civil() structures """
    assert all([_tel.moon_civil('2020-06-05T12:00:00.000000') == 'full',
                _tel.moon_civil('2020-06-12T12:00:00.000000') == 'last quarter',
                _tel.moon_civil('2020-06-20T12:00:00.000000') == 'new',
                _tel.moon_civil('2020-06-28T12:00:00.000000') == 'first quarter',
                _tel.moon_civil('2020-07-04T12:00:00.000000') == 'full']) is True

    # def __init__(self, name='', log=None):
    # def telescope(cls, name='', log=None):
    # def name(self):
    # def name(self, name=''):
    # def log(self):
    # def log(self, log=None):
    # def observer(self):
    # def observatory(self):
    # def aka(self):
    # def altitude(self):
    # def astronomical_dawn(self):
    # def astronomical_dusk(self):
    # def civil_dawn(self):
    # def civil_dusk(self):
    # def dec_limit(self):
    # def dome_slew_rate(self):
    # def latitude(self):
    # def longitude(self):
    # def max_moonex(self):
    # def max_airmass(self):
    # def min_moonex(self):
    # def min_airmass(self):
    # def nautical_dawn(self):
    # def nautical_dusk(self):
    # def slew_rate(self):
    # def supported(self):
    # def __dump__(self, item=None):
    # def dawn(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False):
    # def dusk(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False):
    # def is_day(self, obs_time=Time(get_isot(0, True))):
    # def is_night(self, obs_time=Time(get_isot(0, True))):
    # def is_observable(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
    # def lst(self, obs_time=Time(get_isot(0, True))):
    # def midday(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
    # def midnight(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
    # def moon_alt(self, obs_time=Time(get_isot(0, True))):
    # def moon_az(self, obs_time=Time(get_isot(0, True))):
    # def moon_civil(self, obs_time=get_isot(0, True)):
    # def moon_coord(self, obs_time=Time(get_isot(0, True))):
    # def moon_date(self, obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__PHASE[0], utc=False):
    # def moon_distance(self, obs_time=Time(get_isot(0, True))):
    # def moon_illumination(self, obs_time=Time(get_isot(0, True))):
    # def moon_is_up(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg):
    # def moon_lunation(self, obs_time=get_isot(0, True)):
    # def moon_phase(self, obs_time=Time(get_isot(0, True))):
    # def moon_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
    # def moon_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
    # def moon_steward(self, obs_time=get_isot(0, True)):
    # def observing_end(self, obs_time=Time(get_isot(0, True)), utc=False):
    # def observing_start(self, obs_time=Time(get_isot(0, True)), utc=False):
    # def radec_to_altaz(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
    # def sun_alt(self, obs_time=Time(get_isot(0, True))):
    # def sun_az(self, obs_time=Time(get_isot(0, True))):
    # def sun_coord(self, obs_time=Time(get_isot(0, True))):
    # def sun_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
    # def sun_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
    # def tonight(self, obs_time=Time(get_isot(0, True)), utc=False):
    # def zenith(self, obs_time=Time(get_isot(0, True))):
    # def airmass_plot(self, _ra=MIN__RIGHT__ASCENSION, _dec=MIN__DECLINATION, _date=get_isot(0, True),
    # def moon_coordinates(self, date=get_isot(0, True), ndays=MIN__NDAYS, from_now=False):
    # def moon_coordinates_now(self):
    # def moon_coordinates_today(self):
    # def moon_exclusion(self, date=get_isot(0, True), ndays=MIN__NDAYS, from_now=False):
    # def moon_exclusion_now(self):
    # def moon_exclusion_today(self):
    # def moon_separation(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION, date=get_isot(0, True),
    # def moon_separation_now(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
    # def moon_separation_today(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
    # def observe(self, **kwargs):
    # def observable(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION, date=get_isot(0, True),
    # def observable_now(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
    # def observable_today(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
    # def solar_separation(ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION, date=get_isot(0, True),
    # def solar_separation_now(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
    # def solar_separation_today(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
    # def sky_separation(ra1=MIN__RIGHT__ASCENSION, dec1=MIN__DECLINATION,
