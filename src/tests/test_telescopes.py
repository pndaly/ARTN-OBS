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
LOWER_BOUND = random.randint(-1000, 0)
UPPER_BOUND = random.randint(0, 1000)
ZODIAC = {1: 'Alpha Capricorni', 2: 'Alpha Aquarii', 3: 'Alpha Piscium', 4: 'Alpha Arietis', 5: 'Alpha Tauri',
          6: 'Alpha Geminorum', 7: 'Alpha Cancri', 8: 'Alpha Leonis', 9: 'Alpha Virginis', 10: 'Alpha Librae',
          11: 'Alpha Scorpii', 12: 'Alpha Sagittarii'}


# +
# variable(s)
# -
_tel = Telescope(random.choice(TEL__TELESCOPES))


# +
# Telescope()
# -
def test_telescope_0():
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [TEL__AKA, TEL__ALTITUDE, TEL__ASTRONOMICAL__DAWN, TEL__CIVIL__DAWN, TEL__ASTRONOMICAL__DUSK,
                TEL__CIVIL__DUSK, TEL__DEC__LIMIT, TEL__DOME__SLEW__RATE, TEL__INSTRUMENTS,
                TEL__LATITUDE, TEL__LONGITUDE, TEL__MAX__AIRMASS, TEL__MAX__MOONEX, TEL__MIN__AIRMASS,
                TEL__MIN__MOONEX, TEL__NAME, TEL__NAUTICAL__DUSK, TEL__NAUTICAL__DAWN, TEL__NODES,
                TEL__SLEW__RATE, TEL__SUPPORTED, TEL__TIMEZONE, TEL__UTC__OFFSET, TEL__TELESCOPES])


def test_telescope_1():
    with ptr(Exception):
        Telescope(name=random.choice(INVALID_INPUTS))


def test_telescope_2():
    # noinspection PyUnresolvedReferences
    assert isinstance(_tel, telescopes.factory.Telescope)


def test_telescope_3():
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [_a for _a in dir(_tel) if '__' not in _a])


def test_telescope_5():
    # noinspection PyUnresolvedReferences
    assert isinstance(_tel.observer, astroplan.observer.Observer)


def test_telescope_6():
    # noinspection PyUnresolvedReferences
    assert isinstance(_tel.observatory, astropy.coordinates.earth.EarthLocation)


# +
# Telescope().dawn(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False)
# -
def test_telescope_10():
    assert all(_tel.dawn(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_11():
    _val_t = _tel.dawn(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.dawn(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_12():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.dawn(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), which=_which)
    _val_f = _tel.dawn(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), which=_which)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_13():
    _twilight = random.choice(AST__TWILIGHT)
    _val_t = _tel.dawn(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), twilight=_twilight)
    _val_f = _tel.dawn(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), twilight=_twilight)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_14():
    _offset = random.randint(LOWER_BOUND, UPPER_BOUND)
    _twilight = random.choice(AST__TWILIGHT)
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.dawn(obs_time=get_isot(_offset, True), which=_which, twilight=_twilight, utc=True))
    _val_f = isot_to_jd(_tel.dawn(obs_time=get_isot(_offset, True), which=_which, twilight=_twilight, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


def test_telescope_15():
    _offset = random.randint(LOWER_BOUND, UPPER_BOUND)
    _twilight = random.choice(AST__TWILIGHT)
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.dawn(obs_time=get_isot(_offset, False), which=_which, twilight=_twilight, utc=True))
    _val_f = isot_to_jd(_tel.dawn(obs_time=get_isot(_offset, False), which=_which, twilight=_twilight, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().dusk(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False)
# -
def test_telescope_20():
    assert all(_tel.dusk(obs_time=_k) is None for _k in INVALID_INPUTS) in OBS_TRUE_VALUES


def test_telescope_21():
    _val_t = _tel.dusk(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.dusk(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_22():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.dusk(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), which=_which)
    _val_f = _tel.dusk(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), which=_which)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_23():
    _twilight = random.choice(AST__TWILIGHT)
    _val_t = _tel.dusk(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), twilight=_twilight)
    _val_f = _tel.dusk(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), twilight=_twilight)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_24():
    _offset = random.randint(LOWER_BOUND, UPPER_BOUND)
    _twilight = random.choice(AST__TWILIGHT)
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.dusk(obs_time=get_isot(_offset, True), which=_which, twilight=_twilight, utc=True))
    _val_f = isot_to_jd(_tel.dusk(obs_time=get_isot(_offset, True), which=_which, twilight=_twilight, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


def test_telescope_25():
    _offset = random.randint(LOWER_BOUND, UPPER_BOUND)
    _twilight = random.choice(AST__TWILIGHT)
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.dusk(obs_time=get_isot(_offset, False), which=_which, twilight=_twilight, utc=True))
    _val_f = isot_to_jd(_tel.dusk(obs_time=get_isot(_offset, False), which=_which, twilight=_twilight, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().is_day(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_30():
    assert all(_tel.is_day(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_31():
    _val_t = _tel.is_day(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.is_day(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k in [True, False] for _k in [_val_t, _val_f])


# +
# Telescope().is_night(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_40():
    assert all(_tel.is_night(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_41():
    _val_t = _tel.is_night(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.is_night(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k in [True, False] for _k in [_val_t, _val_f])


# +
# Telescope().is_observable(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_50():
    assert all(_tel.is_observable(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_51():
    assert all(_tel.is_observable(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_52():
    assert all(_tel.is_observable(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_53():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.is_observable(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.is_observable(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(_k in [True, False, None] for _k in [_val_t, _val_f])


def test_telescope_54():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.is_observable(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.is_observable(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(_k in [True, False, None] for _k in [_val_t, _val_f])


def test_telescope_55():
    _val_t = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_tel.is_observable(obs_time=_k, obs_name='Polaris') is True for _k in [_val_t, _val_f])


def test_telescope_56():
    _val_t = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_tel.is_observable(obs_time=_k, obs_name='Sigma Octanis') is False for _k in [_val_t, _val_f])


# +
# Telescope().is_observable_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS)
# -
def test_telescope_60():
    _ndays = random.randint(1, 5)
    assert all(_tel.is_observable_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_61():
    _ndays = random.randint(1, 5)
    assert all(_tel.is_observable_ndays(obs_name=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_62():
    _ndays = random.randint(1, 5)
    assert all(_tel.is_observable_ndays(obs_coords=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_63():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _offset = random.randint(LOWER_BOUND, UPPER_BOUND)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.is_observable_ndays(obs_time=get_isot(_offset, True), obs_name=_t1, ndays=_ndays)
    _val_f = _tel.is_observable_ndays(obs_time=get_isot(_offset, False), obs_name=_t1, ndays=_ndays)
    assert all(_k in [True, False, None] for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_64():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _offset = random.randint(LOWER_BOUND, UPPER_BOUND)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.is_observable_ndays(obs_time=get_isot(_offset, True), obs_coords=_coords)
    _val_f = _tel.is_observable_ndays(obs_time=get_isot(_offset, False), obs_coords=_coords)
    assert all(_k in [True, False, None] for _k in [_val_t[_num], _val_f[_num]])


# +
# Telescope().is_observable_now(self, obs_name='', obs_coords='')
# -
def test_telescope_70():
    assert all(_tel.is_observable_now(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_71():
    assert all(_tel.is_observable_now(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_72():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.is_observable_now(obs_name=_t1)
    assert (_val in [True, False, None])


def test_telescope_73():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.is_observable_now(obs_coords=_coords)
    assert (_val in [True, False, None])


# +
# Telescope().is_observable_today(self, obs_name='', obs_coords='')
# -
def test_telescope_80():
    assert all(_tel.is_observable_today(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_81():
    assert all(_tel.is_observable_today(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_82():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.is_observable_today(obs_name=_t1)
    assert (_val[_num] in [True, False, None])


def test_telescope_83():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.is_observable_today(obs_coords=_coords)
    assert (_val[_num] in [True, False, None])


# +
# Telescope().lst(self, obs_time=Time(get_isot(0, True))
# -
def test_telescope_90():
    assert all(_tel.lst(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_91():
    _val_t = _tel.lst(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.lst(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_RA_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().lunation(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_100():
    assert all(_tel.lunation(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_101():
    _val_t = _tel.lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_102():
    _val_t = _tel.lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(0.0 <= _k <= 30.0 for _k in [_val_t, _val_f])


# +
# Telescope().midday(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_110():
    assert all(_tel.midday(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_111():
    _val_t = _tel.midday(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.midday(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_112():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.midday(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), which=_which)
    _val_f = _tel.midday(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), which=_which)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().midnight(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_120():
    assert all(_tel.midnight(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_121():
    _val_t = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_122():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), which=_which)
    _val_f = _tel.midnight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), which=_which)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().observing_end(self, obs_time=Time(get_isot(0, True)), utc=False)
# -
def test_telescope_130():
    assert all(re.match(OBS_ISO_PATTERN, _tel.observing_end(utc=_k)) is not None for _k in INVALID_INPUTS)


def test_telescope_131():
    _val_t = _tel.observing_end(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.observing_end(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().observing_start(self, obs_time=Time(get_isot(0, True)), utc=False)
# -
def test_telescope_140():
    assert all(re.match(OBS_ISO_PATTERN, _tel.observing_start(utc=_k)) is not None for _k in INVALID_INPUTS)


def test_telescope_141():
    _val_t = _tel.observing_start(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.observing_start(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().parallactic_angle(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_150():
    assert all(_tel.parallactic_angle(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_151():
    assert all(_tel.parallactic_angle(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_152():
    assert all(_tel.parallactic_angle(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_153():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_154():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_155():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_156():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.parallactic_angle(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().position_angle(self, obs_name_1='', obs_name_2='', obs_coords_1='', obs_coords_2='')
# -
def test_telescope_160():
    assert all(_tel.position_angle(obs_name_1=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_161():
    assert all(_tel.position_angle(obs_name_2=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_162():
    assert all(_tel.position_angle(obs_coords_1=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_163():
    assert all(_tel.position_angle(obs_coords_2=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_164():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _t2 = _t1.replace('Alpha', 'Beta')
    assert -360.0 <= _tel.position_angle(obs_name_1=_t1, obs_name_2=_t2) <= 360.0


def test_telescope_165():
    _ra_1 = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_1 = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_1 = f"{random.choice(['-', '+'])}{_dec_1}"
    _coords_1 = f"{_ra_1} {_dec_1}"
    _ra_2 = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_2 = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_2 = f"{random.choice(['-', '+'])}{_dec_2}"
    _coords_2 = f"{_ra_2} {_dec_2}"
    assert (-360.0 <= _tel.position_angle(obs_coords_1=_coords_1, obs_coords_2=_coords_2) <= 360.0)


# +
# Telescope().radec_to_altaz(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_170():
    assert all(_tel.radec_to_altaz(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_171():
    assert all(_tel.radec_to_altaz(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_172():
    assert all(_tel.radec_to_altaz(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_173():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_174():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(isinstance(_k, float) for _k in
               [_val_t.alt.value, _val_t.az.value, _val_f.alt.value, _val_f.az.value])


def test_telescope_175():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.alt.value, _val_f.alt.value])


def test_telescope_176():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.radec_to_altaz(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.az.value, _val_f.az.value])


def test_telescope_177():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.radec_to_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.radec_to_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t.alt.value, _val_t.az.value, _val_f.alt.value, _val_f.az.value])


def test_telescope_178():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.radec_to_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.radec_to_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.alt.value, _val_f.alt.value])


def test_telescope_179():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.radec_to_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.radec_to_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.az.value, _val_f.az.value])


# +
# Telescope().sky_separation(self, obs_name_1='', obs_name_2='', obs_coords_1='', obs_coords_2='')
# -
def test_telescope_180():
    assert all(_tel.sky_separation(obs_name_1=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_181():
    assert all(_tel.sky_separation(obs_name_2=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_182():
    assert all(_tel.sky_separation(obs_coords_1=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_183():
    assert all(_tel.sky_separation(obs_coords_2=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_184():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _t2 = _t1.replace('Alpha', 'Beta')
    assert -360.0 <= _tel.sky_separation(obs_name_1=_t1, obs_name_2=_t2) <= 360.0


def test_telescope_185():
    _ra_1 = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_1 = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_1 = f"{random.choice(['-', '+'])}{_dec_1}"
    _coords_1 = f"{_ra_1} {_dec_1}"
    _ra_2 = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_2 = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec_2 = f"{random.choice(['-', '+'])}{_dec_2}"
    _coords_2 = f"{_ra_2} {_dec_2}"
    assert (-360.0 <= _tel.sky_separation(obs_coords_1=_coords_1, obs_coords_2=_coords_2) <= 360.0)


# +
# Telescope().target_airmass(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_190():
    assert all(_tel.target_airmass(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_191():
    assert all(_tel.target_airmass(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_192():
    assert all(_tel.target_airmass(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_193():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_194():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_195():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_196():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.target_airmass(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().target_airmass_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS)
# -
def test_telescope_200():
    _ndays = random.randint(1, 5)
    assert all(_tel.target_airmass_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_201():
    _ndays = random.randint(1, 5)
    assert all(_tel.target_airmass_ndays(obs_name=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_202():
    _ndays = random.randint(1, 5)
    assert all(_tel.target_airmass_ndays(obs_coords=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_203():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.target_airmass_ndays(obs_name=_t1, ndays=_ndays)
    assert isinstance(_val[_num], float)


def test_telescope_204():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.target_airmass_ndays(obs_name=_t1, ndays=_ndays)
    assert (-360.0 <= _val[_num] <= 360.0)


def test_telescope_205():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.target_airmass_ndays(obs_coords=_coords, ndays=_ndays)
    assert isinstance(_val[_num], float)


def test_telescope_206():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.target_airmass_ndays(obs_coords=_coords, ndays=_ndays)
    assert (-360.0 <= _val[_num] <= 360.0)


# +
# Telescope().target_airmass_now(self, obs_name='', obs_coords='')
# -
def test_telescope_210():
    assert all(_tel.target_airmass_now(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_211():
    assert all(_tel.target_airmass_now(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_212():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.target_airmass_now(obs_name=_t1)
    _val_f = _tel.target_airmass_now(obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_213():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.target_airmass_now(obs_name=_t1)
    _val_f = _tel.target_airmass_now(obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_214():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.target_airmass_now(obs_coords=_coords)
    _val_f = _tel.target_airmass_now(obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_215():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.target_airmass_now(obs_coords=_coords)
    assert (-360.0 <= _val <= 360.0)


# +
# Telescope().target_airmass_today(self, obs_name='', obs_coords='')
# -
def test_telescope_220():
    assert all(_tel.target_airmass_today(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_221():
    assert all(_tel.target_airmass_today(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_222():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.target_airmass_today(obs_name=_t1)
    assert isinstance(_val[_num], float)


def test_telescope_223():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.target_airmass_today(obs_name=_t1)
    assert (-360.0 <= _val[_num] <= 360.0)


def test_telescope_224():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.target_airmass_today(obs_coords=_coords)
    assert isinstance(_val[_num], float)


def test_telescope_225():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.target_airmass_today(obs_coords=_coords)
    assert (-360.0 <= _val[_num] <= 360.0)


# +
# Telescope().target_rise(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', which=AST__WHICH[-1], utc=False)
# -
def test_telescope_230():
    assert all(_tel.target_rise(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_231():
    assert all(_tel.target_rise(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_232():
    assert all(_tel.target_rise(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_233():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d2 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d3 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)
    _d4 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)

    _m1 = int(_d1.split('T')[0].split('-')[1])
    _m2 = int(_d2.split('T')[0].split('-')[1])
    _m3 = int(_d3.split('T')[0].split('-')[1])
    _m4 = int(_d4.split('T')[0].split('-')[1])

    _val_1 = _tel.target_rise(obs_time=_d1, obs_name=ZODIAC.get(_m1, 'Polaris'))
    _val_2 = _tel.target_rise(obs_time=_d2, obs_name=ZODIAC.get(_m2, 'Polaris'))
    _val_3 = _tel.target_rise(obs_time=_d3, obs_name=ZODIAC.get(_m3, 'Polaris'))
    _val_4 = _tel.target_rise(obs_time=_d4, obs_name=ZODIAC.get(_m4, 'Polaris'))
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_1, _val_2, _val_3, _val_4])


def test_telescope_234():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _m1 = int(_d1.split('T')[0].split('-')[1])
    _val_t = isot_to_jd(_tel.target_rise(obs_time=_d1, obs_name=ZODIAC.get(_m1, 'Polaris'), utc=True))
    _val_f = isot_to_jd(_tel.target_rise(obs_time=_d1, obs_name=ZODIAC.get(_m1, 'Polaris'), utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


def test_telescope_235():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d2 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d3 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)
    _d4 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)

    _m1 = int(_d1.split('T')[0].split('-')[1])
    _m2 = int(_d2.split('T')[0].split('-')[1])
    _m3 = int(_d3.split('T')[0].split('-')[1])
    _m4 = int(_d4.split('T')[0].split('-')[1])

    _t1 = get_astropy_coords(name=ZODIAC.get(_m1, 'Polaris'))
    _t2 = get_astropy_coords(name=ZODIAC.get(_m2, 'Polaris'))
    _t3 = get_astropy_coords(name=ZODIAC.get(_m3, 'Polaris'))
    _t4 = get_astropy_coords(name=ZODIAC.get(_m4, 'Polaris'))

    _coords1 = f"{ra_from_decimal(_t1[0])} {dec_from_decimal(_t1[1])}"
    _coords2 = f"{ra_from_decimal(_t2[0])} {dec_from_decimal(_t2[1])}"
    _coords3 = f"{ra_from_decimal(_t3[0])} {dec_from_decimal(_t3[1])}"
    _coords4 = f"{ra_from_decimal(_t4[0])} {dec_from_decimal(_t4[1])}"

    _val_1 = _tel.target_rise(obs_time=_d1, obs_coords=_coords1)
    _val_2 = _tel.target_rise(obs_time=_d2, obs_coords=_coords2)
    _val_3 = _tel.target_rise(obs_time=_d3, obs_coords=_coords3)
    _val_4 = _tel.target_rise(obs_time=_d4, obs_coords=_coords4)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_1, _val_2, _val_3, _val_4])


def test_telescope_236():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _m1 = int(_d1.split('T')[0].split('-')[1])
    _t1 = get_astropy_coords(name=ZODIAC.get(_m1, 'Polaris'))
    _coords1 = f"{ra_from_decimal(_t1[0])} {dec_from_decimal(_t1[1])}"

    _val_1 = isot_to_jd(_tel.target_rise(obs_time=_d1, obs_coords=_coords1, utc=True))
    _val_2 = isot_to_jd(_tel.target_rise(obs_time=_d1, obs_coords=_coords1, utc=False))
    assert math.isclose(abs(_val_1 - _val_2), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().target_set()
# -
def test_telescope_240():
    assert all(_tel.target_set(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_241():
    assert all(_tel.target_set(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_242():
    assert all(_tel.target_set(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_243():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d2 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d3 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)
    _d4 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)

    _m1 = int(_d1.split('T')[0].split('-')[1])
    _m2 = int(_d2.split('T')[0].split('-')[1])
    _m3 = int(_d3.split('T')[0].split('-')[1])
    _m4 = int(_d4.split('T')[0].split('-')[1])

    _val_1 = _tel.target_set(obs_time=_d1, obs_name=ZODIAC.get(_m1, 'Polaris'))
    _val_2 = _tel.target_set(obs_time=_d2, obs_name=ZODIAC.get(_m2, 'Polaris'))
    _val_3 = _tel.target_set(obs_time=_d3, obs_name=ZODIAC.get(_m3, 'Polaris'))
    _val_4 = _tel.target_set(obs_time=_d4, obs_name=ZODIAC.get(_m4, 'Polaris'))
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_1, _val_2, _val_3, _val_4])


def test_telescope_244():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _m1 = int(_d1.split('T')[0].split('-')[1])
    _val_t = isot_to_jd(_tel.target_set(obs_time=_d1, obs_name=ZODIAC.get(_m1, 'Polaris'), utc=True))
    _val_f = isot_to_jd(_tel.target_set(obs_time=_d1, obs_name=ZODIAC.get(_m1, 'Polaris'), utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


def test_telescope_245():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d2 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _d3 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)
    _d4 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)

    _m1 = int(_d1.split('T')[0].split('-')[1])
    _m2 = int(_d2.split('T')[0].split('-')[1])
    _m3 = int(_d3.split('T')[0].split('-')[1])
    _m4 = int(_d4.split('T')[0].split('-')[1])

    _t1 = get_astropy_coords(name=ZODIAC.get(_m1, 'Polaris'))
    _t2 = get_astropy_coords(name=ZODIAC.get(_m2, 'Polaris'))
    _t3 = get_astropy_coords(name=ZODIAC.get(_m3, 'Polaris'))
    _t4 = get_astropy_coords(name=ZODIAC.get(_m4, 'Polaris'))

    _coords1 = f"{ra_from_decimal(_t1[0])} {dec_from_decimal(_t1[1])}"
    _coords2 = f"{ra_from_decimal(_t2[0])} {dec_from_decimal(_t2[1])}"
    _coords3 = f"{ra_from_decimal(_t3[0])} {dec_from_decimal(_t3[1])}"
    _coords4 = f"{ra_from_decimal(_t4[0])} {dec_from_decimal(_t4[1])}"

    _val_1 = _tel.target_set(obs_time=_d1, obs_coords=_coords1)
    _val_2 = _tel.target_set(obs_time=_d2, obs_coords=_coords2)
    _val_3 = _tel.target_set(obs_time=_d3, obs_coords=_coords3)
    _val_4 = _tel.target_set(obs_time=_d4, obs_coords=_coords4)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_1, _val_2, _val_3, _val_4])


def test_telescope_246():
    _d1 = get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)
    _m1 = int(_d1.split('T')[0].split('-')[1])
    _t1 = get_astropy_coords(name=ZODIAC.get(_m1, 'Polaris'))
    _coords1 = f"{ra_from_decimal(_t1[0])} {dec_from_decimal(_t1[1])}"

    _val_1 = isot_to_jd(_tel.target_set(obs_time=_d1, obs_coords=_coords1, utc=True))
    _val_2 = isot_to_jd(_tel.target_set(obs_time=_d1, obs_coords=_coords1, utc=False))
    assert math.isclose(abs(_val_1 - _val_2), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().tonight(self, obs_time=Time(get_isot(0, True)), utc=False)
# -
def test_telescope_250():
    _val_t = _tel.tonight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.tonight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t[0], _val_f[0]])


def test_telescope_251():
    _val_t = _tel.tonight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.tonight(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t[1], _val_f[1]])


# +
# Telescope().zenith(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_260():
    _val_t = _tel.zenith(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.zenith(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, str) for _k in [_val_t[0], _val_f[0]])


def test_telescope_261():
    _val_t = _tel.zenith(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.zenith(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_RA_PATTERN, _k) is not None for _k in [_val_t[0], _val_f[0]])


def test_telescope_262():
    _val_t = _tel.zenith(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.zenith(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_DEC_PATTERN, _k) is not None for _k in [_val_t[1], _val_f[1]])


# +
# Telescope().fm_lunation(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_270():
    assert all(_tel.fm_lunation(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_271():
    _val_t = _tel.fm_lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.fm_lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_272():
    _val_t = _tel.fm_lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.fm_lunation(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(0.0 <= _k <= 30.0 for _k in [_val_t, _val_f])


# +
# Telescope().fm_moon_date(obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__MOON__WHICH[0], utc_offset=0.0)
# -
def test_telescope_280():
    assert all(_tel.fm_moon_date(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_281():
    _val_t = _tel.fm_moon_date(
        obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), utc_offset=_tel.utc_offset)
    _val_f = _tel.fm_moon_date(
        obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), utc_offset=_tel.utc_offset)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_282():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.fm_moon_date(
        obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), which=_which, utc_offset=_tel.utc_offset)
    _val_f = _tel.fm_moon_date(
        obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), which=_which, utc_offset=_tel.utc_offset)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_283():
    _phase = random.choice(AST__MOON__WHICH)
    _val_t = _tel.fm_moon_date(
        obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), phase=_phase, utc_offset=_tel.utc_offset)
    _val_f = _tel.fm_moon_date(
        obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), phase=_phase, utc_offset=_tel.utc_offset)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])
