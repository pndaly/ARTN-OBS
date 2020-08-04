#!/usr/bin/env python3


# +
# import(s)
# -
from . import *
from src.telescopes.factory import *


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_telescopes_plot.py
"""


# +
# variable(s)
# -
_tel_p = AstroPlot(random.choice(TEL__TELESCOPES))


# +
# AstroPlot().__verify_dict__()
# -
def test_telescope_0():
    assert all(not _tel_p.__verify_dict__(_k) for _k in TEST_INVALID_INPUTS)


def test_telescope_1():
    assert _tel_p.__verify_dict__(AST__PLOT__ALTAZ) is False


def test_telescope_2():
    _ndays = random.randint(1, 5)
    _t = _tel_p.moon_altaz_ndays(obs_time=Time(get_isot(0, True)), ndays=_ndays)
    _payload = {'x_axis': _t.obstime.datetime, 'y_axis': _t.alt.degree, 'z_axis': numpy.array(_t.az.degree),
                'x_min': 0.0, 'x_max': 0.0}
    _data = {**AST__PLOT__ALTAZ, **_payload}
    assert _tel_p.__verify_dict__(_data)


# +
# AstroPlot().__verify_keys__()
# -
def test_telescope_10():
    assert all(_tel_p.__verify_keys__(_k, AST__PLOT__KEYS) is False for _k in TEST_INVALID_INPUTS)


def test_telescope_11():
    assert _tel_p.__verify_keys__(AST__PLOT__ALTAZ, AST__PLOT__KEYS)


def test_telescope_12():
    _ndays = random.randint(1, 5)
    _t = _tel_p.moon_altaz_ndays(obs_time=Time(get_isot(0, True)), ndays=_ndays)
    _payload = {'x_axis': _t.obstime.datetime, 'y_axis': _t.alt.degree, 'z_axis': numpy.array(_t.az.degree)}
    _data = {**AST__PLOT__ALTAZ, **_payload}
    assert _tel_p.__verify_keys__(AST__PLOT__ALTAZ, AST__PLOT__KEYS)


# +
# AstroPlot().plot_airmass(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='',
#     ndays=AST__NDAYS, save=True, show=False)
# -
def test_telescope_20():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _data_t = _tel_p.plot_airmass(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1, save=True)
    _data_f = _tel_p.plot_airmass(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1, save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_21():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _ra_d, _dec_d = _tel_p.coords.ra.degree, _tel_p.coords.dec.degree
    _ra_s, _dec_s = ra_from_decimal(_ra_d), dec_from_decimal(_dec_d)
    _ra_l = _ra_s.replace(':', '').replace('.', '').strip()[:6]
    _dec_l = _dec_s.replace(':', '').replace('.', '').replace('-', '').replace('+', '').strip()[:6]
    _data_t = _tel_p.plot_airmass(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1, save=True)
    assert os.path.exists(f'plot_{_ra_l}_{_dec_l}.png')


def test_telescope_22():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _coords = f"{_ra} {_dec}"
    _data_t = _tel_p.plot_airmass(obs_time=Time(get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True)), obs_coords=_coords, save=True)
    _data_f = _tel_p.plot_airmass(obs_time=Time(get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False)), obs_coords=_coords, save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_23():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _ra_l = _ra.replace(':', '').replace('.', '').strip()[:6]
    _dec_l = _dec.replace(':', '').replace('.', '').replace('-', '').replace('+', '').strip()[:6]
    _data_t = _tel_p.plot_airmass(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords, save=True)
    assert os.path.exists(f'plot_{_ra_l}_{_dec_l}.png')


# +
# AstroPlot().plot_all_altaz(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='',
#     ndays=AST__NDAYS, save=True, show=False)
# -
def test_telescope_30():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _data_t = _tel_p.plot_all_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1, save=True)
    _data_f = _tel_p.plot_all_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1, save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_31():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _ra_d, _dec_d = _tel_p.coords.ra.degree, _tel_p.coords.dec.degree
    _ra_s, _dec_s = ra_from_decimal(_ra_d), dec_from_decimal(_dec_d)
    _ra_l = _ra_s.replace(':', '').replace('.', '').strip()[:6]
    _dec_l = _dec_s.replace(':', '').replace('.', '').replace('-', '').replace('+', '').strip()[:6]
    _data_t = _tel_p.plot_all_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1, save=True)
    assert os.path.exists(f'plot_{_ra_l}_{_dec_l}.png')


def test_telescope_32():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _data_t = _tel_p.plot_all_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords, save=True)
    _data_f = _tel_p.plot_all_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_coords=_coords, save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_33():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _ra_l = _ra.replace(':', '').replace('.', '').strip()[:6]
    _dec_l = _dec.replace(':', '').replace('.', '').replace('-', '').replace('+', '').strip()[:6]
    _data_t = _tel_p.plot_all_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords, save=True)
    assert os.path.exists(f'plot_{_ra_l}_{_dec_l}.png')


# +
# AstroPlot().plot_moon_altaz(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS, save=True, show=False)
# -
# 40
def test_telescope_40():
    _data_t = _tel_p.plot_moon_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), save=True)
    _data_f = _tel_p.plot_moon_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_41():
    _data_t = _tel_p.plot_moon_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), save=True)
    assert os.path.exists(f'plot_moon.png')


# +
# AstroPlot().plot_sun_altaz(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS, save=True, show=False)
# -
def test_telescope_50():
    _data_t = _tel_p.plot_sun_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), save=True)
    _data_f = _tel_p.plot_sun_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_51():
    _data_t = _tel_p.plot_sun_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), save=True)
    assert os.path.exists('plot_sun.png')


# +
# AstroPlot().plot_target_altaz(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='',
#     ndays=AST__NDAYS, save=True, show=False)
# -
def test_telescope_60():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _data_t = _tel_p.plot_target_altaz(
        obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1, save=True)
    _data_f = _tel_p.plot_target_altaz(
        obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_name=_t1, save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_61():
    _t1 = OBS_ZODIAC.get(random.randint(0, 11), 'Polaris')
    _ra_d, _dec_d = _tel_p.coords.ra.degree, _tel_p.coords.dec.degree
    _ra_s, _dec_s = ra_from_decimal(_ra_d), dec_from_decimal(_dec_d)
    _ra_l = _ra_s.replace(':', '').replace('.', '').strip()[:6]
    _dec_l = _dec_s.replace(':', '').replace('.', '').replace('-', '').replace('+', '').strip()[:6]
    _data_t = _tel_p.plot_target_altaz(
        obs_time=get_isot(random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_name=_t1, save=True)
    assert os.path.exists(f'plot_{_ra_l}_{_dec_l}.png')


def test_telescope_62():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _data_t = _tel_p.plot_target_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords, save=True)
    _data_f = _tel_p.plot_target_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), False), obs_coords=_coords, save=True)
    assert all(isinstance(_k, str) for _k in [_data_t, _data_f])


def test_telescope_63():
    _ra = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.randint(0, 89):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    _dec = f"{random.choice(['-', '+'])}{_dec}"
    _coords = f"{_ra} {_dec}"
    _ra_l = _ra.replace(':', '').replace('.', '').strip()[:6]
    _dec_l = _dec.replace(':', '').replace('.', '').replace('-', '').replace('+', '').strip()[:6]
    _data_t = _tel_p.plot_target_altaz(obs_time=get_isot(
        random.randint(TEST_LOWER_BOUND, TEST_UPPER_BOUND), True), obs_coords=_coords, save=True)
    assert os.path.exists(f'plot_{_ra_l}_{_dec_l}.png')
