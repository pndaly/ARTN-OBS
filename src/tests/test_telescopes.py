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
                TEL__SLEW__RATE, TEL__SUPPORTED, TEL__TELESCOPES]) in OBS_TRUE_VALUES


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
    assert all(_tel.is_observable(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_22():
    """ test Telescope.is_observable() for incorrect input(s) """
    assert all(_tel.is_observable(obs_name=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_23():
    """ test Telescope.is_observable() for incorrect input(s) """
    assert all(_tel.is_observable(obs_coords=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_24():
    """ test Telescope.is_observable() for correct input(s) """
    _val = _tel.is_observable(get_isot(random.randint(-1000, 1000), True), obs_name='M51')
    assert _val in OBS_TRUE_VALUES or _val in OBS_FALSE_VALUES


def test_telescope_25():
    """ test Telescope.is_observable() for correct input(s) """
    _val = _tel.is_observable(get_isot(random.randint(-1000, 1000), False), obs_coords='13:30:00 47:11:00')
    assert _val in [OBS_TRUE_VALUES, OBS_FALSE_VALUES, None]


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
    assert _tel.moon_civil(obs_time=get_isot(random.randint(-1000, 1000), True)) in MOON__CIVIL.values()


def test_telescope_45():
    """ tests Telescope.moon_civil() for correct input(s) """
    assert all([_tel.moon_civil('2020-06-05T12:00:00.000000') == 'full',
                _tel.moon_civil('2020-06-12T12:00:00.000000') == 'last quarter',
                _tel.moon_civil('2020-06-20T12:00:00.000000') == 'new',
                _tel.moon_civil('2020-06-28T12:00:00.000000') == 'first quarter',
                _tel.moon_civil('2020-07-04T12:00:00.000000') == 'full']) is True


# +
# test: Telescope().moon_coord()
# -
def test_telescope_46():
    """ test Telescope.moon_coord() for incorrect input(s) """
    assert all(_tel.moon_coord(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_47():
    """ test Telescope().moon_coord() for correct input(s) """
    assert isinstance(_tel.moon_coord(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


def test_telescope_48():
    """ test Telescope().moon_coord() for correct input(s) """
    assert isinstance(_tel.moon_coord(
        get_isot(random.randint(-1000, 1000), False)).alt.value, float) in OBS_TRUE_VALUES


def test_telescope_49():
    """ test Telescope().moon_coord() for correct input(s) """
    assert (-90.0 <= _tel.moon_coord(
        get_isot(random.randint(-1000, 1000), False)).alt.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_50():
    """ test Telescope().moon_coord() for correct input(s) """
    assert isinstance(_tel.moon_coord(
        get_isot(random.randint(-1000, 1000), True)).az.value, float) in OBS_TRUE_VALUES


def test_telescope_51():
    """ test Telescope().moon_coord() for correct input(s) """
    assert (-360.0 <= _tel.moon_coord(
        get_isot(random.randint(-1000, 1000), False)).az.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_52():
    """ test Telescope().moon_coord() for correct input(s) """
    assert isinstance(_tel.moon_coord(
        get_isot(random.randint(-1000, 1000), False)).distance.value, float) in OBS_TRUE_VALUES


def test_telescope_53():
    """ test Telescope().moon_coord() for correct input(s) """
    assert (_tel.moon_coord(get_isot(random.randint(-1000, 1000), False)).distance.value > 0.0) in OBS_TRUE_VALUES


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
        obs_time=get_isot(random.randint(-1000, 1000), True), phase=random.choice(AST__PHASE))) is not None


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
    assert all(_tel.moon_is_up(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_65():
    """ test Telescope.moon_is_up() for incorrect input(s) """
    assert all(_tel.moon_is_up(horizon=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_66():
    """ test Telescope.moon_is_up() for correct random input(s) """
    _val = _tel.moon_is_up(get_isot(random.randint(-1000, 1000), False))
    assert _val in [OBS_TRUE_VALUES, OBS_FALSE_VALUES, None]


def test_telescope_67():
    """ test Telescope.moon_is_up() for correct random input(s) """
    _val = _tel.moon_is_up(get_isot(random.randint(-1000, 1000), True))
    assert _val in [OBS_TRUE_VALUES, OBS_FALSE_VALUES, None]


# +
# test: Telescope().moon_lunation()
# -
def test_telescope_68():
    """ test Telescope.moon_lunation() for incorrect input(s) """
    assert all(_tel.moon_lunation(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_69():
    """ test Telescope().moon_lunation() for correct input(s) """
    assert isinstance(_tel.moon_lunation(get_isot(random.randint(-1000, 1000), True)), float) in OBS_TRUE_VALUES


def test_telescope_70():
    """ test Telescope().moon_lunation() for correct input(s) """
    assert (0.0 <= _tel.moon_lunation(get_isot(random.randint(-1000, 1000), False)) <= 30.0) in OBS_TRUE_VALUES


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
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


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
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


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
    assert all(_tel.observing_end(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_90():
    """ test Telescope.observing_end() for correct input(s) """
    assert re.match(OBS_ISO_PATTERN, _tel.observing_end(
        obs_time=get_isot(random.randint(-1000, 1000), True))) is not None


# +
# test: Telescope().observing_start()
# -
def test_telescope_91():
    """ test Telescope.observing_start() for incorrect input(s) """
    assert all(_tel.observing_start(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


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
    assert all(_tel.is_observable(obs_coords=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


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
# test: Telescope().sun_coord()
# -
def test_telescope_110():
    """ test Telescope.sun_coord() for incorrect input(s) """
    assert all(_tel.sun_coord(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_telescope_111():
    """ test Telescope().sun_coord() for correct input(s) """
    assert isinstance(_tel.sun_coord(), astropy.coordinates.sky_coordinate.SkyCoord) in OBS_TRUE_VALUES


def test_telescope_112():
    """ test Telescope().sun_coord() for correct input(s) """
    assert isinstance(_tel.sun_coord(
        get_isot(random.randint(-1000, 1000), False)).alt.value, float) in OBS_TRUE_VALUES


def test_telescope_113():
    """ test Telescope().sun_coord() for correct input(s) """
    assert (-90.0 <= _tel.sun_coord(
        get_isot(random.randint(-1000, 1000), False)).alt.value <= 90.0) in OBS_TRUE_VALUES


def test_telescope_114():
    """ test Telescope().sun_coord() for correct input(s) """
    assert isinstance(_tel.sun_coord(
        get_isot(random.randint(-1000, 1000), True)).az.value, float) in OBS_TRUE_VALUES


def test_telescope_115():
    """ test Telescope().sun_coord() for correct input(s) """
    assert (-360.0 <= _tel.sun_coord(
        get_isot(random.randint(-1000, 1000), False)).az.value <= 360.0) in OBS_TRUE_VALUES


def test_telescope_116():
    """ test Telescope().sun_coord() for correct input(s) """
    assert isinstance(_tel.sun_coord(
        get_isot(random.randint(-1000, 1000), False)).distance.value, float) in OBS_TRUE_VALUES


def test_telescope_117():
    """ test Telescope().sun_coord() for correct input(s) """
    assert (_tel.sun_coord(get_isot(random.randint(-1000, 1000), False)).distance.value > 0.0) in OBS_TRUE_VALUES


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
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


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
    assert math.isclose(abs(_jd1 - _jd2), abs(OBS_UTC_OFFSET/24.0), rel_tol=0.000001)


# +
# test: Telescope().tonight()
# -
def test_telescope_126():
    """ test Telescope.tonight() for incorrect input(s) """
    assert all(_tel.tonight(obs_time=_k)[0] is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_127():
    """ test Telescope.tonight() for incorrect input(s) """
    assert all(_tel.tonight(obs_time=_k)[1] is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


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
    assert (all(_tel.zenith(obs_time=_k)[0] is None for _k in INVALID_INPUTS)
            and all(_tel.zenith(obs_time=_k)[1] is None for _k in INVALID_INPUTS)) in OBS_TRUE_VALUES


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
