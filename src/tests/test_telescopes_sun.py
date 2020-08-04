#!/usr/bin/env python3


# +
# import(s)
# -
from src.tests import *
from src.telescopes.factory import *

import astropy


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_telescopes_sun.py
"""


# +
# variable(s)
# -
_tel = Telescope(random.choice(TEL__TELESCOPES))


# +
# Telescope().sun_alt(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_0():
    assert all(_tel.sun_alt(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_1():
    _val_t = _tel.sun_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_2():
    _val_t = _tel.sun_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_alt(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_altaz(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_10():
    assert all(_tel.sun_altaz(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_11():
    _val_t = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_12():
    _val_t = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.alt.value, _val_t.az.value, _val_t.distance.value,
                _val_f.alt.value, _val_f.az.value, _val_f.distance.value])


def test_telescope_13():
    _val_t = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.alt.value, _val_f.alt.value])


def test_telescope_14():
    _val_t = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.az.value, _val_f.az.value])


def test_telescope_15():
    _val_t = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_altaz(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().sun_altaz_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_20():
    assert all(_tel.sun_altaz_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_21():
    _val_t = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in
               [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_22():
    _val_t = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in
               [_val_t[TEST_NUM].alt.value, _val_t[TEST_NUM].az.value, _val_t[TEST_NUM].distance.value,
                _val_f[TEST_NUM].alt.value, _val_f[TEST_NUM].az.value, _val_f[TEST_NUM].distance.value])


def test_telescope_23():
    _val_t = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[TEST_NUM].alt.value, _val_f[TEST_NUM].alt.value])


def test_telescope_24():
    _val_t = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[TEST_NUM].az.value, _val_f[TEST_NUM].az.value])


def test_telescope_25():
    _val_t = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_altaz_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(_k > 0.0 for _k in [_val_t[TEST_NUM].distance.value, _val_f[TEST_NUM].distance.value])


def test_telescope_26():
    _val_1 = _tel.sun_altaz_ndays().alt[0].value
    _val_2 = _tel.sun_alt()
    assert math.isclose(_val_1, _val_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_27():
    _val_1 = _tel.sun_altaz_ndays().az[0].value
    _val_2 = _tel.sun_az()
    assert math.isclose(_val_1, _val_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_28():
    _val_1 = _tel.sun_altaz_ndays().distance[0].value
    _val_2 = _tel.sun_distance()
    assert math.isclose(_val_1, _val_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_29():
    _iso_t = f"{get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True).split('T')[0]}T00:00:00.000000"
    _iso_f = f"{get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False).split('T')[0]}T00:00:00.000000"
    _val_t = _tel.sun_altaz_ndays(obs_time=_iso_t, ndays=TEST_NDAYS)
    _val_f = _tel.sun_altaz_ndays(obs_time=_iso_f, ndays=TEST_NDAYS)
    assert all(len(_k) == AST__5__MINUTES*TEST_NDAYS for _k in [_val_t.alt, _val_t.az, _val_f.alt, _val_f.az])


# +
# Telescope().sun_az(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_30():
    assert all(_tel.sun_az(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_31():
    _val_t = _tel.sun_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_32():
    _val_t = _tel.sun_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_az(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_dec(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_40():
    assert all(_tel.sun_dec(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_41():
    _val_t = _tel.sun_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_42():
    _val_t = _tel.sun_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_dec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_distance(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_50():
    assert all(_tel.sun_distance(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_51():
    _val_t = _tel.sun_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_52():
    _val_t = _tel.sun_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_distance(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_ra(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_60():
    assert all(_tel.sun_ra(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_61():
    _val_t = _tel.sun_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_62():
    _val_t = _tel.sun_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_ra(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_radec(self, obs_time=Time(get_isot(0, True)))
# -
def test_telescope_70():
    assert all(_tel.sun_radec(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_71():
    _val_t = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in [_val_t, _val_f])


def test_telescope_72():
    _val_t = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(isinstance(_k, float) for _k in
               [_val_t.ra.value, _val_t.dec.value, _val_t.distance.value,
                _val_f.ra.value, _val_f.dec.value, _val_f.distance.value])


def test_telescope_73():
    _val_t = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t.dec.value, _val_f.dec.value])


def test_telescope_74():
    _val_t = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t.ra.value, _val_f.ra.value])


def test_telescope_75():
    _val_t = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True))
    _val_f = _tel.sun_radec(obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False))
    assert all(_k > 0.0 for _k in [_val_t.distance.value, _val_f.distance.value])


# +
# Telescope().sun_radec_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS)
# -
def test_telescope_80():
    assert all(_tel.sun_radec_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_81():
    _val_t = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    # noinspection PyUnresolvedReferences
    assert all(isinstance(_k, astropy.coordinates.sky_coordinate.SkyCoord) for _k in
               [_val_t[TEST_NUM], _val_f[TEST_NUM]])


def test_telescope_82():
    _val_t = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(isinstance(_k, float) for _k in
               [_val_t[TEST_NUM].ra.value, _val_t[TEST_NUM].dec.value, _val_t[TEST_NUM].distance.value,
                _val_f[TEST_NUM].ra.value, _val_f[TEST_NUM].dec.value, _val_f[TEST_NUM].distance.value])


def test_telescope_83():
    _val_t = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-90.0 <= _k <= 90.0 for _k in [_val_t[TEST_NUM].dec.value, _val_f[TEST_NUM].dec.value])


def test_telescope_84():
    _val_t = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t[TEST_NUM].ra.value, _val_f[TEST_NUM].ra.value])


def test_telescope_85():
    _val_t = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), ndays=TEST_NDAYS)
    _val_f = _tel.sun_radec_ndays(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), ndays=TEST_NDAYS)
    assert all(_k > 0.0 for _k in [_val_t[TEST_NUM].distance.value, _val_f[TEST_NUM].distance.value])


def test_telescope_86():
    _val_1 = _tel.sun_radec_ndays().ra[0].value
    _val_2 = _tel.sun_ra()
    assert math.isclose(_val_1, _val_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_87():
    _val_1 = _tel.sun_radec_ndays().dec[0].value
    _val_2 = _tel.sun_dec()
    assert math.isclose(_val_1, _val_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_88():
    _iso_t = f"{get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True).split('T')[0]}T00:00:00.000000"
    _iso_f = f"{get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False).split('T')[0]}T00:00:00.000000"
    _val_t = _tel.sun_radec_ndays(obs_time=_iso_t, ndays=TEST_NDAYS)
    _val_f = _tel.sun_radec_ndays(obs_time=_iso_f, ndays=TEST_NDAYS)
    assert all(len(_k) == AST__5__MINUTES*TEST_NDAYS for _k in [_val_t.ra, _val_t.dec, _val_f.ra, _val_f.dec])


# +
# Telescope().sun_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_90():
    assert all(_tel.sun_rise(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_91():
    _val_t = _tel.sun_rise(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.sun_rise(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_92():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.sun_rise(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.sun_rise(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=TEST_TOLERANCE['3dp'])


# +
# Telescope().sun_separation(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='')
# -
def test_telescope_100():
    assert all(_tel.sun_separation(obs_time=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_101():
    assert all(_tel.sun_separation(obs_name=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_102():
    assert all(_tel.sun_separation(obs_coords=_k) is math.nan for _k in TEST_INVALID_INPUTS)


def test_telescope_103():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_104():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val_t = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1)
    _val_f = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


def test_telescope_105():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_coords=_coords)
    assert all(isinstance(_k, float) for _k in [_val_t, _val_f])


def test_telescope_106():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val_t = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords)
    _val_f = _tel.sun_separation(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_coords=_coords)
    assert all(-360.0 <= _k <= 360.0 for _k in [_val_t, _val_f])


# +
# Telescope().sun_separation_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS)
# -
def test_telescope_110():
    assert all(_tel.sun_separation_ndays(obs_time=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_111():
    assert all(_tel.sun_separation_ndays(obs_name=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_112():
    assert all(_tel.sun_separation_ndays(obs_coords=_k, ndays=TEST_NDAYS) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_113():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.sun_separation_ndays(obs_name=_t1, ndays=TEST_NDAYS)[TEST_NUM]
    assert isinstance(_val, float)


def test_telescope_114():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _val = _tel.sun_separation_ndays(obs_name=_t1, ndays=TEST_NDAYS)[TEST_NUM]
    assert (-360.0 <= _val <= 360.0)


def test_telescope_115():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_ndays(obs_coords=_coords, ndays=TEST_NDAYS)
    assert isinstance(_val[TEST_NUM], float)


def test_telescope_116():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _val = _tel.sun_separation_ndays(obs_coords=_coords, ndays=TEST_NDAYS)
    assert (-360.0 <= _val[TEST_NUM] <= 360.0)


# +
# Telescope().sun_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False)
# -
def test_telescope_120():
    assert all(_tel.sun_set(obs_time=_k) is None for _k in TEST_INVALID_INPUTS)


def test_telescope_121():
    _val_t = _tel.sun_set(which=random.choice(AST__WHICH), utc=True)
    _val_f = _tel.sun_set(which=random.choice(AST__WHICH), utc=False)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in [_val_t, _val_f])


def test_telescope_122():
    _which = random.choice(AST__WHICH)
    _val_t = isot_to_jd(_tel.sun_set(which=_which, utc=True))
    _val_f = isot_to_jd(_tel.sun_set(which=_which, utc=False))
    assert math.isclose(abs(_val_t - _val_f), abs(_tel.utc_offset/24.0), rel_tol=TEST_TOLERANCE['3dp'])


# +
# Telescope().sun_radec() vs. Telescope().sun_altaz()
# -
def test_telescope_130():
    _sun_radec = _tel.sun_radec()
    _coords = f"{ra_from_decimal(_sun_radec.ra.value)} {dec_from_decimal(_sun_radec.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value
    _sun_altaz = _tel.sun_altaz()
    _alt_2, _az_2 = _sun_altaz.alt.value, _sun_altaz.az.value
    assert math.isclose(_alt_1, _alt_2, rel_tol=TEST_TOLERANCE['3dp'])


def test_telescope_131():
    _sun_radec = _tel.sun_radec()
    _coords = f"{ra_from_decimal(_sun_radec.ra.value)} {dec_from_decimal(_sun_radec.dec.value)}"
    _radec_to_altaz = _tel.radec_to_altaz(obs_coords=_coords)
    _alt_1, _az_1 = _radec_to_altaz.alt.value, _radec_to_altaz.az.value
    _sun_altaz = _tel.sun_altaz()
    _alt_2, _az_2 = _sun_altaz.alt.value, _sun_altaz.az.value
    assert math.isclose(_az_1, _az_2, rel_tol=TEST_TOLERANCE['3dp'])
