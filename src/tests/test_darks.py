#!/usr/bin/env python3


# +
# import(s)
# -
from . import *
from pytest import raises as ptr
from src.observations.darks import *


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_darks.py
"""


# +
# test: Darks()
# -
def test_darks_0():
    with ptr(Exception):
        Darks(telescope=random.choice(TEST_INVALID_INPUTS))


def test_darks_1():
    with ptr(Exception):
        Darks(instrument=random.choice(TEST_INVALID_INPUTS))


def test_darks_2():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    # noinspection PyUnresolvedReferences
    assert isinstance(Darks(_tel, _ins), observations.darks.Darks)


def test_darks_3():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    # noinspection PyUnresolvedReferences
    assert isinstance(Darks(_tel, _ins).telescope, telescopes.factory.Telescope)


def test_darks_4():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    # noinspection PyUnresolvedReferences
    assert isinstance(Darks(_tel, _ins).instrument, instruments.factory.Instrument)


def test_darks_5():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Darks(_tel, _ins)
    assert all(isinstance(_k, float) for _k in
               [_d.dawn_astronomical_jd, _d.dawn_civil_jd, _d.dawn_nautical_jd,
                _d.dusk_astronomical_jd, _d.dusk_civil_jd, _d.dusk_nautical_jd,
                _d.moon_rise_jd, _d.moon_set_jd, _d.mst_jd, _d.night_end_jd, _d.night_start_jd,
                _d.sun_rise_jd, _d.sun_set_jd, _d.utc_jd])


def test_darks_6():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Darks(_tel, _ins)
    assert all(isinstance(_k, (float, str)) for _k in
               [_d.time_for_darks, _d.time_for_flats, _d.time_for_foci,
                _d.time_for_non_sidereal, _d.time_for_sidereal, _d.dusk_nautical_jd,
                _d.dark_filter, _d.flat_filter, _d.foci_filter, _d.non_sidereal_filter,
                _d.sidereal_filter])


def test_darks_7():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Darks(_tel, _ins)
    assert all(isinstance(_k, (list, dict, tuple)) for _k in
               [_d.observing_night, _d.observing_night_r,
                _d.observing_night_jd, _d.observing_night_jd_r])


def test_darks_8():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Darks(_tel, _ins)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in
               [_d.dawn_astronomical, _d.dawn_civil, _d.dawn_nautical,
                _d.dusk_astronomical, _d.dusk_civil, _d.dusk_nautical,
                _d.moon_rise, _d.moon_set, _d.mst, _d.night_end, _d.night_start,
                _d.sun_rise, _d.sun_set, _d.utc])


def test_darks_9():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _iso, _jd = Darks(_tel, _ins).calculate()
    assert re.match(OBS_ISO_PATTERN, _iso) is not None


def test_darks_10():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _iso, _jd = Darks(_tel, _ins).calculate()
    assert (isinstance(_jd, float) and _jd is not math.nan)
