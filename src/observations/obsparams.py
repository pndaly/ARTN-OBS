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
# constant(s)
# -
OBSPARAM_DARK_CONE_ANGLE = math.nan
OBSPARAM_FLAT_CONE_ANGLE = math.nan
OBSPARAM_FOCI_CONE_ANGLE = 35.0
OBSPARAM_HOURS_PER_DAY = 24.0
OBSPARAM_NON_SIDEREAL_CONE_ANGLE = 20.0
OBSPARAM_SIDEREAL_CONE_ANGLE = 25.0
OBSPARAM_TIME_FOR_DARKS = 1.0 / OBSPARAM_HOURS_PER_DAY
OBSPARAM_TIME_FOR_FLATS = 1.5 / OBSPARAM_HOURS_PER_DAY
OBSPARAM_TIME_FOR_FOCI = 0.5 / OBSPARAM_HOURS_PER_DAY
OBSPARAM_TIME_FOR_NON_SIDEREAL = 0.5 / OBSPARAM_HOURS_PER_DAY
OBSPARAM_TIME_FOR_SIDEREAL = 3.0 / OBSPARAM_HOURS_PER_DAY


# +
# class: ObsParams()
# -
# noinspection PyBroadException,PyUnresolvedReferences
class ObsParams(object):
    """ store observation parameter(s) """

    # +
    # method: __init__()
    # -
    def __init__(self, telescope=None, instrument=None, log=None):

        # get input(s)
        self.telescope = telescope
        self.instrument = instrument
        self.log = log

        # other getter/setter variable(s)
        self.__time_for_darks = OBSPARAM_TIME_FOR_DARKS
        self.__time_for_flats = OBSPARAM_TIME_FOR_FLATS
        self.__time_for_foci = OBSPARAM_TIME_FOR_FOCI
        self.__time_for_non_sidereal = OBSPARAM_TIME_FOR_NON_SIDEREAL
        self.__time_for_sidereal = OBSPARAM_TIME_FOR_SIDEREAL

        self.__dark_cone_angle = OBSPARAM_DARK_CONE_ANGLE
        self.__flat_cone_angle = OBSPARAM_FLAT_CONE_ANGLE
        self.__foci_cone_angle = OBSPARAM_FOCI_CONE_ANGLE
        self.__non_sidereal_cone_angle = OBSPARAM_NON_SIDEREAL_CONE_ANGLE
        self.__sidereal_cone_angle = OBSPARAM_SIDEREAL_CONE_ANGLE

        self.__dark_filter = random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()
        self.__flat_filter = random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()
        self.__foci_filter = random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()
        self.__non_sidereal_filter = random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()
        self.__sidereal_filter = random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()

        self.__dark_binning = random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()
        self.__flat_binning = random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()
        self.__foci_binning = random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()
        self.__non_sidereal_binning = random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()
        self.__sidereal_binning = random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()

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
            raise Exception(f'invalid combination, instrument={self.__instrument.name}, '
                            f'telescope={self.__telescope.name}')

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
    # other getter(s) / setter(s)
    # -
    @property
    def dark_cone_angle(self):
        return self.__dark_cone_angle

    @dark_cone_angle.setter
    def dark_cone_angle(self, dark_cone_angle=OBSPARAM_DARK_CONE_ANGLE):
        self.__dark_cone_angle = dark_cone_angle if \
            (isinstance(dark_cone_angle, float) and (0.0 <= dark_cone_angle <= 180.0)) else OBSPARAM_DARK_CONE_ANGLE

    @property
    def flat_cone_angle(self):
        return self.__flat_cone_angle

    @flat_cone_angle.setter
    def flat_cone_angle(self, flat_cone_angle=OBSPARAM_FLAT_CONE_ANGLE):
        self.__flat_cone_angle = flat_cone_angle if \
            (isinstance(flat_cone_angle, float) and (0.0 <= flat_cone_angle <= 180.0)) else OBSPARAM_FLAT_CONE_ANGLE

    @property
    def foci_cone_angle(self):
        return self.__foci_cone_angle

    @foci_cone_angle.setter
    def foci_cone_angle(self, foci_cone_angle=OBSPARAM_FOCI_CONE_ANGLE):
        self.__foci_cone_angle = foci_cone_angle if \
            (isinstance(foci_cone_angle, float) and (0.0 <= foci_cone_angle <= 180.0)) else OBSPARAM_FOCI_CONE_ANGLE

    @property
    def non_sidereal_cone_angle(self):
        return self.__non_sidereal_cone_angle

    @non_sidereal_cone_angle.setter
    def non_sidereal_cone_angle(self, non_sidereal_cone_angle=OBSPARAM_NON_SIDEREAL_CONE_ANGLE):
        self.__non_sidereal_cone_angle = non_sidereal_cone_angle if \
            (isinstance(non_sidereal_cone_angle, float) and (0.0 <= non_sidereal_cone_angle <= 180.0)) else \
            OBSPARAM_NON_SIDEREAL_CONE_ANGLE

    @property
    def sidereal_cone_angle(self):
        return self.__sidereal_cone_angle

    @sidereal_cone_angle.setter
    def sidereal_cone_angle(self, sidereal_cone_angle=OBSPARAM_SIDEREAL_CONE_ANGLE):
        self.__sidereal_cone_angle = sidereal_cone_angle if \
            (isinstance(sidereal_cone_angle, float) and (0.0 <= sidereal_cone_angle <= 180.0)) else \
            OBSPARAM_SIDEREAL_CONE_ANGLE

    @property
    def dark_binning(self):
        return self.__dark_binning

    @dark_binning.setter
    def dark_binning(self, dark_binning=None):
        self.__dark_binning = dark_binning if \
            (isinstance(dark_binning, str) and dark_binning.strip() != '' and
             dark_binning in INS__BINNING[self.__instrument.name]) else \
            random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()

    @property
    def flat_binning(self):
        return self.__flat_binning

    @flat_binning.setter
    def flat_binning(self, flat_binning=None):
        self.__flat_binning = flat_binning if \
            (isinstance(flat_binning, str) and flat_binning.strip() != '' and
             flat_binning in INS__BINNING[self.__instrument.name]) else \
            random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()

    @property
    def foci_binning(self):
        return self.__foci_binning

    @foci_binning.setter
    def foci_binning(self, foci_binning=None):
        self.__foci_binning = foci_binning if \
            (isinstance(foci_binning, str) and foci_binning.strip() != '' and
             foci_binning in INS__BINNING[self.__instrument.name]) else \
            random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()

    @property
    def non_sidereal_binning(self):
        return self.__non_sidereal_binning

    @non_sidereal_binning.setter
    def non_sidereal_binning(self, non_sidereal_binning=None):
        self.__non_sidereal_binning = non_sidereal_binning if \
            (isinstance(non_sidereal_binning, str) and non_sidereal_binning.strip() != '' and
             non_sidereal_binning in INS__BINNING[self.__instrument.name]) else \
            random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()

    @property
    def sidereal_binning(self):
        return self.__sidereal_binning

    @sidereal_binning.setter
    def sidereal_binning(self, sidereal_binning=None):
        self.__sidereal_binning = sidereal_binning if \
            (isinstance(sidereal_binning, str) and sidereal_binning.strip() != '' and
             sidereal_binning in INS__BINNING[self.__instrument.name]) else \
            random.choice(INS__BINNING[self.__instrument.name].split(',')).strip()

    @property
    def dark_filter(self):
        return self.__dark_filter

    @dark_filter.setter
    def dark_filter(self, dark_filter=None):
        self.__dark_filter = dark_filter if \
            (isinstance(dark_filter, str) and dark_filter.strip() != '' and
             dark_filter in INS__FILTERS[self.__instrument.name]) else \
            random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()

    @property
    def flat_filter(self):
        return self.__flat_filter

    @flat_filter.setter
    def flat_filter(self, flat_filter=None):
        self.__flat_filter = flat_filter if \
            (isinstance(flat_filter, str) and flat_filter.strip() != '' and
             flat_filter in INS__FILTERS[self.__instrument.name]) else \
            random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()

    @property
    def foci_filter(self):
        return self.__foci_filter

    @foci_filter.setter
    def foci_filter(self, foci_filter=None):
        self.__foci_filter = foci_filter if \
            (isinstance(foci_filter, str) and foci_filter.strip() != '' and
             foci_filter in INS__FILTERS[self.__instrument.name]) else \
            random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()

    @property
    def non_sidereal_filter(self):
        return self.__non_sidereal_filter

    @non_sidereal_filter.setter
    def non_sidereal_filter(self, non_sidereal_filter=None):
        self.__non_sidereal_filter = non_sidereal_filter if \
            (isinstance(non_sidereal_filter, str) and non_sidereal_filter.strip() != '' and
             non_sidereal_filter in INS__FILTERS[self.__instrument.name]) else \
            random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()

    @property
    def sidereal_filter(self):
        return self.__sidereal_filter

    @sidereal_filter.setter
    def sidereal_filter(self, sidereal_filter=None):
        self.__sidereal_filter = sidereal_filter if \
            (isinstance(sidereal_filter, str) and sidereal_filter.strip() != '' and
             sidereal_filter in INS__FILTERS[self.__instrument.name]) else \
            random.choice(INS__FILTERS[self.__instrument.name].split(',')).strip()

    @property
    def time_for_darks(self):
        return self.__time_for_darks

    @time_for_darks.setter
    def time_for_darks(self, time_for_darks=OBSPARAM_TIME_FOR_DARKS):
        self.__time_for_darks = time_for_darks if \
            (isinstance(time_for_darks, float) and (0.0 < time_for_darks < 1.0)) else OBSPARAM_TIME_FOR_DARKS

    @property
    def time_for_flats(self):
        return self.__time_for_flats

    @time_for_flats.setter
    def time_for_flats(self, time_for_flats=OBSPARAM_TIME_FOR_FLATS):
        self.__time_for_flats = time_for_flats if \
            (isinstance(time_for_flats, float) and (0.0 < time_for_flats < 1.0)) else OBSPARAM_TIME_FOR_FLATS

    @property
    def time_for_foci(self):
        return self.__time_for_foci

    @time_for_foci.setter
    def time_for_foci(self, time_for_foci=OBSPARAM_TIME_FOR_FOCI):
        self.__time_for_foci = time_for_foci if \
            (isinstance(time_for_foci, float) and (0.0 < time_for_foci < 1.0)) else OBSPARAM_TIME_FOR_FOCI

    @property
    def time_for_non_sidereal(self):
        return self.__time_for_non_sidereal

    @time_for_non_sidereal.setter
    def time_for_non_sidereal(self, time_for_non_sidereal=OBSPARAM_TIME_FOR_NON_SIDEREAL):
        self.__time_for_non_sidereal = time_for_non_sidereal if \
            (isinstance(time_for_non_sidereal, float) and (0.0 < time_for_non_sidereal < 1.0)) else \
            OBSPARAM_TIME_FOR_NON_SIDEREAL

    @property
    def time_for_sidereal(self):
        return self.__time_for_sidereal

    @time_for_sidereal.setter
    def time_for_sidereal(self, time_for_sidereal=OBSPARAM_TIME_FOR_SIDEREAL):
        self.__time_for_sidereal = time_for_sidereal if \
            (isinstance(time_for_sidereal, float) and (0.0 < time_for_sidereal < 1.0)) else OBSPARAM_TIME_FOR_SIDEREAL

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
            self.__log.debug(f"self.__time_for_darks={self.__time_for_darks}")
            self.__log.debug(f"self.__time_for_flats={self.__time_for_flats}")
            self.__log.debug(f"self.__time_for_foci={self.__time_for_foci}")
            self.__log.debug(f"self.__time_for_non_sidereal={self.__time_for_non_sidereal}")
            self.__log.debug(f"self.__time_for_sidereal={self.__time_for_sidereal}")
            self.__log.debug(f"self.__utc={self.__utc}")
            self.__log.debug(f"self.__utc_jd={self.__utc_jd}")
            self.__log.debug(f"self.__dark_binning={self.__dark_binning}")
            self.__log.debug(f"self.__flat_binning={self.__flat_binning}")
            self.__log.debug(f"self.__foci_binning={self.__foci_binning}")
            self.__log.debug(f"self.__non_sidereal_binning={self.__non_sidereal_binning}")
            self.__log.debug(f"self.__sidereal_binning={self.__sidereal_binning}")
            self.__log.debug(f"self.__dark_filter={self.__dark_filter}")
            self.__log.debug(f"self.__flat_filter={self.__flat_filter}")
            self.__log.debug(f"self.__foci_filter={self.__foci_filter}")
            self.__log.debug(f"self.__non_sidereal_filter={self.__non_sidereal_filter}")
            self.__log.debug(f"self.__sidereal_filter={self.__sidereal_filter}")
            self.__log.debug(f"self.__dark_cone_angle={self.__dark_cone_angle}")
            self.__log.debug(f"self.__flat_cone_angle={self.__flat_cone_angle}")
            self.__log.debug(f"self.__foci_cone_angle={self.__foci_cone_angle}")
            self.__log.debug(f"self.__non_sidereal_cone_angle={self.__non_sidereal_cone_angle}")
            self.__log.debug(f"self.__sidereal_cone_angle={self.__sidereal_cone_angle}")

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
