#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.tests import *
from src.observations.foci import *


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_foci.py
"""


# +
# test: Foci()
# -
def test_foci_0():
    with ptr(Exception):
        Foci(telescope=random.choice(TEST_INVALID_INPUTS))


def test_foci_1():
    with ptr(Exception):
        Foci(instrument=random.choice(TEST_INVALID_INPUTS))


def test_foci_2():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    # noinspection PyUnresolvedReferences
    assert isinstance(Foci(_tel, _ins), observations.foci.Foci)


def test_foci_3():
    """ test Foci() for correct input(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    # noinspection PyUnresolvedReferences
    assert isinstance(Foci(_tel, _ins).telescope, telescopes.factory.Telescope)


def test_foci_4():
    """ test Foci() for correct input(s) """
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    # noinspection PyUnresolvedReferences
    assert isinstance(Foci(_tel, _ins).instrument, instruments.factory.Instrument)


def test_foci_5():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Foci(_tel, _ins)
    assert all(isinstance(_k, float) for _k in
               [_d.dawn_astronomical_jd, _d.dawn_civil_jd, _d.dawn_nautical_jd,
                _d.dusk_astronomical_jd, _d.dusk_civil_jd, _d.dusk_nautical_jd,
                _d.moon_rise_jd, _d.moon_set_jd, _d.mst_jd, _d.night_end_jd, _d.night_start_jd,
                _d.sun_rise_jd, _d.sun_set_jd, _d.utc_jd])


def test_foci_6():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Foci(_tel, _ins)
    assert all(isinstance(_k, (float, str)) for _k in
               [_d.time_for_darks, _d.time_for_flats, _d.time_for_foci,
                _d.time_for_non_sidereal, _d.time_for_sidereal, _d.dusk_nautical_jd,
                _d.dark_filter, _d.flat_filter, _d.foci_filter, _d.non_sidereal_filter,
                _d.sidereal_filter])


def test_foci_7():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Foci(_tel, _ins)
    assert all(isinstance(_k, (list, dict, tuple)) for _k in
               [_d.observing_night, _d.observing_night_r,
                _d.observing_night_jd, _d.observing_night_jd_r])


def test_foci_8():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _d = Foci(_tel, _ins)
    assert all(re.match(OBS_ISO_PATTERN, _k) is not None for _k in
               [_d.dawn_astronomical, _d.dawn_civil, _d.dawn_nautical,
                _d.dusk_astronomical, _d.dusk_civil, _d.dusk_nautical,
                _d.moon_rise, _d.moon_set, _d.mst, _d.night_end, _d.night_start,
                _d.sun_rise, _d.sun_set, _d.utc])


def test_foci_9():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _iso, _jd = Foci(_tel, _ins).calculate()
    assert re.match(OBS_ISO_PATTERN, _iso) is not None


def test_foci_10():
    _ins = random.choice(INS__INSTRUMENTS)
    _tel = INS__TELESCOPE[_ins]
    _iso, _jd = Foci(_tel, _ins).calculate()
    assert (isinstance(_jd, float) and _jd is not math.nan)
