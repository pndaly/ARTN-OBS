#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.observations.sidereal import *


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_sidereal.py
"""


# +
# test: Sidereal()
# -
def test_sidereal_1():
    """ test Sidereal() for incorrect input(s) """
    with ptr(Exception):
        Sidereal(telescope=random.choice([None, get_hash(), {}, [], ()]))


def test_sidereal_2():
    """ test Sidereal() for incorrect input(s) """
    with ptr(Exception):
        Sidereal(instrument=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_sidereal_3():
    """ test Sidereal() for correct input(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    assert isinstance(Sidereal(_tel, _ins), observations.sidereal.Sidereal) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_sidereal_4():
    """ test Sidereal() for correct input(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    assert isinstance(Sidereal(_tel, _ins).telescope, telescopes.factory.Telescope) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_sidereal_5():
    """ test Sidereal() for correct input(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    assert isinstance(Sidereal(_tel, _ins).instrument, instruments.factory.Instrument) in OBS_TRUE_VALUES


def test_sidereal_6():
    """ test Sidereal() returns correct attribute(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Sidereal(_tel, _ins)
    assert all(isinstance(_k, float) for _k in
               [_d.dawn_astronomical_jd, _d.dawn_civil_jd, _d.dawn_nautical_jd,
                _d.dusk_astronomical_jd, _d.dusk_civil_jd, _d.dusk_nautical_jd,
                _d.moon_rise_jd, _d.moon_set_jd, _d.mst_jd, _d.night_end_jd, _d.night_start_jd,
                _d.sun_rise_jd, _d.sun_set_jd, _d.utc_jd]) in OBS_TRUE_VALUES


def test_sidereal_7():
    """ test Sidereal() returns correct attribute(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Sidereal(_tel, _ins)
    assert all(isinstance(_k, (float, str)) for _k in
               [_d.time_for_darks, _d.time_for_flats, _d.time_for_foci,
                _d.time_for_non_sidereal, _d.time_for_sidereal, _d.dusk_nautical_jd,
                _d.dark_filter, _d.flat_filter, _d.foci_filter, _d.non_sidereal_filter,
                _d.sidereal_filter]) in OBS_TRUE_VALUES


def test_sidereal_8():
    """ test Sidereal() returns correct attribute(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Sidereal(_tel, _ins)
    assert all(isinstance(_k, (list, dict, tuple)) for _k in
               [_d.observing_night, _d.observing_night_r,
                _d.observing_night_jd, _d.observing_night_jd_r]) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_sidereal_9():
    """ test Sidereal() returns correct attribute(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Sidereal(_tel, _ins)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in
               [_d.dawn_astronomical, _d.dawn_civil, _d.dawn_nautical,
                _d.dusk_astronomical, _d.dusk_civil, _d.dusk_nautical,
                _d.moon_rise, _d.moon_set, _d.mst, _d.night_end, _d.night_start,
                _d.sun_rise, _d.sun_set, _d.utc]) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_sidereal_10():
    """ test Sidereal() returns correct attribute(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _iso, _jd = Sidereal(_tel, _ins).calculate()
    assert re.match(OBS_ISO_PATTERN, _iso) is not None


# noinspection PyUnresolvedReferences
def test_sidereal_11():
    """ test Sidereal() returns correct attribute(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _iso, _jd = Sidereal(_tel, _ins).calculate()
    assert (isinstance(_jd, float) and _jd is not math.nan) in OBS_TRUE_VALUES