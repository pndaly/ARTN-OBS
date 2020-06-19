#!/usr/bin/env python3


# +
#  import(s)
# -
from src.instruments.factory import *
from src.telescopes.factory import *


# +
# __doc__
# -
__doc__ = """

  class ObsParams(object) - Creates an object to hold telescope and instrument specific parameter(s)
  
  Example:
    from src.observations.obsparams import *
    _l = Logger().logger
    _t = Telescope('Kuiper')
    _i = Instrument('Mont4k')
    _o = ObsParams(telescope=_t, instrument=_i, log=_l)
    _o.__dump__()

"""


# +
# class: ObsParams()
# -
# noinspection PyBroadException,PyUnresolvedReferences
class ObsParams(object):
    """ store observation parameter(s) """

    # +
    # class variable(s)
    # -
    time_for_darks = 1.0 / 24.0
    time_for_foci = 0.5 / 24.0
    time_for_non_sidereal = 0.5 / 24.0
    time_for_sidereal = 3.0 / 24.0

    # +
    # method: __init__()
    # -
    def __init__(self, telescope=None, instrument=None, log=None):

        # get input(s)
        self.telescope = telescope
        self.instrument = instrument
        self.log = log

        # initialize all variable(s)
        self.__dawn_astronomical = None
        self.__dawn_astronomical_jd = None
        self.__dawn_civil = None
        self.__dawn_civil_jd = None
        self.__dawn_nautical = None
        self.__dawn_nautical_jd = None
        self.__dusk_astronomical = None
        self.__dusk_astronomical_jd = None
        self.__dusk_civil = None
        self.__dusk_civil_jd = None
        self.__dusk_nautical = None
        self.__dusk_nautical_jd = None
        self.__moon_rise = None
        self.__moon_rise_jd = None
        self.__moon_set = None
        self.__moon_set_jd = None
        self.__mst = None
        self.__mst_jd = None
        self.__night_start = None
        self.__night_start_jd = None
        self.__night_end = None
        self.__night_end_jd = None
        self.__observing_night = {}
        self.__observing_night_r = {}
        self.__observing_night_jd = {}
        self.__observing_night_jd_r = {}
        self.__sun_rise = None
        self.__sun_rise_jd = None
        self.__sun_set = None
        self.__sun_set_jd = None
        self.__utc = None
        self.__utc_jd = None

        # refresh
        self.refresh()

    # +
    # decorator(s)
    # -
    @property
    def telescope(self):
        return self.__telescope

    @telescope.setter
    def telescope(self, telescope=None):
        # use the input telescope object
        if isinstance(telescope, telescopes.factory.Telescope):
            self.__telescope = telescope
        # create a new telescope object
        elif isinstance(telescope, str) and telescope in TEL__TELESCOPES:
            self.__telescope = Telescope(name=telescope)
        # unrecognized input
        else:
            self.__telescope = None
        # on failure, return error
        if self.__telescope is None:
            raise Exception(f'invalid input, telescope={telescope}')

    @property
    def instrument(self):
        return self.__instrument

    @instrument.setter
    def instrument(self, instrument=None):
        # use the input instrument object
        if isinstance(instrument, instruments.factory.Instrument):
            self.__instrument = instrument
        # create a new instrument object
        elif isinstance(instrument, str) and instrument in INS__INSTRUMENTS:
            self.__instrument = Instrument(name=instrument)
        # unrecognized input
        else:
            self.__instrument = None
        # on failure, return error
        if self.__instrument is None:
            raise Exception(f'invalid input, instrument={instrument}')
        # unsupported combination, report error
        if self.__instrument.name not in INS__SUPPORTED[self.__telescope.name]:
            raise Exception(f'invalid combination, instrument={self.__instrument.name}, telescope={self.__telescope.name}')

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log=None):
        # use the input logger object
        if isinstance(log, logging.Logger):
            self.__log = log
        # create a new logger object
        elif isinstance(log, bool):
            self.__log = Logger(f'{self.__telescope.name}-{self.__instrument.name}').logger
        # do nothing
        else:
            self.__log = None

    # +
    # getter(s)
    # -
    @property
    def dawn_astronomical(self):
        return self.__dawn_astronomical

    @property
    def dawn_astronomical_jd(self):
        return self.__dawn_astronomical_jd

    @property
    def dawn_civil(self):
        return self.__dawn_civil

    @property
    def dawn_civil_jd(self):
        return self.__dawn_civil_jd

    @property
    def dawn_nautical(self):
        return self.__dawn_nautical

    @property
    def dawn_nautical_jd(self):
        return self.__dawn_nautical_jd

    @property
    def dusk_astronomical(self):
        return self.__dusk_astronomical

    @property
    def dusk_astronomical_jd(self):
        return self.__dusk_astronomical_jd

    @property
    def dusk_civil(self):
        return self.__dusk_civil

    @property
    def dusk_civil_jd(self):
        return self.__dusk_civil_jd

    @property
    def dusk_nautical(self):
        return self.__dusk_nautical

    @property
    def dusk_nautical_jd(self):
        return self.__dusk_nautical_jd

    @property
    def moon_rise(self):
        return self.__moon_rise

    @property
    def moon_rise_jd(self):
        return self.__moon_rise_jd

    @property
    def moon_set(self):
        return self.__moon_set

    @property
    def moon_set_jd(self):
        return self.__moon_set_jd

    @property
    def mst(self):
        return self.__mst

    @property
    def mst_jd(self):
        return self.__mst_jd

    @property
    def night_start(self):
        return self.__night_start

    @property
    def night_start_jd(self):
        return self.__night_start_jd

    @property
    def night_end(self):
        return self.__night_end

    @property
    def night_end_jd(self):
        return self.__night_end_jd

    @property
    def observing_night(self):
        return self.__observing_night

    @property
    def observing_night_r(self):
        return self.__observing_night_r

    @property
    def observing_night_jd(self):
        return self.__observing_night_jd

    @property
    def observing_night_jd_r(self):
        return self.__observing_night_jd_r

    @property
    def sun_rise(self):
        return self.__sun_rise

    @property
    def sun_rise_jd(self):
        return self.__sun_rise_jd

    @property
    def sun_set(self):
        return self.__sun_set

    @property
    def sun_set_jd(self):
        return self.__sun_set_jd

    @property
    def utc(self):
        return self.__utc

    @property
    def utc_jd(self):
        return self.__utc_jd

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

        if self.__log:
            self.__log.debug(f"self.__dawn_astronomical={self.__dawn_astronomical}")
            self.__log.debug(f"self.__dawn_astronomical_jd={self.__dawn_astronomical_jd}")
            self.__log.debug(f"self.__dawn_civil={self.__dawn_civil}")
            self.__log.debug(f"self.__dawn_civil_jd={self.__dawn_civil_jd}")
            self.__log.debug(f"self.__dawn_nautical={self.__dawn_nautical}")
            self.__log.debug(f"self.__dawn_nautical_jd={self.__dawn_nautical_jd}")
            self.__log.debug(f"self.__dusk_astronomical={self.__dusk_astronomical}")
            self.__log.debug(f"self.__dusk_astronomical_jd={self.__dusk_astronomical_jd}")
            self.__log.debug(f"self.__dusk_civil={self.__dusk_civil}")
            self.__log.debug(f"self.__dusk_civil_jd={self.__dusk_civil_jd}")
            self.__log.debug(f"self.__dusk_nautical={self.__dusk_nautical}")
            self.__log.debug(f"self.__dusk_nautical_jd={self.__dusk_nautical_jd}")
            self.__log.debug(f"self.__instrument={self.__instrument}")
            self.__log.debug(f"self.__moon_rise={self.__moon_rise}")
            self.__log.debug(f"self.__moon_rise_jd={self.__moon_rise_jd}")
            self.__log.debug(f"self.__moon_set={self.__moon_set}")
            self.__log.debug(f"self.__moon_set_jd={self.__moon_set_jd}")
            self.__log.debug(f"self.__mst={self.__mst}")
            self.__log.debug(f"self.__mst_jd={self.__mst_jd}")
            self.__log.debug(f"self.__night_start={self.__night_start}")
            self.__log.debug(f"self.__night_start_jd={self.__night_start_jd}")
            self.__log.debug(f"self.__night_end={self.__night_end}")
            self.__log.debug(f"self.__night_end_jd={self.__night_end_jd}")
            self.__log.debug(f"self.__observing_night={self.__observing_night}")
            self.__log.debug(f"self.__observing_night_r={self.__observing_night_r}")
            self.__log.debug(f"self.__observing_night_jd={self.__observing_night_jd}")
            self.__log.debug(f"self.__observing_night_jd_r={self.__observing_night_jd_r}")
            self.__log.debug(f"self.__sun_rise={self.__sun_rise}")
            self.__log.debug(f"self.__sun_rise_jd={self.__sun_rise_jd}")
            self.__log.debug(f"self.__sun_set={self.__sun_set}")
            self.__log.debug(f"self.__sun_set_jd={self.__sun_set_jd}")
            self.__log.debug(f"self.__telescope={self.__telescope}")
            self.__log.debug(f"self.__utc={self.__utc}")
            self.__log.debug(f"self.__utc_jd={self.__utc_jd}")

    # +
    # method: refresh()
    # -
    def refresh(self):
        """ refresh all variable(s) """

        # initialize all variable(s)
        self.__mst = get_isot(0, False)
        self.__utc = get_isot(0, True)
        self.__mst_jd = isot_to_jd(self.__mst)
        self.__utc_jd = isot_to_jd(self.__utc)

        self.__moon_rise = self.__telescope.moon_rise(obs_time=self.__utc, which='next')
        self.__moon_rise_jd = isot_to_jd(self.__moon_rise)
        self.__moon_set = self.__telescope.moon_set(obs_time=self.__utc, which='next')
        self.__moon_set_jd = isot_to_jd(self.__moon_set)

        self.__sun_rise = self.__telescope.sun_rise(obs_time=self.__utc, which='next')
        self.__sun_rise_jd = isot_to_jd(self.__sun_rise)
        self.__sun_set = self.__telescope.sun_set(obs_time=self.__utc, which='next')
        self.__sun_set_jd = isot_to_jd(self.__sun_set)

        self.__dawn_astronomical = self.__telescope.dawn(obs_time=self.__utc, which='next', twilight='astronomical')
        self.__dawn_astronomical_jd = isot_to_jd(self.__dawn_astronomical)
        self.__dawn_civil = self.__telescope.dawn(obs_time=self.__utc, which='next', twilight='civil')
        self.__dawn_civil_jd = isot_to_jd(self.__dawn_civil)
        self.__dawn_nautical = self.__telescope.dawn(obs_time=self.__utc, which='next', twilight='nautical')
        self.__dawn_nautical_jd = isot_to_jd(self.__dawn_nautical)

        self.__dusk_astronomical = self.__telescope.dusk(obs_time=self.__utc, which='next', twilight='astronomical')
        self.__dusk_astronomical_jd = isot_to_jd(self.__dusk_astronomical)
        self.__dusk_civil = self.__telescope.dusk(obs_time=self.__utc, which='next', twilight='civil')
        self.__dusk_civil_jd = isot_to_jd(self.__dusk_civil)
        self.__dusk_nautical = self.__telescope.dusk(obs_time=self.__utc, which='next', twilight='nautical')
        self.__dusk_nautical_jd = isot_to_jd(self.__dusk_nautical)

        self.__night_start = self.__telescope.observing_start(self.__utc)
        self.__night_start_jd = isot_to_jd(self.__night_start)
        self.__night_end = self.__telescope.observing_end(self.__utc)
        self.__night_end_jd = isot_to_jd(self.__night_end)

        self.__observing_night = {
            'mst': self.__mst,
            'night_start': self.__night_start,
            'night_end': self.__night_end,
            'moon_rise': self.__moon_rise,
            'moon_set': self.__moon_set,
            'sun_rise': self.__sun_rise,
            'sun_set': self.__sun_set,
            'dawn_astronomical': self.__dawn_astronomical,
            'dawn_civil': self.__dawn_civil,
            'dawn_nautical': self.__dawn_nautical,
            'dusk_astronomical': self.__dusk_astronomical,
            'dusk_civil': self.__dusk_civil,
            'dusk_nautical': self.__dusk_nautical
        }
        self.__observing_night_r = {_v: _k for _k, _v in self.__observing_night.items()}
        self.__observing_night_jd = {
            'mst_jd': self.__mst_jd,
            'night_start_jd': self.__night_start_jd,
            'night_end_jd': self.__night_end_jd,
            'moon_rise_jd': self.__moon_rise_jd,
            'moon_set_jd': self.__moon_set_jd,
            'sun_rise_jd': self.__sun_rise_jd,
            'sun_set_jd': self.__sun_set_jd,
            'dawn_astronomical_jd': self.__dawn_astronomical_jd,
            'dawn_civil_jd': self.__dawn_civil_jd,
            'dawn_nautical_jd': self.__dawn_nautical_jd,
            'dusk_astronomical_jd': self.__dusk_astronomical_jd,
            'dusk_civil_jd': self.__dusk_civil_jd,
            'dusk_nautical_jd': self.__dusk_nautical_jd
        }
        self.__observing_night_jd_r = {_v: _k for _k, _v in self.__observing_night_jd.items()}
