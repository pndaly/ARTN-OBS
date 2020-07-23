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
  % python3.7 -m pytest -p no:warnings test_telescopes.py
"""


# +
# constant(s)
# -
INVALID_INPUTS = [None, get_hash(), {}, [], ()]


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
                TEL__SLEW__RATE, TEL__SUPPORTED, TEL__TIMEZONE, TEL__UTC__OFFSET, TEL__TELESCOPES]) in OBS_TRUE_VALUES


def test_telescope_2():
    """ test Telescope() for incorrect input(s) """
    with ptr(Exception):
        Telescope(name=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_telescope_3():
    """ test Telescope() for correct input(s) """
    assert isinstance(_tel, telescopes.factory.Telescope) in OBS_TRUE_VALUES


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


# +
# test: Telescope().dawn()
# -
def test_telescope_7():
    """ test Telescope.dawn() for incorrect input(s) """
    assert all(_tel.dawn(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_8():
    """ test Telescope.dawn() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.dawn(obs_time=get_isot(random.randint(-1000, 1000), True))) is not None


def test_telescope_9():
    """ test Telescope.dawn() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.dawn(which=random.choice(AST__WHICH))) is not None


def test_telescope_10():
    """ test Telescope.dawn() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.dawn(twilight=random.choice(AST__TWILIGHT))) is not None


# +
# test: Telescope().dusk()
# -
def test_telescope_11():
    """ test Telescope.dusk() for incorrect input(s) """
    assert all(_tel.dusk(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_12():
    """ test Telescope.dusk() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.dusk(obs_time=get_isot(random.randint(-1000, 1000), True))) is not None


def test_telescope_13():
    """ test Telescope.dusk() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.dusk(which=random.choice(AST__WHICH))) is not None


def test_telescope_14():
    """ test Telescope.dusk() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.dusk(twilight=random.choice(AST__TWILIGHT))) is not None


# +
# test: Telescope().is_day()
# -
def test_telescope_15():
    """ test Telescope.is_day() for incorrect input(s) """
    assert all(_tel.is_day(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_16():
    """ test Telescope.is_day() for correct random input(s) """
    _val = _tel.is_day(get_isot(random.randint(-1000, 1000), False))
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


def test_telescope_17():
    """ test Telescope.is_day() for correct random input(s) """
    _val = _tel.is_day(get_isot(random.randint(-1000, 1000), True))
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


# +
# test: Telescope().is_night()
# -
def test_telescope_18():
    """ test Telescope.is_night() for incorrect input(s) """
    assert all(_tel.is_night(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_19():
    """ test Telescope.is_night() for correct random input(s) """
    _val = _tel.is_night(get_isot(random.randint(-1000, 1000), False))
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


def test_telescope_20():
    """ test Telescope.is_night() for correct random input(s) """
    _val = _tel.is_night(get_isot(random.randint(-1000, 1000), True))
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


# +
# test: Telescope().is_observable()
# -
def test_telescope_21():
    """ test Telescope.is_observable() for incorrect input(s) """
    assert all(_tel.is_observable(obs_time=_k) is False for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_22():
    """ test Telescope.is_observable() for incorrect input(s) """
    assert all(_tel.is_observable(obs_name=_k) is False for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_23():
    """ test Telescope.is_observable() for incorrect input(s) """
    assert all(_tel.is_observable(obs_coords=_k) is False for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_24():
    """ test Telescope.is_observable() for correct input(s) """
    _val = _tel.is_observable(get_isot(random.randint(-1000, 1000), True), obs_name='M51')
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


def test_telescope_25():
    """ test Telescope.is_observable() for correct input(s) """
    _val = _tel.is_observable(get_isot(random.randint(-1000, 1000), True), obs_coords='13:30:00 47:11:00')
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


def test_telescope_26():
    """ test Telescope().is_observable() for correct input(s) """
    _n = 'Polaris' if TEL__LATITUDE[_tel.name] >= 0.0 else 'Sigma Octantis'
    assert _tel.is_observable(obs_time=_tel.midnight(
        obs_time=get_isot(random.randint(-1000, 1000), True)), obs_name=_n) is True


# +
# test: Telescope().lst
# -
def test_telescope_27():
    """ test Telescope.lst() for incorrect input(s) """
    assert all(_tel.lst(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_28():
    """ test Telescope.lst() for correct input(s) """
    assert re.match(OBS_RA_PATTERN, _tel.lst(get_isot(random.randint(-1000, 1000), True))) is not None


# +
# test: Telescope().midday()
# -
def test_telescope_29():
    """ test Telescope.midday() for incorrect input(s) """
    assert all(_tel.midday(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_30():
    """ test Telescope.midday() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.midday(get_isot(random.randint(-1000, 1000), False))) is not None


def test_telescope_31():
    """ test Telescope.midday() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.midday(get_isot(random.randint(-1000, 1000), True))) is not None


# +
# test: Telescope().midnight()
# -
def test_telescope_32():
    """ test Telescope.midnight() for incorrect input(s) """
    assert all(_tel.midnight(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_33():
    """ test Telescope.midnight() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.midnight(get_isot(random.randint(-1000, 1000), False))) is not None


def test_telescope_34():
    """ test Telescope.midnight() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.midnight(get_isot(random.randint(-1000, 1000), True))) is not None


# +
# test: Telescope().moon_alt()
# -
def test_telescope_35():
    """ test Telescope.moon_alt() for incorrect input(s) """
    assert all(_tel.moon_alt(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_36():
    """ test Telescope.moon_alt() for correct random input(s) """
    assert _tel.moon_alt(get_isot(random.randint(-1000, 1000), True)) is not math.nan


def test_telescope_37():
    """ test Telescope.moon_alt() for correct random input(s) """
    assert isinstance(_tel.moon_alt(get_isot(random.randint(-1000, 1000), False)), float) in OBS_TRUE_VALUES


def test_telescope_38():
    """ test Telescope.moon_alt() for correct random input(s) """
    assert (-90.0 <= _tel.moon_alt(get_isot(random.randint(-1000, 1000), True)) <= 90.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_az()
# -
def test_telescope_39():
    """ test Telescope.moon_az() for incorrect input(s) """
    assert all(_tel.moon_az(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_40():
    """ test Telescope.moon_az() for correct random input(s) """
    assert _tel.moon_az(get_isot(random.randint(-1000, 1000), True)) is not math.nan


def test_telescope_41():
    """ test Telescope.moon_az() for correct random input(s) """
    assert isinstance(_tel.moon_az(get_isot(random.randint(-1000, 1000), False)), float) in OBS_TRUE_VALUES


def test_telescope_42():
    """ test Telescope.moon_alt() for correct random input(s) """
    assert (-360.0 <= _tel.moon_az(get_isot(random.randint(-1000, 1000), True)) <= 360.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_civil()
# -
def test_telescope_43():
    """ test Telescope.moon_civil() for incorrect input(s) """
    assert all(_tel.moon_civil(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_44():
    """ test Telescope().moon_civil() for correct input(s) """
    assert _tel.moon_civil(obs_time=get_isot(random.randint(-1000, 1000), True)) in AST__MOON__CIVIL.values()


def test_telescope_45():
    """ tests Telescope.moon_civil() for correct input(s) """
    assert all([_tel.moon_civil('2020-06-05T12:00:00.000000') == 'full',
                _tel.moon_civil('2020-06-12T12:00:00.000000') == 'last quarter',
                _tel.moon_civil('2020-06-20T12:00:00.000000') == 'new',
                _tel.moon_civil('2020-06-28T12:00:00.000000') == 'first quarter',
                _tel.moon_civil('2020-07-04T12:00:00.000000') == 'full']) is True


# +
# test: Telescope().moon_altaz()
# -
def test_telescope_46():
    """ test Telescope.moon_altaz() for incorrect input(s) """
    assert all(_tel.moon_altaz(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_47():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert isinstance(_tel.moon_altaz(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


def test_telescope_48():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert isinstance(_tel.moon_altaz(
        get_isot(random.randint(-1000, 1000), False)).alt.value, float) in OBS_TRUE_VALUES


def test_telescope_49():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert (-90.0 <= _tel.moon_altaz(
        get_isot(random.randint(-1000, 1000), False)).alt.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_50():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert isinstance(_tel.moon_altaz(
        get_isot(random.randint(-1000, 1000), True)).az.value, float) in OBS_TRUE_VALUES


def test_telescope_51():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert (-360.0 <= _tel.moon_altaz(
        get_isot(random.randint(-1000, 1000), False)).az.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_52():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert isinstance(_tel.moon_altaz(
        get_isot(random.randint(-1000, 1000), False)).distance.value, float) in OBS_TRUE_VALUES


def test_telescope_53():
    """ test Telescope().moon_altaz() for correct input(s) """
    assert (_tel.moon_altaz(get_isot(random.randint(-1000, 1000), False)).distance.value > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_date()
# -
def test_telescope_54():
    """ test Telescope.moon_date() for incorrect input(s) """
    assert all(_tel.moon_date(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_55():
    """ test Telescope.moon_date() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_date(obs_time=get_isot(random.randint(-1000, 1000), True))) is not None


def test_telescope_56():
    """ test Telescope.moon_date() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_date(
        obs_time=get_isot(random.randint(-1000, 1000), True), which=random.choice(AST__WHICH))) is not None


def test_telescope_57():
    """ test Telescope.moon_date() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_date(
        obs_time=get_isot(random.randint(-1000, 1000), True), phase=random.choice(AST__MOON__WHICH))) is not None


# +
# test: Telescope().moon_distance()
# -
def test_telescope_58():
    """ test Telescope.moon_distance() for incorrect input(s) """
    assert all(_tel.moon_distance(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_59():
    """ test Telescope().moon_distance() for correct input(s) """
    assert isinstance(_tel.moon_distance(get_isot(random.randint(-1000, 1000), True)), float) in OBS_TRUE_VALUES


def test_telescope_60():
    """ test Telescope().moon_distance() for correct input(s) """
    assert (_tel.moon_distance(get_isot(random.randint(-1000, 1000), False)) > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_illumination()
# -
def test_telescope_61():
    """ test Telescope.moon_illumination() for incorrect input(s) """
    assert all(_tel.moon_illumination(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_62():
    """ test Telescope().moon_illumination() for correct input(s) """
    assert isinstance(_tel.moon_illumination(get_isot(random.randint(-1000, 1000), True)), float) in OBS_TRUE_VALUES


def test_telescope_63():
    """ test Telescope().moon_illumination() for correct input(s) """
    assert (0.0 <= _tel.moon_illumination(get_isot(random.randint(-1000, 1000), False)) <= 1.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_is_up()
# -
def test_telescope_64():
    """ test Telescope.moon_is_up() for incorrect input(s) """
    assert all(_tel.moon_is_up(obs_time=_k) is False for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_65():
    """ test Telescope.moon_is_up() for incorrect input(s) """
    assert all(_tel.moon_is_up(horizon=_k) is False for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_66():
    """ test Telescope.moon_is_up() for correct random input(s) """
    _val = _tel.moon_is_up(get_isot(random.randint(-1000, 1000), False))
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


def test_telescope_67():
    """ test Telescope.moon_is_up() for correct random input(s) """
    _val = _tel.moon_is_up(get_isot(random.randint(-1000, 1000), True))
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


# +
# test: Telescope().lunation()
# -
def test_telescope_68():
    """ test Telescope.lunation() for incorrect input(s) """
    assert all(_tel.lunation(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_69():
    """ test Telescope().lunation() for correct input(s) """
    assert isinstance(_tel.lunation(get_isot(random.randint(-1000, 1000), True)), float) in OBS_TRUE_VALUES


def test_telescope_70():
    """ test Telescope().lunation() for correct input(s) """
    assert (0.0 <= _tel.lunation(get_isot(random.randint(-1000, 1000), False)) <= 30.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_phase()
# -
def test_telescope_71():
    """ test Telescope.moon_phase() for incorrect input(s) """
    assert all(_tel.moon_phase(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_72():
    """ test Telescope().moon_phase() for correct input(s) """
    assert isinstance(_tel.moon_phase(get_isot(random.randint(-1000, 1000), True)), float) in OBS_TRUE_VALUES


def test_telescope_73():
    """ test Telescope().moon_phase() for correct input(s) """
    assert (0.0 <= _tel.moon_phase(get_isot(random.randint(-1000, 1000), False)) <= math.pi) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_rise()
# -
def test_telescope_74():
    """ test Telescope.moon_rise() for incorrect input(s) """
    assert all(_tel.moon_rise(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_75():
    """ test Telescope.moon_rise() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_rise(which=random.choice(AST__WHICH))) is not None


def test_telescope_76():
    """ test Telescope().moon_rise() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_rise()) is not None


def test_telescope_77():
    """ test Telescope().moon_rise() for correct input(s) """
    _jd1 = isot_to_jd(_tel.moon_rise(utc=False))
    _jd2 = isot_to_jd(_tel.moon_rise(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(_tel.utc_offset/24.0), rel_tol=0.000001)


# +
# test: Telescope().moon_set()
# -
def test_telescope_78():
    """ test Telescope.moon_set() for incorrect input(s) """
    assert all(_tel.moon_set(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_79():
    """ test Telescope.moon_set() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_set(which=random.choice(AST__WHICH))) is not None


def test_telescope_80():
    """ test Telescope().moon_set() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.moon_set()) is not None


def test_telescope_81():
    """ test Telescope().moon_set() for correct input(s) """
    _jd1 = isot_to_jd(_tel.moon_set(utc=False))
    _jd2 = isot_to_jd(_tel.moon_set(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(_tel.utc_offset/24.0), rel_tol=0.000001)


# +
# test: Telescope().moon_steward()
# -
def test_telescope_82():
    """ test Telescope.moon_steward() for incorrect input(s) """
    assert (all(_tel.moon_steward(obs_time=_k)[0] is None for _k in INVALID_INPUTS)
            and all(_tel.moon_steward(obs_time=_k)[1] is None for _k in INVALID_INPUTS)) in OBS_TRUE_VALUES


def test_telescope_83():
    """ test Telescope.moon_steward() for incorrect input(s) """
    assert _tel.moon_steward(obs_time=get_hash())[0] is None


def test_telescope_84():
    """ test Telescope.moon_steward() for incorrect input(s) """
    assert _tel.moon_steward(obs_time=get_hash())[1] is None


def test_telescope_85():
    """ test Telescope().moon_steward() for correct input(s) """
    assert isinstance(_tel.moon_steward(get_isot(random.randint(-1000, 1000), True))[0], float) in OBS_TRUE_VALUES


def test_telescope_86():
    """ test Telescope().moon_steward() for correct input(s) """
    assert isinstance(_tel.moon_steward(get_isot(random.randint(-1000, 1000), True))[1], str) in OBS_TRUE_VALUES


def test_telescope_87():
    """ test Telescope().moon_steward() for correct input(s) """
    assert (-15.0 <= _tel.moon_steward(get_isot(random.randint(-1000, 1000), False))[0] <= 15.0) in OBS_TRUE_VALUES


def test_telescope_88():
    """ test Telescope().moon_steward() for correct input(s) """
    assert (_tel.moon_steward(
        get_isot(random.randint(-1000, 1000), False))[1] in ['bright', 'dark', 'grey']) in OBS_TRUE_VALUES


# +
# test: Telescope().observing_end()
# -
def test_telescope_89():
    """ test Telescope.observing_end() for incorrect input(s) """
    assert all(re.match(OBS_ISO_PATTERN, _tel.observing_end(utc=_k)) is not None for _k in INVALID_INPUTS) \
           in OBS_TRUE_VALUES


def test_telescope_90():
    """ test Telescope.observing_end() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.observing_end(
        obs_time=get_isot(random.randint(-1000, 1000), True))) is not None


# +
# test: Telescope().observing_start()
# -
def test_telescope_91():
    """ test Telescope.observing_start() for incorrect input(s) """
    assert all(re.match(OBS_ISO_PATTERN, _tel.observing_start(utc=_k)) is not None for _k in INVALID_INPUTS) \
           in OBS_TRUE_VALUES

def test_telescope_92():
    """ test Telescope.observing_start() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.observing_start(
        obs_time=get_isot(random.randint(-1000, 1000), True))) is not None


# +
# test: Telescope().radec_to_altaz()
# -
def test_telescope_93():
    """ test Telescope.radec_to_altaz() for incorrect input(s) """
    assert all(_tel.radec_to_altaz(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_94():
    """ test Telescope.radec_to_altaz() for incorrect input(s) """
    assert all(_tel.radec_to_altaz(obs_name=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_95():
    """ test Telescope.radec_to_altaz() for incorrect input(s) """
    assert all(_tel.radec_to_altaz(obs_coords=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_96():
    """ test Telescope.radec_to_altaz() for correct input(s) """
    assert isinstance(_tel.radec_to_altaz(get_isot(random.randint(-1000, 1000), True), obs_name='M51'),
                      astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_97():
    """ test Telescope.radec_to_altaz() for correct input(s) """
    assert isinstance(_tel.radec_to_altaz(get_isot(random.randint(-1000, 1000), True), obs_coords='13:30:00 47:11:00'),
                      astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


def test_telescope_98():
    """ test Telescope.radec_to_altaz() for correct input(s) """
    _alt = _tel.radec_to_altaz(get_isot(random.randint(-1000, 1000), False), obs_name='M51').alt.value
    assert (-90.0 <= _alt <= 90.0) in OBS_TRUE_VALUES


def test_telescope_99():
    """ test Telescope.radec_to_altaz() for correct input(s) """
    _az = _tel.radec_to_altaz(get_isot(random.randint(-1000, 1000), False), obs_name='M51').az.value
    assert (-360.0 <= _az <= 360.0) in OBS_TRUE_VALUES


def test_telescope_100():
    """ test Telescope.radec_to_altaz() for correct input(s) """
    _alt = _tel.radec_to_altaz(get_isot(random.randint(-1000, 1000), False), obs_coords='13:30:00 47:11:00').alt.value
    assert (-90.0 <= _alt <= 90.0) in OBS_TRUE_VALUES


def test_telescope_101():
    """ test Telescope.radec_to_altaz() for correct input(s) """
    _az = _tel.radec_to_altaz(get_isot(random.randint(-1000, 1000), False), obs_coords='13:30:00 47:11:00').az.value
    assert (-360.0 <= _az <= 360.0) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_alt()
# -
def test_telescope_102():
    """ test Telescope.sun_alt() for incorrect input(s) """
    assert all(_tel.sun_alt(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_103():
    """ test Telescope.sun_alt() for correct random input(s) """
    assert _tel.sun_alt(get_isot(random.randint(-1000, 1000), True)) is not math.nan


def test_telescope_104():
    """ test Telescope.sun_alt() for correct random input(s) """
    assert isinstance(_tel.sun_alt(get_isot(random.randint(-1000, 1000), False)), float) in OBS_TRUE_VALUES


def test_telescope_105():
    """ test Telescope.sun_alt() for correct random input(s) """
    assert (-90.0 <= _tel.sun_alt(get_isot(random.randint(-1000, 1000), True)) <= 90.0) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_az()
# -
def test_telescope_106():
    """ test Telescope.sun_az() for incorrect input(s) """
    assert all(_tel.sun_az(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_107():
    """ test Telescope.sun_az() for correct random input(s) """
    assert _tel.sun_az(get_isot(random.randint(-1000, 1000), True)) is not math.nan


def test_telescope_108():
    """ test Telescope.sun_az() for correct random input(s) """
    assert isinstance(_tel.sun_az(get_isot(random.randint(-1000, 1000), False)), float) in OBS_TRUE_VALUES


def test_telescope_109():
    """ test Telescope.sun_alt() for correct random input(s) """
    assert (-360.0 <= _tel.sun_az(get_isot(random.randint(-1000, 1000), True)) <= 360.0) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_altaz()
# -
def test_telescope_110():
    """ test Telescope.sun_altaz() for incorrect input(s) """
    assert all(_tel.sun_altaz(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_111():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert isinstance(_tel.sun_altaz(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


def test_telescope_112():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert isinstance(_tel.sun_altaz(
        get_isot(random.randint(-1000, 1000), False)).alt.value, float) in OBS_TRUE_VALUES


def test_telescope_113():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert (-90.0 <= _tel.sun_altaz(
        get_isot(random.randint(-1000, 1000), False)).alt.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_114():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert isinstance(_tel.sun_altaz(
        get_isot(random.randint(-1000, 1000), True)).az.value, float) in OBS_TRUE_VALUES


def test_telescope_115():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert (-360.0 <= _tel.sun_altaz(
        get_isot(random.randint(-1000, 1000), False)).az.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_116():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert isinstance(_tel.sun_altaz(
        get_isot(random.randint(-1000, 1000), False)).distance.value, float) in OBS_TRUE_VALUES


def test_telescope_117():
    """ test Telescope().sun_altaz() for correct input(s) """
    assert (_tel.sun_altaz(get_isot(random.randint(-1000, 1000), False)).distance.value > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_rise()
# -
def test_telescope_118():
    """ test Telescope.sun_rise() for incorrect input(s) """
    assert all(_tel.sun_rise(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_119():
    """ test Telescope.sun_rise() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.sun_rise(which=random.choice(AST__WHICH))) is not None


def test_telescope_120():
    """ test Telescope().sun_rise() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.sun_rise()) is not None


def test_telescope_121():
    """ test Telescope().sun_rise() for correct input(s) """
    _jd1 = isot_to_jd(_tel.sun_rise(utc=False))
    _jd2 = isot_to_jd(_tel.sun_rise(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(_tel.utc_offset/24.0), rel_tol=0.000001)


# +
# test: Telescope().sun_set()
# -
def test_telescope_122():
    """ test Telescope.sun_set() for incorrect input(s) """
    assert all(_tel.sun_set(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_123():
    """ test Telescope.sun_set() for correct random input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.sun_set(which=random.choice(AST__WHICH))) is not None


def test_telescope_124():
    """ test Telescope().sun_set() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.sun_set()) is not None


def test_telescope_125():
    """ test Telescope().sun_set() for correct input(s) """
    _jd1 = isot_to_jd(_tel.sun_set(utc=False))
    _jd2 = isot_to_jd(_tel.sun_set(utc=True))
    assert math.isclose(abs(_jd1 - _jd2), abs(_tel.utc_offset/24.0), rel_tol=0.000001)


# +
# test: Telescope().tonight()
# -
def test_telescope_126():
    """ test Telescope.tonight() for incorrect input(s) """
    assert all(re.match(OBS_ISO_PATTERN, _tel.tonight(utc=_k)[0]) is not None for _k in INVALID_INPUTS) \
           in OBS_TRUE_VALUES


def test_telescope_127():
    """ test Telescope.tonight() for incorrect input(s) """
    assert all(re.match(OBS_ISO_PATTERN, _tel.tonight(utc=_k)[1]) is not None for _k in INVALID_INPUTS) \
           in OBS_TRUE_VALUES


def test_telescope_128():
    """ test Telescope().tonight() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.tonight(get_isot(random.randint(-1000, 1000), True))[0]) is not None


def test_telescope_129():
    """ test Telescope().tonight() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.tonight(get_isot(random.randint(-1000, 1000), False))[1]) is not None


# +
# test: Telescope().zenith()
# -
def test_telescope_130():
    """ test Telescope.zenith() for incorrect input(s) """
    assert all(_tel.zenith(obs_time=_k)[0] is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_131():
    """ test Telescope().zenith() for correct input(s) """
    assert isinstance(_tel.zenith(get_isot(random.randint(-1000, 1000), True))[0], str) in OBS_TRUE_VALUES


def test_telescope_132():
    """ test Telescope().zenith() for correct input(s) """
    assert isinstance(_tel.zenith(get_isot(random.randint(-1000, 1000), False))[1], str) in OBS_TRUE_VALUES


def test_telescope_133():
    """ test Telescope().zenith() for correct input(s) """
    assert re.match(OBS_RA_PATTERN, _tel.zenith(get_isot(random.randint(-1000, 1000), True))[0]) is not None


def test_telescope_134():
    """ test Telescope().zenith() for correct input(s) """
    assert re.match(OBS_DEC_PATTERN, _tel.zenith(get_isot(random.randint(-1000, 1000), False))[1]) is not None


# +
# test: Telescope().parallactic_angle()
# -
def test_telescope_135():
    """ test Telescope.parallactic_angle() for incorrect input(s) """
    assert all(_tel.parallactic_angle(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_136():
    """ test Telescope.parallactic_angle() for incorrect input(s) """
    assert all(_tel.parallactic_angle(obs_name=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_137():
    """ test Telescope.parallactic_angle() for incorrect input(s) """
    assert all(_tel.parallactic_angle(obs_coords=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_138():
    """ test Telescope.parallactic_angle() for correct input(s) """
    _val = _tel.parallactic_angle(get_isot(random.randint(-1000, 1000), True), obs_name='M51').degree
    assert isinstance(_val, float) in OBS_TRUE_VALUES and _val is not math.nan


def test_telescope_139():
    """ test Telescope.parallactic_angle() for correct input(s) """
    _val = _tel.parallactic_angle(get_isot(random.randint(-1000, 1000), True), obs_coords='13:30:00 47:11:00').degree
    assert (-360.0 <= _val <= 360.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_radec()
# -
def test_telescope_140():
    """ test Telescope.moon_radec() for incorrect input(s) """
    assert all(_tel.moon_radec(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_141():
    """ test Telescope().moon_radec() for correct input(s) """
    _val = _tel.moon_radec(get_isot(random.randint(-1000, 1000), False))
    assert isinstance(_val, astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_radec_today()
# -
# noinspection PyUnresolvedReferences
def test_telescope_142():
    """ test Telescope().moon_radec_today() for correct input(s) """
    assert isinstance(_tel.moon_radec_today(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_radec_now()
# -
def test_telescope_143():
    """ test Telescope().moon_radec_now() for correct input(s) """
    _val = _tel.moon_radec_now()
    assert all(isinstance(_k, float) in OBS_TRUE_VALUES for _k in [_val.ra.value, _val.dec.value, _val.distance.value])


def test_telescope_144():
    """ test Telescope().moon_radec_now() for correct input(s) """
    _val = _tel.moon_radec_now()
    assert (-360.0 <= _val.ra.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_145():
    """ test Telescope().moon_radec_now() for correct input(s) """
    _val = _tel.moon_radec_now()
    assert (-90.0 <= _val.dec.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_146():
    """ test Telescope().moon_radec_now() for correct input(s) """
    _val = _tel.moon_radec_now()
    assert (_val.distance.value > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_radec_now() vs. Telescope().moon_altaz()
# -
def test_telescope_147():
    """ test comparison of results from Telescope.moon_radec_now() vs. Telescope.moon_altaz() """
    # get alt, az from moon_coordinates_now
    _now = _tel.moon_radec_now()
    _ra, _dec = ra_from_decimal(_now.ra.value), dec_from_decimal(_now.dec.value)
    _y = _tel.radec_to_altaz(obs_coords=f'{_ra} {_dec}')
    _alt_1, _az_1 = _y.alt.value, _y.az.value
    # get alt, az from moon_altaz
    _moon = _tel.moon_altaz()
    _alt_2, _az_2 = _moon.alt.value, _moon.az.value
    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)


# +
# test: Telescope().moon_altaz_ndays()
# -
def test_telescope_148():
    """ test Telescope.moon_altaz_ndays() for incorrect input(s) """
    assert all(_tel.moon_altaz_ndays(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_149():
    """ test Telescope().moon_altaz_ndays() for correct input(s) """
    _val = _tel.moon_altaz_ndays(get_isot(random.randint(-1000, 1000), False))
    assert isinstance(_val, astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_altaz_today()
# -
# noinspection PyUnresolvedReferences
def test_telescope_150():
    """ test Telescope().moon_altaz_today() for correct input(s) """
    assert isinstance(_tel.moon_altaz_today(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_altaz_now()
# -
def test_telescope_151():
    """ test Telescope().moon_altaz_now() for correct input(s) """
    _val = _tel.moon_altaz_now()
    assert all(isinstance(_k, float) in OBS_TRUE_VALUES for _k in [_val.alt.value, _val.az.value, _val.distance.value])


def test_telescope_152():
    """ test Telescope().moon_altaz_now() for correct input(s) """
    _val = _tel.moon_altaz_now()
    assert (-360.0 <= _val.az.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_153():
    """ test Telescope().moon_altaz_now() for correct input(s) """
    _val = _tel.moon_altaz_now()
    assert (0.0 <= _val.alt.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_154():
    """ test Telescope().moon_altaz_now() for correct input(s) """
    _val = _tel.moon_altaz_now()
    assert (_val.distance.value > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_radec_now() vs. Telescope().moon_altaz_now()
# -
def test_telescope_155():
    """ test comparison of results from Telescope.moon_radec_now() vs. Telescope.moon_altaz_now() """
    # get alt, az from moon_coordinates_now
    _now = _tel.moon_radec_now()
    _ra, _dec = ra_from_decimal(_now.ra.value), dec_from_decimal(_now.dec.value)
    _y = _tel.radec_to_altaz(obs_coords=f'{_ra} {_dec}')
    _alt_1, _az_1 = _y.alt.value, _y.az.value
    # get alt, az from moon_coord
    _moon = _tel.moon_altaz_now()
    _alt_2, _az_2 = _moon.alt.value, _moon.az.value
    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)


# +
# test: Telescope().moon_exclusion()
# -
def test_telescope_156():
    """ test Telescope.moon_exclusion() for incorrect input(s) """
    assert all(_tel.moon_exclusion(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_157():
    """ test Telescope().moon_exclusion() for correct input(s) """
    _val = _tel.moon_exclusion(get_isot(random.randint(-1000, 1000), False))
    assert isinstance(_val, float) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_exclusion_today()
# -
# noinspection PyUnresolvedReferences
def test_telescope_158():
    """ test Telescope().moon_exclusion_today() for correct input(s) """
    assert isinstance(_tel.moon_exclusion_today(), np.ndarray) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_exclusion_now()
# -
def test_telescope_159():
    """ test Telescope().moon_exclusion_now() for correct input(s) """
    assert isinstance(_tel.moon_exclusion_now(), float) in OBS_TRUE_VALUES


def test_telescope_160():
    """ test Telescope().moon_exclusion_now() for correct input(s) """
    assert (_tel.min_moonex <= _tel.moon_exclusion_now() <= _tel.max_moonex) in OBS_TRUE_VALUES


# +
# test: Telescope.moon_separation()
# -
def test_telescope_161():
    """ test Telescope().moon_separation() for incorrect input(s) """
    assert all(_tel.moon_separation(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_162():
    """ test Telescope().moon_separation() for incorrect input(s) """
    assert all(_tel.moon_separation(obs_name=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_163():
    """ test Telescope().moon_separation() for incorrect input(s) """
    assert all(_tel.moon_separation(obs_coords=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_164():
    """ test Telescope().moon_separation() for correct input(s) """
    assert isinstance(_tel.moon_separation(obs_name='M51'), float) in OBS_TRUE_VALUES


def test_telescope_165():
    """ test Telescope().moon_separation() for correct input(s) """
    assert isinstance(_tel.moon_separation(obs_coords='13:30:00 47:11:00'), float) in OBS_TRUE_VALUES


# +
# test: Telescope.moon_separation_now()
# -
def test_telescope_166():
    """ test Telescope().moon_separation_now() for incorrect input(s) """
    assert all(_tel.moon_separation_now(obs_name=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_167():
    """ test Telescope().moon_separation_now() for incorrect input(s) """
    assert all(_tel.moon_separation_now(obs_coords=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_168():
    """ test Telescope().moon_separation_now() for correct input(s) """
    _val = _tel.moon_separation_now(obs_name='M51')
    assert (isinstance(_val, float) and -360.0 <= _val <= 360.0) in OBS_TRUE_VALUES


def test_telescope_169():
    """ test Telescope().moon_separation_now() for correct input(s) """
    _val = _tel.moon_separation_now(obs_coords='13:30:00 47:11:00')
    assert (isinstance(_val, float) and -360.0 <= _val <= 360.0) in OBS_TRUE_VALUES


# +
# test: Telescope.moon_separation_today()
# -
def test_telescope_170():
    """ test Telescope().moon_separation_today() for incorrect input(s) """
    assert all(_tel.moon_separation_today(obs_name=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_171():
    """ test Telescope().moon_separation_today() for incorrect input(s) """
    assert all(_tel.moon_separation_today(obs_coords=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_172():
    """ test Telescope().moon_separation_today() for correct input(s) """
    assert isinstance(_tel.moon_separation_today(obs_name='M51'), np.ndarray) in OBS_TRUE_VALUES


def test_telescope_173():
    """ test Telescope().moon_separation_today() for correct input(s) """
    assert isinstance(_tel.moon_separation_today(obs_coords='13:30:00 47:11:00'), np.ndarray) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_radec()
# -
def test_telescope_174():
    """ test Telescope.sun_radec() for incorrect input(s) """
    assert all(_tel.sun_radec(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_175():
    """ test Telescope().sun_radec() for correct input(s) """
    _val = _tel.sun_radec(get_isot(random.randint(-1000, 1000), False))
    assert isinstance(_val, astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_radec_today()
# -
# noinspection PyUnresolvedReferences
def test_telescope_176():
    """ test Telescope().sun_radec_today() for correct input(s) """
    assert isinstance(_tel.sun_radec_today(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_radec_now()
# -
def test_telescope_177():
    """ test Telescope().sun_radec_now() for correct input(s) """
    _val = _tel.sun_radec_now()
    assert all(isinstance(_k, float) in OBS_TRUE_VALUES for _k in [_val.ra.value, _val.dec.value, _val.distance.value])


def test_telescope_178():
    """ test Telescope().sun_radec_now() for correct input(s) """
    _val = _tel.sun_radec_now()
    assert (-360.0 <= _val.ra.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_179():
    """ test Telescope().sun_radec_now() for correct input(s) """
    _val = _tel.sun_radec_now()
    assert (-90.0 <= _val.dec.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_180():
    """ test Telescope().sun_radec_now() for correct input(s) """
    _val = _tel.sun_radec_now()
    assert (_val.distance.value > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_radec_now() vs. Telescope().sun_coord()
# -
def test_telescope_181():
    """ test comparison of results from Telescope.sun_radec_now() vs. Telescope.sun_coord() """
    # get alt, az from moon_coordinates_now
    _now = _tel.sun_radec_now()
    _ra, _dec = ra_from_decimal(_now.ra.value), dec_from_decimal(_now.dec.value)
    _y = _tel.radec_to_altaz(obs_coords=f'{_ra} {_dec}')
    _alt_1, _az_1 = _y.alt.value, _y.az.value
    # get alt, az from moon_coord
    _sun = _tel.sun_altaz()
    _alt_2, _az_2 = _sun.alt.value, _sun.az.value
    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)


# +
# test: Telescope().sun_altaz()
# -
def test_telescope_182():
    """ test Telescope.sun_altaz() for incorrect input(s) """
    assert all(_tel.sun_altaz(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_183():
    """ test Telescope().sun_altaz() for correct input(s) """
    _val = _tel.sun_altaz(get_isot(random.randint(-1000, 1000), False))
    assert isinstance(_val, astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_altaz_today()
# -
# noinspection PyUnresolvedReferences
def test_telescope_184():
    """ test Telescope().sun_altaz_today() for correct input(s) """
    assert isinstance(_tel.sun_altaz_today(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_altaz_now()
# -
def test_telescope_185():
    """ test Telescope().sun_altaz_now() for correct input(s) """
    _val = _tel.sun_altaz_now()
    assert all(isinstance(_k, float) in OBS_TRUE_VALUES for _k in [_val.alt.value, _val.az.value, _val.distance.value])


def test_telescope_186():
    """ test Telescope().sun_altaz_now() for correct input(s) """
    _val = _tel.sun_altaz_now()
    assert (-360.0 <= _val.az.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_187():
    """ test Telescope().sun_altaz_now() for correct input(s) """
    _val = _tel.sun_altaz_now()
    assert (0.0 <= _val.alt.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_188():
    """ test Telescope().sun_altaz_now() for correct input(s) """
    _val = _tel.sun_altaz_now()
    assert (_val.distance.value > 0.0) in OBS_TRUE_VALUES


# +
# test: Telescope().sun_radec_now() vs. Telescope().sun_altaz_now()
# -
def test_telescope_189():
    """ test comparison of results from Telescope.sun_radec_now() vs. Telescope.sun_altaz_now() """
    # get alt, az from moon_coordinates_now
    _now = _tel.sun_radec_now()
    _ra, _dec = ra_from_decimal(_now.ra.value), dec_from_decimal(_now.dec.value)
    _y = _tel.radec_to_altaz(obs_coords=f'{_ra} {_dec}')
    _alt_1, _az_1 = _y.alt.value, _y.az.value
    # get alt, az from sun_coord
    _sun = _tel.sun_altaz_now()
    _alt_2, _az_2 = _sun.alt.value, _sun.az.value
    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)


# +
# test: Telescope.sun_separation()
# -
def test_telescope_190():
    """ test Telescope().sun_separation() for incorrect input(s) """
    assert all(_tel.sun_separation(obs_time=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_191():
    """ test Telescope().sun_separation() for incorrect input(s) """
    assert all(_tel.sun_separation(obs_name=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_192():
    """ test Telescope().sun_separation() for incorrect input(s) """
    assert all(_tel.sun_separation(obs_coords=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_193():
    """ test Telescope().sun_separation() for correct input(s) """
    assert isinstance(_tel.sun_separation(obs_name='M51'), float) in OBS_TRUE_VALUES


def test_telescope_194():
    """ test Telescope().sun_separation() for correct input(s) """
    assert isinstance(_tel.sun_separation(obs_coords='13:30:00 47:11:00'), float) in OBS_TRUE_VALUES


# +
# test: Telescope.sun_separation_now()
# -
def test_telescope_195():
    """ test Telescope().sun_separation_now() for incorrect input(s) """
    assert all(_tel.sun_separation_now(obs_name=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_196():
    """ test Telescope().sun_separation_now() for incorrect input(s) """
    assert all(_tel.sun_separation_now(obs_coords=_k) is math.nan for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_197():
    """ test Telescope().sun_separation_now() for correct input(s) """
    _val = _tel.sun_separation_now(obs_name='M51')
    assert (isinstance(_val, float) and -360.0 <= _val <= 360.0) in OBS_TRUE_VALUES


def test_telescope_198():
    """ test Telescope().sun_separation_now() for correct input(s) """
    _val = _tel.sun_separation_now(obs_coords='13:30:00 47:11:00')
    assert (isinstance(_val, float) and -360.0 <= _val <= 360.0) in OBS_TRUE_VALUES


# +
# test: Telescope.sun_separation_today()
# -
def test_telescope_199():
    """ test Telescope().sun_separation_today() for incorrect input(s) """
    assert all(_tel.sun_separation_today(obs_name=_k) is None for _k in [get_hash(), {}, [], ()]) in OBS_TRUE_VALUES


def test_telescope_200():
    """ test Telescope().sun_separation_today() for incorrect input(s) """
    assert all(_tel.sun_separation_today(obs_coords=_k) is None for _k in [get_hash(), {}, [], ()]) in OBS_TRUE_VALUES


def test_telescope_201():
    """ test Telescope().sun_separation_today() for correct input(s) """
    assert isinstance(_tel.sun_separation_today(obs_name='M51'), np.ndarray) in OBS_TRUE_VALUES


def test_telescope_202():
    """ test Telescope().sun_separation_today() for correct input(s) """
    assert isinstance(_tel.sun_separation_today(obs_coords='13:30:00 47:11:00'), np.ndarray) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_illumination_ndays()
# -
def test_telescope_203():
    """ test Telescope.moon_illumination_ndays() for incorrect input(s) """
    assert all(_tel.moon_illumination_ndays(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_204():
    """ test Telescope().moon_illumination_ndays() for correct input(s) """
    _val = _tel.moon_illumination_ndays(get_isot(random.randint(-1000, 1000), False))
    assert isinstance(_val, np.ndarray) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_illumination_today()
# -
# noinspection PyUnresolvedReferences
def test_telescope_205():
    """ test Telescope().moon_illumination_today() for correct input(s) """
    assert isinstance(_tel.moon_illumination_today(), np.ndarray) in OBS_TRUE_VALUES


# +
# test: Telescope().moon_illumination_now()
# -
def test_telescope_206():
    """ test Telescope().moon_illumination_now() for correct input(s) """
    assert isinstance(_tel.moon_illumination_now(), float) in OBS_TRUE_VALUES


def test_telescope_207():
    """ test Telescope().moon_illumination_now() for correct input(s) """
    assert (0.0 <= _tel.moon_illumination_now() <= 1.0) in OBS_TRUE_VALUES

