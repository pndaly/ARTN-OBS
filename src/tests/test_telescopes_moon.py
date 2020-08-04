#!/usr/bin/env python3


# +
# import(s)
# -
from . import *
from src.telescopes.factory import *

import astropy
import numpy


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_telescopes_moon.py
"""


# +
# variable(s)
# -
_tel = Telescope(random.choice(TEL__TELESCOPES))


# +
# Telescope().moon_alt(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_0():
    assert all(_tel.moon_alt(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_1():
    _val_t = _tel.moon_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_2():
    _val_t = _tel.moon_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_altaz(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_10():
    assert all(_tel.moon_altaz(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_11():
    _val_t = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_12():
    _val_t = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.alt.value, _val_t.az.value, _val_t.distance.value,
                _val_f.alt.value, _val_f.az.value, _val_f.distance.value])


def test_telescope_13():
    _val_t = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.alt.value, _val_f.alt.value])


def test_telescope_14():
    _val_t = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.az.value, _val_f.az.value])


def test_telescope_15():
    _val_t = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().moon_altaz_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_20():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_altaz_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_21():
    _val_t = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_22():
    _val_t = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in
               [_val_t[TEST_NUM].alt.value, _val_t[TEST_NUM].az.value, _val_t[TEST_NUM].distance.value,
                _val_f[TEST_NUM].alt.value, _val_f[TEST_NUM].az.value, _val_f[TEST_NUM].distance.value])


def test_telescope_23():
    _val_t = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[TEST_NUM].alt.value, _val_f[TEST_NUM].alt.value])


def test_telescope_24():
    _val_t = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[TEST_NUM].az.value, _val_f[TEST_NUM].az.value])


def test_telescope_25():
    _val_t = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(_k > 0.0 for _k in [_val_t[TEST_NUM].distance.value, _val_f[TEST_NUM].distance.value])


# +
# Telescope().moon_az(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_30():
    assert all(_tel.moon_az(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_31():
    _val_t = _tel.moon_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_32():
    _val_t = _tel.moon_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_civil(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_40():
    assert all(_tel.moon_civil(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_41():
    _val_t = _tel.moon_civil(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_civil(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k in list(AST__MOON__CIVIL.values()) for _k in [_val_t, _val_f])


def test_telescope_42():
    assert all([_tel.moon_civil('2020-06-05T12:00:00.000000') == 'full',
                _tel.moon_civil('2020-06-12T12:00:00.000000') == 'last quarter',
                _tel.moon_civil('2020-06-20T12:00:00.000000') == 'new',
                _tel.moon_civil('2020-06-28T12:00:00.000000') == 'first quarter',
                _tel.moon_civil('2020-07-04T12:00:00.000000') == 'full'])


# +
# Telescope().moon_date(self, obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__MOON__WHICH[0], utc=False)
# -
def test_telescope_50():
    assert all(_tel.moon_date(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_51():
    _val_t = _tel.moon_date(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_date(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_52():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.moon_date(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), which=_which)
    _val_f = _tel.moon_date(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), which=_which)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_53():
    _phase = random.choice(AST__MOON__WHICH)
    _val_t = _tel.moon_date(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), phase=_phase)
    _val_f = _tel.moon_date(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), phase=_phase)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().moon_dec(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_60():
    assert all(_tel.moon_dec(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_61():
    _val_t = _tel.moon_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_62():
    _val_t = _tel.moon_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_distance(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_70():
    assert all(_tel.moon_distance(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_71():
    _val_t = _tel.moon_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_72():
    _val_t = _tel.moon_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_exclusion(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_80():
    assert all(_tel.moon_exclusion(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_81():
    _val_t = _tel.moon_exclusion(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_exclusion(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_82():
    _min = _tel.min_moonex
    _max = _tel.max_moonex + _tel.min_moonex
    _val_t = _tel.moon_exclusion(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_exclusion(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_min <= _k <= _max for _k in [_val_t, _val_f])


# +
# Telescope().moon_exclusion_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_90():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_exclusion_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_91():
    _val_t = _tel.moon_exclusion_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_exclusion_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, numpy.ndarray) for _k in [_val_t, _val_f])


def test_telescope_92():
    _val_t = _tel.moon_exclusion_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_exclusion_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_93():
    _min = _tel.min_moonex
    _max = _tel.max_moonex + _tel.min_moonex
    _val_t = _tel.moon_exclusion_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_exclusion_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(_min <= _k <= _max for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


# +
# Telescope().moon_illumination(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_100():
    assert all(_tel.moon_illumination(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_101():
    _val_t = _tel.moon_illumination(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_illumination(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_102():
    _val_t = _tel.moon_illumination(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_illumination(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(0.0 <= _k <= 1.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_illumination_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_110():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_illumination_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_111():
    _val_t = _tel.moon_illumination_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_illumination_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, numpy.ndarray) for _k in [_val_t, _val_f])


def test_telescope_112():
    _val_t = _tel.moon_illumination_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_illumination_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_113():
    _val_t = _tel.moon_illumination_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_illumination_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(0.0 <= _k <= 1.0 for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


# +
# Telescope().moon_is_up(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg)
# -
def test_telescope_120():
    assert all(_tel.moon_is_up(obs_time=_k) in [True, False, None] for _k in TEST_INVALID_INPUTS)


def test_telescope_121():
    assert all(_tel.moon_is_up(horizon=_k) is None for _k in TEST_INVALID_INPUTS[:-2])


def test_telescope_122():
    assert _tel.moon_is_up(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True)) in [True, False, None]


def test_telescope_123():
    assert _tel.moon_is_up(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False)) in [True, False, None]


# +
# Telescope().moon_is_down(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg)
# -
def test_telescope_130():
    assert all(_tel.moon_is_down(obs_time=_k) in [True, False, None] for _k in TEST_INVALID_INPUTS)


def test_telescope_131():
    assert all(_tel.moon_is_down(horizon=_k) is None for _k in TEST_INVALID_INPUTS[:-2])


def test_telescope_132():
    assert _tel.moon_is_down(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True)) in [True, False, None]


def test_telescope_133():
    assert _tel.moon_is_down(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False)) in [True, False, None]


# +
# Telescope().moon_phase(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_140():
    assert all(_tel.moon_phase(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_141():
    _val_t = _tel.moon_phase(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_phase(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_142():
    _val_t = _tel.moon_phase(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_phase(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-math.pi <= _k <= math.pi for _k in [_val_t, _val_f])


# +
# Telescope().moon_phase_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_150():
    assert all(_tel.moon_phase_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_151():
    _val_t = _tel.moon_phase_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_phase_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, numpy.ndarray) for _k in [_val_t, _val_f])


def test_telescope_152():
    _val_t = _tel.moon_phase_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_phase_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_153():
    _val_t = _tel.moon_phase_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_phase_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-math.pi <= _k <= math.pi for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


# +
# Telescope().moon_ra(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_160():
    assert all(_tel.moon_ra(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_161():
    _val_t = _tel.moon_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_162():
    _val_t = _tel.moon_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_radec(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_170():
    assert all(_tel.moon_radec(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_171():
    _val_t = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_172():
    _val_t = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.ra.value, _val_t.dec.value, _val_t.distance.value,
                _val_f.ra.value, _val_f.dec.value, _val_f.distance.value])


def test_telescope_173():
    _val_t = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.dec.value, _val_f.dec.value])


def test_telescope_174():
    _val_t = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.ra.value, _val_f.ra.value])


def test_telescope_175():
    _val_t = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.moon_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().moon_radec_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_180():
    assert all(_tel.moon_radec_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_181():
    _val_t = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_182():
    _val_t = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in
               [_val_t[TEST_NUM].ra.value, _val_t[TEST_NUM].dec.value, _val_t[TEST_NUM].distance.value,
                _val_f[TEST_NUM].ra.value, _val_f[TEST_NUM].dec.value, _val_f[TEST_NUM].distance.value])


def test_telescope_183():
    _val_t = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[TEST_NUM].dec.value, _val_f[TEST_NUM].dec.value])


def test_telescope_184():
    _val_t = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[TEST_NUM].ra.value, _val_f[TEST_NUM].ra.value])


def test_telescope_185():
    _val_t = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.moon_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(_k > 0.0 for _k in [_val_t[TEST_NUM].distance.value, _val_f[TEST_NUM].distance.value])


# +
# Telescope().moon_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_190():
    assert all(_tel.moon_rise(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_191():
    _val_t = _tel.moon_rise(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.moon_rise(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_192():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.moon_rise(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.moon_rise(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().moon_separation(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_200():
    assert all(_tel.moon_separation(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_201():
    assert all(_tel.moon_separation(obs_name=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_202():
    assert all(_tel.moon_separation(obs_coords=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_203():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_204():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_205():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_206():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.moon_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_separation_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS)
# -
def test_telescope_210():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_separation_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_211():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_separation_ndays(obs_name=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_212():
    assert all(_tel.moon_separation_ndays(obs_coords=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_213():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.moon_separation_ndays(obs_name=_t1, ndays=TEST_NDAYS)
    assert isinstance(_val[TEST_NUM], float)


def test_telescope_214():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.moon_separation_ndays(obs_name=_t1, ndays=TEST_NDAYS)
    assert (-360.0 <= _val[TEST_NUM] <= 360.0)


def test_telescope_215():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_ndays(obs_coords=_coords, ndays=TEST_NDAYS)
    assert isinstance(_val[TEST_NUM], float)


def test_telescope_216():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_ndays(obs_coords=_coords, ndays=TEST_NDAYS)
    assert (-360.0 <= _val[TEST_NUM] <= 360.0)


# +
# Telescope().moon_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_220():
    assert all(_tel.moon_set(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_221():
    _val_t = _tel.moon_set(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.moon_set(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_222():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.moon_set(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.moon_set(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().moon_steward(self, obs_time=get_isot(0, True))
# -
def test_telescope_230():
    assert all(_tel.moon_steward(obs_time=_k)[0] is None for _k in TEST_INVALID_INPUTS)


def test_telescope_231():
    assert isinstance(_tel.moon_steward(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))[0], float)


def test_telescope_232():
    assert isinstance(_tel.moon_steward(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))[1], str)


def test_telescope_233():
    assert -30.0 <= _tel.moon_steward(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))[0] <= 30.0


def test_telescope_234():
    assert _tel.moon_steward(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))[1] in AST__MOON__STEWARD


# +
# Telescope().moon_radec() vs. Telescope().moon_altaz()
# -
def test_telescope_240():
    _moon_radec = _tel.moon_radec()
    _coords = f"{ra_from_decimal(_moon_radec.ra.value)} {dec_from_decimal(_moon_radec.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value
    _moon_altaz = _tel.moon_altaz()
    _alt_2, _az_2 = _moon_altaz.alt.value, _moon_altaz.az.value
    assert math.isclose(_alt_1, _alt_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_241():
    _moon_radec = _tel.moon_radec()
    _coords = f"{ra_from_decimal(_moon_radec.ra.value)} {dec_from_decimal(_moon_radec.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value
    _moon_altaz = _tel.moon_altaz()
    _alt_2, _az_2 = _moon_altaz.alt.value, _moon_altaz.az.value
    assert math.isclose(_az_1, _az_2, rel_tol=TEST_TOLERANCE['3dp'])


# +
# Telescope().fm_lunation(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_250():
    assert all(_tel.fm_lunation(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_251():
    _val_t = _tel.fm_lunation(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.fm_lunation(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_252():
    _val_t = _tel.fm_lunation(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.fm_lunation(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(0.0 <= _k <= 30.0 for _k in [_val_t, _val_f])


# +
# Telescope().fm_moon_date(obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__MOON__WHICH[0], utc_offset=0.0)
# -
def test_telescope_260():
    assert all(_tel.fm_moon_date(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_261():
    _val_t = _tel.fm_moon_date(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), utc_offset=_tel.utc_offset)
    _val_f = _tel.fm_moon_date(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), utc_offset=_tel.utc_offset)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_262():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.fm_moon_date(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), which=_which, utc_offset=_tel.utc_offset)
    _val_f = _tel.fm_moon_date(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), which=_which, utc_offset=_tel.utc_offset)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_263():
    _phase = random.choice(AST__MOON__WHICH)
    _val_t = _tel.fm_moon_date(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), phase=_phase, utc_offset=_tel.utc_offset)
    _val_f = _tel.fm_moon_date(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), phase=_phase, utc_offset=_tel.utc_offset)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])
