#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.instruments.factory import *


# +
# doc string(s)
# -
__doc__ = """
  % python3 -m pytest test_instruments.py
"""


# +
# test: Instrument()
# -
def test_instrument_1():
    """ tests INS__ structures """
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [INS__BINNING, INS__DITHER, INS__FILTERS, INS__FLAT__EXPOSURE__TIMES, INS__INSTRUMENTS, INS__NAME,
                INS__NODES, INS__READOUT, INS__READOUT__TIMES, INS__SLITS, INS__SUPPORTED, INS__TELESCOPE,
                INS__TELESCOPES, INS__TYPE]) in OBS_TRUE_VALUES


def test_instrument_2():
    """ test Instrument() for incorrect input(s) """
    with ptr(Exception):
        Instrument(name=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_instrument_3():
    """ test Instrument() for correct input(s) """
    assert isinstance(Instrument(random.choice(INS__INSTRUMENTS)), instruments.factory.Instrument) in OBS_TRUE_VALUES


# noinspection PyUnresolvedReferences
def test_instrument_4():
    """ test Instrument() returns correct attribute(s) """
    assert all(isinstance(_k, (float, int, str, list, dict, tuple)) for _k in
               [_a for _a in dir(Instrument(random.choice(INS__INSTRUMENTS))) if '__' not in _a]) in OBS_TRUE_VALUES
