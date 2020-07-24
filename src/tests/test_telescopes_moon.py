#!/usr/bin/env python3


# +
# import(s)
# -
from src.telescopes.factory import *

import astropy


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_telescopes_moon.py
"""


# +
# constant(s)
# -
INVALID_INPUTS = [None, get_hash(), {}, [], ()]
LOWER_BOUND = random.randint(-1000, 0)
UPPER_BOUND = random.randint(0, 1000)


# +
# variable(s)
# -
_tel = Telescope(random.choice(TEL__TELESCOPES))


# +
# Telescope().moon_altaz(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_0():
    assert all(_tel.moon_altaz(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_1():
    _val_t = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_2():
    _val_t = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.alt.value, _val_t.az.value, _val_t.distance.value,
                _val_f.alt.value, _val_f.az.value, _val_f.distance.value])


def test_telescope_3():
    _val_t = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.alt.value, _val_f.alt.value])


def test_telescope_4():
    _val_t = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.az.value, _val_f.az.value])


def test_telescope_5():
    _val_t = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().moon_altaz_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_10():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_altaz_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_11():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_12():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(isinstance(_k, float) for _k in
               [_val_t[_num].alt.value, _val_t[_num].az.value, _val_t[_num].distance.value,
                _val_f[_num].alt.value, _val_f[_num].az.value, _val_f[_num].distance.value])


def test_telescope_13():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[_num].alt.value, _val_f[_num].alt.value])


def test_telescope_14():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[_num].az.value, _val_f[_num].az.value])


def test_telescope_15():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(_k > 0.0 for _k in [_val_t[_num].distance.value, _val_f[_num].distance.value])


# +
# Telescope().moon_altaz_now(self)
# -
def test_telescope_20():
    _val = _tel.moon_altaz_now()
    assert all(isinstance(_k, float) for _k in [_val.alt.value, _val.az.value, _val.distance.value])


def test_telescope_21():
    _val = _tel.moon_altaz_now()
    assert (-90.0 <= _val.alt.value <= 90.0)


def test_telescope_22():
    _val = _tel.moon_altaz_now()
    assert (-360.0 <= _val.az.value <= 360.0)


def test_telescope_23():
    _val = _tel.moon_altaz_now()
    assert (_val.distance.value > 0.0)


# +
# Telescope().moon_altaz_today(self)
# -
def test_telescope_30():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_altaz_today()
    # noinspection PyUnresolvedReferences
    assert isinstance(_val[_num], astropy.coordinates.sky_coordinate.SkyCoord)


def test_telescope_31():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_altaz_today()
    assert all(isinstance(_k, float) for _k in [_val[_num].alt.value, _val[_num].az.value, _val[_num].distance.value])


def test_telescope_32():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_altaz_today()
    assert (-90.0 <= _val[_num].alt.value <= 90.0)


def test_telescope_33():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_altaz_today()
    assert (-360.0 <= _val[_num].az.value <= 360.0)


def test_telescope_34():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_altaz_today()
    assert (_val[_num].distance.value > 0.0)


# +
# Telescope().moon_alt(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_40():
    assert all(_tel.moon_alt(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_41():
    _val_t = _tel.moon_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_42():
    _val_t = _tel.moon_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_az(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_50():
    assert all(_tel.moon_az(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_51():
    _val_t = _tel.moon_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_52():
    _val_t = _tel.moon_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_civil(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_60():
    assert all(_tel.moon_civil(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_61():
    _val_t = _tel.moon_civil(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_civil(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k in list(AST__MOON__CIVIL.values()) for _k in [_val_t, _val_f])


def test_telescope_62():
    assert all([_tel.moon_civil('2020-06-05T12:00:00.000000') == 'full',
                _tel.moon_civil('2020-06-12T12:00:00.000000') == 'last quarter',
                _tel.moon_civil('2020-06-20T12:00:00.000000') == 'new',
                _tel.moon_civil('2020-06-28T12:00:00.000000') == 'first quarter',
                _tel.moon_civil('2020-07-04T12:00:00.000000') == 'full'])


# +
# Telescope().moon_date(self, obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__MOON__WHICH[0], utc=False)
# -
def test_telescope_70():
    assert all(_tel.moon_date(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_71():
    _val_t = _tel.moon_date(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_date(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_72():
    _which = random.choice(AST__WHICH)
    _val_t = _tel.moon_date(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), which=_which)
    _val_f = _tel.moon_date(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), which=_which)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


def test_telescope_73():
    _phase = random.choice(AST__MOON__WHICH)
    _val_t = _tel.moon_date(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), phase=_phase)
    _val_f = _tel.moon_date(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), phase=_phase)
    assert all(re.match(OBS_ISO_PATTERN, _k) for _k in [_val_t, _val_f])


# +
# Telescope().moon_distance(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_80():
    assert all(_tel.moon_distance(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_81():
    _val_t = _tel.moon_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_82():
    _val_t = _tel.moon_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_exclusion(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_90():
    assert all(_tel.moon_exclusion(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_91():
    _val_t = _tel.moon_exclusion(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_exclusion(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_92():
    _min = _tel.min_moonex
    _max = _tel.max_moonex + _tel.min_moonex
    _val_t = _tel.moon_exclusion(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_exclusion(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_min <= _k <= _max for _k in [_val_t, _val_f])


# +
# Telescope().moon_exclusion_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_100():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_exclusion_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_101():
    _ndays = random.randint(1, 5)
    _val_t = _tel.moon_exclusion_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_exclusion_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, np.ndarray) for _k in [_val_t, _val_f])


def test_telescope_102():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_exclusion_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_exclusion_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(isinstance(_k, float) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_103():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _min = _tel.min_moonex
    _max = _tel.max_moonex + _tel.min_moonex
    _val_t = _tel.moon_exclusion_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_exclusion_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(_min <= _k <= _max for _k in [_val_t[_num], _val_f[_num]])


# +
# Telescope().moon_exclusion_now(self)
# -
def test_telescope_110():
    assert isinstance(_tel.moon_exclusion_now(), float)


def test_telescope_111():
    _min = _tel.min_moonex
    _max = _tel.max_moonex + _tel.min_moonex
    assert (_min <= _tel.moon_exclusion_now() <= _max)


# +
# Telescope().moon_exclusion_today(self)
# -
def test_telescope_120():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_exclusion_today()
    assert isinstance(_val[_num], float)


def test_telescope_121():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _min = _tel.min_moonex
    _max = _tel.max_moonex + _tel.min_moonex
    _val = _tel.moon_exclusion_today()
    assert (_min <= _val[_num] <= _max)


# +
# Telescope().moon_illumination(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_130():
    assert all(_tel.moon_illumination(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_131():
    _val_t = _tel.moon_illumination(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_illumination(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_132():
    _val_t = _tel.moon_illumination(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_illumination(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(0.0 <= _k <= 1.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_illumination_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
# 140
def test_telescope_140():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_illumination_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_141():
    _ndays = random.randint(1, 5)
    _val_t = _tel.moon_illumination_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_illumination_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, np.ndarray) for _k in [_val_t, _val_f])


def test_telescope_142():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_illumination_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_illumination_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(isinstance(_k, float) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_143():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_illumination_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_illumination_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(0.0 <= _k <= 1.0 for _k in [_val_t[_num], _val_f[_num]])


# +
# Telescope().moon_illumination_now(self)
# -
def test_telescope_150():
    assert isinstance(_tel.moon_illumination_now(), float)


def test_telescope_151():
    assert (0.0 <= _tel.moon_illumination_now() <= 1.0)


# +
# Telescope().moon_illumination_today(self)
# -
def test_telescope_160():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_illumination_today()
    assert isinstance(_val[_num], float)


def test_telescope_161():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_illumination_today()[_num]
    assert (0.0 <= _val <= 1.0)


# +
# Telescope().moon_is_up(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg)
# -
def test_telescope_170():
    assert all(_tel.moon_is_up(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_171():
    assert all(_tel.moon_is_up(horizon=_k) is None for _k in INVALID_INPUTS)


def test_telescope_172():
    assert _tel.moon_is_up(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)) in [True, False, None]


def test_telescope_173():
    assert _tel.moon_is_up(obs_time=get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)) in [True, False, None]


# +
# Telescope().moon_is_down(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg)
# -
def test_telescope_180():
    assert all(_tel.moon_is_down(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_181():
    assert all(_tel.moon_is_down(horizon=_k) is None for _k in INVALID_INPUTS)


def test_telescope_182():
    assert _tel.moon_is_down(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True)) in [True, False, None]


def test_telescope_183():
    assert _tel.moon_is_down(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False)) in [True, False, None]


# +
# Telescope().moon_phase(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_190():
    assert all(_tel.moon_phase(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_191():
    _val_t = _tel.moon_phase(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_phase(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_192():
    _val_t = _tel.moon_phase(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_phase(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-math.pi <= _k <= math.pi for _k in [_val_t, _val_f])


# +
# Telescope().moon_phase_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_200():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_phase_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_201():
    _ndays = random.randint(1, 5)
    _val_t = _tel.moon_phase_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_phase_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(isinstance(_k, np.ndarray) for _k in [_val_t, _val_f])


def test_telescope_202():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_phase_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_phase_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(isinstance(_k, float) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_203():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_phase_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_phase_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(-math.pi <= _k <= math.pi for _k in [_val_t[_num], _val_f[_num]])


# +
# Telescope().moon_phase_now(self)
# -
def test_telescope_210():
    assert isinstance(_tel.moon_phase_now(), float)


def test_telescope_211():
    assert (-math.pi <= _tel.moon_phase_now() <= math.pi)


# +
# Telescope().moon_phase_today(self)
# -
def test_telescope_220():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_phase_today()
    assert isinstance(_val[_num], float)


def test_telescope_221():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_phase_today()
    assert (-math.pi <= _val[_num] <= math.pi)


# +
# Telescope().moon_radec(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_230():
    assert all(_tel.moon_radec(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_231():
    _val_t = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_232():
    _val_t = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.ra.value, _val_t.dec.value, _val_t.distance.value,
                _val_f.ra.value, _val_f.dec.value, _val_f.distance.value])


def test_telescope_233():
    _val_t = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.dec.value, _val_f.dec.value])


def test_telescope_234():
    _val_t = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.ra.value, _val_f.ra.value])


def test_telescope_235():
    _val_t = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.moon_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().moon_radec_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_240():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_radec_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_241():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_242():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(isinstance(_k, float) for _k in
               [_val_t[_num].ra.value, _val_t[_num].dec.value, _val_t[_num].distance.value,
                _val_f[_num].ra.value, _val_f[_num].dec.value, _val_f[_num].distance.value])


def test_telescope_243():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[_num].dec.value, _val_f[_num].dec.value])


def test_telescope_244():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[_num].ra.value, _val_f[_num].ra.value])


def test_telescope_245():
    _ndays = random.randint(1, 5)
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val_t = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.moon_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    assert all(_k > 0.0 for _k in [_val_t[_num].distance.value, _val_f[_num].distance.value])


# +
# Telescope().moon_radec_now(self)
# -
def test_telescope_250():
    _val = _tel.moon_radec_now()
    assert all(isinstance(_k, float) for _k in [_val.ra.value, _val.dec.value, _val.distance.value])


def test_telescope_251():
    _val = _tel.moon_radec_now()
    assert (-90.0 <= _val.dec.value <= 90.0)


def test_telescope_252():
    _val = _tel.moon_radec_now()
    assert (-360.0 <= _val.ra.value <= 360.0)


def test_telescope_253():
    _val = _tel.moon_radec_now()
    assert (_val.distance.value > 0.0)


# +
# Telescope().moon_radec_today(self)
# -
def test_telescope_260():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_radec_today()[_num]
    # noinspection PyUnresolvedReferences
    assert isinstance(_val, astropy.coordinates.sky_coordinate.SkyCoord)


def test_telescope_261():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_radec_today()
    assert all(isinstance(_k, float) for _k in [_val[_num].ra.value, _val[_num].dec.value, _val[_num].distance.value])


def test_telescope_262():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_radec_today()
    assert (-90.0 <= _val[_num].dec.value <= 90.0)


def test_telescope_263():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_radec_today()
    assert (-360.0 <= _val[_num].ra.value <= 360.0)


def test_telescope_264():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_radec_today()
    assert (_val[_num].distance.value > 0.0)


# +
# Telescope().moon_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_270():
    assert all(_tel.moon_rise(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_271():
    _val_t = _tel.moon_rise(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.moon_rise(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_272():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.moon_rise(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.moon_rise(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().moon_separation(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_280():
    assert all(_tel.moon_separation(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_281():
    assert all(_tel.moon_separation(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_282():
    assert all(_tel.moon_separation(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_283():
    _val_t = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name='M51')
    _val_f = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name='M51')
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_284():
    _val_t = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name='M51')
    _val_f = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name='M51')
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_285():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_286():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.moon_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().moon_separation_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS)
# -
def test_telescope_290():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_separation_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_291():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_separation_ndays(obs_name=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_292():
    _ndays = random.randint(1, 5)
    assert all(_tel.moon_separation_ndays(obs_coords=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_293():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _val = _tel.moon_separation_ndays(obs_name='M51', ndays=_ndays)
    assert isinstance(_val[_num], float)


def test_telescope_294():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _val = _tel.moon_separation_ndays(obs_name='M51', ndays=_ndays)
    assert (-360.0 <= _val[_num] <= 360.0)


def test_telescope_295():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_ndays(obs_coords=_coords, ndays=_ndays)
    assert isinstance(_val[_num], float)


def test_telescope_296():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_ndays(obs_coords=_coords, ndays=_ndays)
    assert (-360.0 <= _val[_num] <= 360.0)


# +
# Telescope().moon_separation_now(self, obs_name='', obs_coords='')
# -
def test_telescope_300():
    assert all(_tel.moon_separation_now(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_301():
    assert all(_tel.moon_separation_now(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_302():
    _val_t = _tel.moon_separation_now(obs_name='M51')
    _val_f = _tel.moon_separation_now(obs_name='M51')
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_303():
    _val_t = _tel.moon_separation_now(obs_name='M51')
    _val_f = _tel.moon_separation_now(obs_name='M51')
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_304():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.moon_separation_now(obs_coords=_coords)
    _val_f = _tel.moon_separation_now(obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_305():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_now(obs_coords=_coords)
    assert (-360.0 <= _val <= 360.0)


# +
# Telescope().moon_separation_today(self, obs_name='', obs_coords='')
# -
def test_telescope_310():
    assert all(_tel.moon_separation_today(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_311():
    assert all(_tel.moon_separation_today(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_312():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_separation_today(obs_name='M51')
    assert isinstance(_val[_num], float)


def test_telescope_313():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.moon_separation_today(obs_name='M51')
    assert (-360.0 <= _val[_num] <= 360.0)


def test_telescope_314():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_today(obs_coords=_coords)
    assert isinstance(_val[_num], float)


def test_telescope_315():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.moon_separation_today(obs_coords=_coords)
    assert (-360.0 <= _val[_num] <= 360.0)


# +
# Telescope().moon_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_320():
    assert all(_tel.moon_set(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_321():
    _val_t = _tel.moon_set(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.moon_set(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_322():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.moon_set(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.moon_set(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().moon_steward(self, obs_time=get_isot(0, True))
# -
def test_telescope_330():
    assert all(_tel.moon_steward(obs_time=_k)[0] is None for _k in INVALID_INPUTS)


def test_telescope_331():
    assert isinstance(_tel.moon_steward(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))[0], float)


def test_telescope_332():
    assert isinstance(_tel.moon_steward(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))[1], str)


def test_telescope_333():
    assert -30.0 <= _tel.moon_steward(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))[0] <= 30.0


def test_telescope_334():
    assert _tel.moon_steward(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))[1] in AST__MOON__STEWARD


# +
# Telescope().moon_radec() vs. Telescope().moon_altaz()
# -
def test_telescope_340():

    _moon_radec = _tel.moon_radec()
    _coords = f"{ra_from_decimal(_moon_radec.ra.value)} {dec_from_decimal(_moon_radec.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value

    _moon_altaz = _tel.moon_altaz()
    _alt_2, _az_2 = _moon_altaz.alt.value, _moon_altaz.az.value

    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)


# +
# Telescope().moon_radec_now() vs. Telescope().moon_altaz_now()
# -
def test_telescope_350():
    _moon_radec_now = _tel.moon_radec_now()
    _coords = f"{ra_from_decimal(_moon_radec_now.ra.value)} {dec_from_decimal(_moon_radec_now.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value

    _moon_altaz_now = _tel.moon_altaz_now()
    _alt_2, _az_2 = _moon_altaz_now.alt.value, _moon_altaz_now.az.value

    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)
