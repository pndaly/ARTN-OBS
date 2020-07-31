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
  % python3.7 -m pytest -p no:warnings test_telescopes_sun.py
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
# Telescope().sun_altaz(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_0():
    assert all(_tel.sun_altaz(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_1():
    _val_t = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_2():
    _val_t = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.alt.value, _val_t.az.value, _val_t.distance.value,
                _val_f.alt.value, _val_f.az.value, _val_f.distance.value])


def test_telescope_3():
    _val_t = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.alt.value, _val_f.alt.value])


def test_telescope_4():
    _val_t = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.az.value, _val_f.az.value])


def test_telescope_5():
    _val_t = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().sun_altaz_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_10():
    _ndays = random.randint(1, 5)
    assert all(_tel.sun_altaz_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_11():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_12():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(isinstance(_k, float) for _k in
               [_val_t[_num].alt.value, _val_t[_num].az.value, _val_t[_num].distance.value,
                _val_f[_num].alt.value, _val_f[_num].az.value, _val_f[_num].distance.value])


def test_telescope_13():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[_num].alt.value, _val_f[_num].alt.value])


def test_telescope_14():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[_num].az.value, _val_f[_num].az.value])


def test_telescope_15():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_altaz_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(_k > 0.0 for _k in [_val_t[_num].distance.value, _val_f[_num].distance.value])


# +
# Telescope().sun_altaz_now(self)
# -
def test_telescope_20():
    _val = _tel.sun_altaz_now()
    assert all(isinstance(_k, float) for _k in [_val.alt.value, _val.az.value, _val.distance.value])


def test_telescope_21():
    _val = _tel.sun_altaz_now()
    assert (-90.0 <= _val.alt.value <= 90.0)


def test_telescope_22():
    _val = _tel.sun_altaz_now()
    assert (-360.0 <= _val.az.value <= 360.0)


def test_telescope_23():
    _val = _tel.sun_altaz_now()
    assert (_val.distance.value > 0.0)


# +
# Telescope().sun_altaz_today(self)
# -
def test_telescope_30():
    _num = random.randint(1, AST__5__MINUTES - 1)
    # noinspection PyUnresolvedReferences
    assert isinstance(_tel.sun_altaz_today()[_num], astropy.coordinates.sky_coordinate.SkyCoord)


def test_telescope_31():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_altaz_today()[_num]
    assert all(isinstance(_k, float) for _k in [_val.alt.value, _val.az.value, _val.distance.value])


def test_telescope_32():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_altaz_today()[_num]
    assert (-90.0 <= _val.alt.value <= 90.0)


def test_telescope_33():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_altaz_today()[_num]
    assert (-360.0 <= _val.az.value <= 360.0)


def test_telescope_34():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_altaz_today()[_num]
    assert (_val.distance.value > 0.0)


# +
# Telescope().sun_alt(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_40():
    assert all(_tel.sun_alt(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_41():
    _val_t = _tel.sun_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_42():
    _val_t = _tel.sun_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_alt(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_az(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_50():
    assert all(_tel.sun_az(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_51():
    _val_t = _tel.sun_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_52():
    _val_t = _tel.sun_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_az(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_distance(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_60():
    assert all(_tel.sun_distance(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_61():
    _val_t = _tel.sun_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_62():
    _val_t = _tel.sun_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_distance(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_radec(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_70():
    assert all(_tel.sun_radec(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_71():
    _val_t = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_72():
    _val_t = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.ra.value, _val_t.dec.value, _val_t.distance.value,
                _val_f.ra.value, _val_f.dec.value, _val_f.distance.value])


def test_telescope_73():
    _val_t = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.dec.value, _val_f.dec.value])


def test_telescope_74():
    _val_t = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.ra.value, _val_f.ra.value])


def test_telescope_75():
    _val_t = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True))
    _val_f = _tel.sun_radec(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().sun_radec_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_80():
    _ndays = random.randint(1, 5)
    assert all(_tel.sun_radec_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_81():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t[_num], _val_f[_num]])


def test_telescope_82():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(isinstance(_k, float) for _k in
               [_val_t[_num].ra.value, _val_t[_num].dec.value, _val_t[_num].distance.value,
                _val_f[_num].ra.value, _val_f[_num].dec.value, _val_f[_num].distance.value])


def test_telescope_83():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[_num].dec.value, _val_f[_num].dec.value])


def test_telescope_84():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[_num].ra.value, _val_f[_num].ra.value])


def test_telescope_85():
    _ndays = random.randint(1, 5)
    _val_t = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), ndays=_ndays)
    _val_f = _tel.sun_radec_ndays(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), ndays=_ndays)
    _num = random.randint(1, AST__5__MINUTES - 1)
    assert all(_k > 0.0 for _k in [_val_t[_num].distance.value, _val_f[_num].distance.value])


# +
# Telescope().sun_radec_now(self)
# -
def test_telescope_90():
    _val = _tel.sun_radec_now()
    assert all(isinstance(_k, float) for _k in [_val.ra.value, _val.dec.value, _val.distance.value])


def test_telescope_91():
    _val = _tel.sun_radec_now()
    assert (-90.0 <= _val.dec.value <= 90.0)


def test_telescope_92():
    _val = _tel.sun_radec_now()
    assert (-360.0 <= _val.ra.value <= 360.0)


def test_telescope_93():
    _val = _tel.sun_radec_now()
    assert (_val.distance.value > 0.0)


# +
# Telescope().sun_radec_today(self)
# -
def test_telescope_100():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_radec_today()[_num]
    # noinspection PyUnresolvedReferences
    assert isinstance(_val, astropy.coordinates.sky_coordinate.SkyCoord)


def test_telescope_101():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_radec_today()[_num]
    assert all(isinstance(_k, float) for _k in [_val.ra.value, _val.dec.value, _val.distance.value])


def test_telescope_102():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_radec_today()[_num]
    assert (-90.0 <= _val.dec.value <= 90.0)


def test_telescope_103():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_radec_today()[_num]
    assert (-360.0 <= _val.ra.value <= 360.0)


def test_telescope_104():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _val = _tel.sun_radec_today()[_num]
    assert (_val.distance.value > 0.0)


# +
# Telescope().sun_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_110():
    assert all(_tel.sun_rise(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_111():
    _val_t = _tel.sun_rise(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.sun_rise(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_112():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.sun_rise(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.sun_rise(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().sun_separation(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_120():
    assert all(_tel.sun_separation(obs_time=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_121():
    assert all(_tel.sun_separation(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_122():
    assert all(_tel.sun_separation(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_123():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_124():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_125():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_126():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.sun_separation(get_isot(random.randint(LOWER_BOUND, UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_separation_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS)
# -
def test_telescope_130():
    _ndays = random.randint(1, 5)
    assert all(_tel.sun_separation_ndays(obs_time=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_131():
    _ndays = random.randint(1, 5)
    assert all(_tel.sun_separation_ndays(obs_name=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_132():
    _ndays = random.randint(1, 5)
    assert all(_tel.sun_separation_ndays(obs_coords=_k, ndays=_ndays) is None for _k in INVALID_INPUTS)


def test_telescope_133():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.sun_separation_ndays(obs_name=_t1, ndays=_ndays)[_num]
    assert isinstance(_val, float)


def test_telescope_134():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.sun_separation_ndays(obs_name=_t1, ndays=_ndays)[_num]
    assert (-360.0 <= _val <= 360.0)


def test_telescope_135():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_ndays(obs_coords=_coords, ndays=_ndays)
    assert isinstance(_val[_num], float)


def test_telescope_136():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ndays = random.randint(1, 5)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_ndays(obs_coords=_coords, ndays=_ndays)
    assert (-360.0 <= _val[_num] <= 360.0)


# +
# Telescope().sun_separation_now(self, obs_name='', obs_coords='')
# -
def test_telescope_140():
    assert all(_tel.sun_separation_now(obs_name=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_141():
    assert all(_tel.sun_separation_now(obs_coords=_k) is math.nan for _k in INVALID_INPUTS)


def test_telescope_142():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.sun_separation_now(obs_name=_t1)
    _val_f = _tel.sun_separation_now(obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_143():
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.sun_separation_now(obs_name=_t1)
    _val_f = _tel.sun_separation_now(obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_144():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.sun_separation_now(obs_coords=_coords)
    _val_f = _tel.sun_separation_now(obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_145():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_now(obs_coords=_coords)
    assert (-360.0 <= _val <= 360.0)


# +
# Telescope().sun_separation_today(self, obs_name='', obs_coords='')
# -
def test_telescope_150():
    assert all(_tel.sun_separation_today(obs_name=_k) is None for _k in INVALID_INPUTS)


def test_telescope_151():
    assert all(_tel.sun_separation_today(obs_coords=_k) is None for _k in INVALID_INPUTS)


def test_telescope_152():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.sun_separation_today(obs_name=_t1)
    assert isinstance(_val[_num], float)


def test_telescope_153():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _t1 = ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.sun_separation_today(obs_name=_t1)
    assert (-360.0 <= _val[_num] <= 360.0)


def test_telescope_154():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_today(obs_coords=_coords)
    assert isinstance(_val[_num], float)


def test_telescope_155():
    _num = random.randint(1, AST__5__MINUTES - 1)
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_today(obs_coords=_coords)
    assert (-360.0 <= _val[_num] <= 360.0)


# +
# Telescope().sun_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_160():
    assert all(_tel.sun_set(obs_time=_k) is None for _k in INVALID_INPUTS)


def test_telescope_161():
    _val_t = _tel.sun_set(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.sun_set(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_162():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.sun_set(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.sun_set(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=0.0001)


# +
# Telescope().sun_radec() vs. Telescope().sun_altaz()
# -
def test_telescope_170():

    _sun_radec = _tel.sun_radec()
    _coords = f"{ra_from_decimal(_sun_radec.ra.value)} {dec_from_decimal(_sun_radec.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value

    _sun_altaz = _tel.sun_altaz()
    _alt_2, _az_2 = _sun_altaz.alt.value, _sun_altaz.az.value

    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)


# +
# Telescope().sun_radec_now() vs. Telescope().sun_altaz_now()
# -
def test_telescope_171():
    _sun_radec_now = _tel.sun_radec_now()
    _coords = f"{ra_from_decimal(_sun_radec_now.ra.value)} {dec_from_decimal(_sun_radec_now.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value

    _sun_altaz_now = _tel.sun_altaz_now()
    _alt_2, _az_2 = _sun_altaz_now.alt.value, _sun_altaz_now.az.value

    assert math.isclose(_alt_1, _alt_2, rel_tol=0.1) and math.isclose(_az_1, _az_2, rel_tol=0.1)
