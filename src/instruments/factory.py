#!/usr/bin/env python3


# +
# import(s)
# -
from src import *
from src.instruments import *


# +
# (factory) class: Instrument()
# -
# noinspection PyBroadException,PyUnresolvedReferences,PyTypeChecker
class Instrument(object):

    # +
    # method: __init__
    # -
    def __init__(self, name='', log=None):

        # get input(s)
        self.name = name
        self.log = log

        # set default(s)
        self.__msg = None
        self.__binning = INS__BINNING[self.__name]
        self.__dither = INS__DITHER[self.__name] if INS__TYPE == 'imager' else None
        self.__filters = INS__FILTERS[self.__name]
        self.__flat_exposure_times = INS__FLAT__EXPOSURE__TIMES[self.__name]
        self.__readout = INS__READOUT[self.__name]
        self.__readout_times = INS__READOUT__TIMES[self.__name]
        self.__slits = INS__SLITS[self.__name] if INS__TYPE == 'spectrograph' else None
        self.__telescope = INS__TELESCOPE[self.__name]
        self.__type = INS__TYPE[self.__name]
        self.__supported = INS__SUPPORTED[self.__telescope]

    # +
    # class method: instrument()
    # -
    @classmethod
    def instrument(cls, name='', log=None):
        """ returns a new class """
        return cls(name, log)

    # +
    # Decorator(s) for getter(s) and setter(s)
    # -
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=''):
        self.__name = name if (isinstance(name, str) and name in INS__INSTRUMENTS) else INS__INSTRUMENTS[0]

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log=None):
        self.__log = log if isinstance(log, logging.Logger) else None

    # + 
    # getters without setters
    # -
    @property
    def binning(self):
        return self.__binning

    @property
    def dither(self):
        return self.__dither

    @property
    def filters(self):
        return self.__filters

    @property
    def flat_exposure_times(self):
        return self.__flat_exposure_times

    @property
    def readout(self):
        return float(self.__readout)

    @property
    def readout_times(self):
        return self.__readout_times

    @property
    def slits(self):
        return self.__slits

    @property
    def telescope(self):
        return self.__telescope

    @property
    def type(self):
        return self.__type

    @property
    def supported(self):
        return self.__supported

    # +
    # method: __dump__()
    # -
    def __dump__(self, item=None):
        """ dump variable(s) """
        if item is None:
            self.__msg = ''
        if isinstance(item, tuple) and not ():
            self.__msg = ''.join('{}\n'.format(str(v)) for v in item)[:-1]
        elif isinstance(item, list) and not []:
            self.__msg = ''.join('{}\n'.format(str(v)) for v in item)[:-1]
        elif isinstance(item, set) and not {}:
            self.__msg = ''.join('{}\n'.format(str(v)) for v in item)[:-1]
        elif isinstance(item, dict) and not {}:
            self.__msg = ''.join('{}={}\n'.format(str(k), str(v)) for k, v in item.items())[:-1]
        else:
            self.__msg = ''.join('{}\n'.format(str(item)))
        if self.__log is not None:
            self.__log.debug(f'{self.__msg}')
