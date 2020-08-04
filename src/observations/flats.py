#!/usr/bin/env python3


# +
#  import(s)
# -
from src.observations.obsparams import *


# +
# __doc__
# -
__doc__ = """

  class Flats(ObsParams) - Creates an object to calculate flat observation(s) between limits
  
  Example:
    from src.observations.flats import *
    _l = Logger().logger
    _t = Telescope('Kuiper')
    _i = Instrument('Mont4k')
    _o = Flats(telescope=_t, instrument=_i, log=_l)
    _o.__dump__()
    _o.__flats_dump__()
    _o.calculate()

"""


# +
# class: Flats()
# -
# noinspection PyBroadException,PyUnresolvedReferences
class Flats(ObsParams):
    """ generate flat observation(s) """

    # +
    # method: __init__()
    # -
    def __init__(self, telescope=None, instrument=None, log=None):

        # initialize parent(s)
        super().__init__(telescope, instrument, log)
        self.__telescope = self.telescope
        self.__instrument = self.instrument
        self.__log = self.log

        # initialize other variable(s)
        self.__begin = None
        self.__begin_jd = None
        self.__delta = None
        self.__elapsed_time_jd = None
        self.__end = None
        self.__end_flats_jd = None
        self.__end_jd = None
        self.__end_time = None
        self.__end_time_jd = None
        self.__msg = None
        self.__num_flats = None
        self.__num_flat_sets = None
        self.__seconds = None
        self.__start_flats_jd = None
        self.__time_per_observation = None
        self.__total_exps = None
        self.__total_time = None

        # calculate
        self.__flat_times = self.__instrument.flat_exposure_times
        self.__read_times = self.__instrument.readout_times
        self.__ave_flat_time = sum(_v for _v in self.__flat_times.values()) / len(self.__flat_times)
        self.__ave_read_time = sum(_v for _v in self.__read_times.values()) / len(self.__read_times)

    # +
    # method: __flats_dump__()
    # -
    def __flats_dump__(self, item=None):
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
            self.__log.debug(f'self={self}')
            self.__log.debug(f"self.__ave_flat_time = {self.__ave_flat_time}")
            self.__log.debug(f"self.__ave_read_time = {self.__ave_read_time}")
            self.__log.debug(f"self.__begin = {self.__begin}")
            self.__log.debug(f"self.__begin_jd = {self.__begin_jd}")
            self.__log.debug(f"self.__delta = {self.__delta}")
            self.__log.debug(f"self.__elapsed_time_jd = {self.__elapsed_time_jd}")
            self.__log.debug(f"self.__end = {self.__end}")
            self.__log.debug(f"self.__end_flats_jd = {self.__end_time_jd}")
            self.__log.debug(f"self.__end_jd = {self.__end_jd}")
            self.__log.debug(f"self.__end_time = {self.__end_time}")
            self.__log.debug(f"self.__end_time_jd = {self.__end_time_jd}")
            self.__log.debug(f"self.__flat_times = {self.__flat_times}")
            self.__log.debug(f'self.__instrument={self.__instrument}')
            self.__log.debug(f'self.__msg={self.__msg}')
            self.__log.debug(f"self.__num_flats = {self.__num_flats}")
            self.__log.debug(f"self.__num_flat_sets = {self.__num_flat_sets}")
            self.__log.debug(f"self.__read_times = {self.__read_times}")
            self.__log.debug(f"self.__seconds = {self.__seconds}")
            self.__log.debug(f"self.__start_flats_jd = {self.__start_flats_jd}")
            self.__log.debug(f'self.__telescope={self.__telescope}')
            self.__log.debug(f'self.__time_per_observation={self.__telescope}')
            self.__log.debug(f'self.__total_exps={self.__total_exps}')
            self.__log.debug(f'self.__total_time={self.__total_time}')

    # +
    # method: calc_num_flats()
    # -
    def calc_num_flats(self):
        """ calculates the number of exposures and time taken """
        self.__total_exps = len(self.__instrument.flat_exposure_times) * len(self.__instrument.readout_times)
        self.__total_time = (self.__ave_flat_time + self.__ave_read_time) * self.__total_exps
        self.__num_flat_sets = int(self.__seconds / self.__total_time)
        return self.__num_flat_sets

    # +
    # method: calculate()
    # -
    def calculate(self, begin=get_isot(0, True), end=jd_to_isot(isot_to_jd(get_isot(0, True))+OBS_ONE_HOUR)):
        """ calculate flat observing schedule """

        # initialize
        self.__begin = begin
        self.__end = end
        self.__begin_jd = isot_to_jd(self.__begin)
        self.__end_jd = isot_to_jd(self.__end)
        self.__seconds = (self.__end_jd - self.__begin_jd) * OBS_SECONDS_PER_DAY
        self.__num_flat_sets = self.calc_num_flats()
        self.__elapsed_time_jd = self.__num_flat_sets * self.__instrument.readout / OBS_SECONDS_PER_DAY
        self.__end_time_jd = self.__begin_jd + self.__elapsed_time_jd
        self.__end_time = jd_to_isot(self.__end_time_jd)
        self.__delta = abs(self.__end_time_jd - self.__end_jd) * OBS_SECONDS_PER_DAY

        # for every filter, take observation in every binning
        if self.__log:
            self.__log.debug(f"Calculating flat observation(s) before {self.__end}")
            self.__log.debug(f"{self.__begin[:-7]} < flat(s) < {self.__end[:-7]}")
            self.__log.debug(f"Verify telescope is opposite sunset/sunrise and dome is open")

        pdh(f"Calculating flat observation(s) before {self.__end}", color='blue')
        pdh(f"{self.__begin[:-7]} < flat(s) < {self.__end[:-7]}", color='blue')
        pdh(f"Verify telescope is opposite sunset/sunrise and dome is open", color='yellow')

        self.__num_flats = 0
        self.__start_flats_jd = self.__begin_jd
        self.__end_flats_jd = self.__end_jd
        for _f in self.__flat_times:
            for _b in self.__read_times:
                self.__time_per_observation = self.__flat_times[_f] + self.__read_times[_b]
                if self.__log:
                    self.__log.debug(f'Filter: {_f}, exposure time={self.__flat_times[_f]}s, '
                                     f'Binning: {_b}, readout time={self.__read_times[_b]}s, '
                                     f'time_per_observation={self.__time_per_observation}s')
                pdh(f"{jd_to_isot(self.__start_flats_jd)[:-7]} observe {self.__num_flat_sets} flat(s) "
                    f"[filter: {_f}, binning: {_b}]")
                self.__num_flats += self.__num_flat_sets
                self.__start_flats_jd += (self.__time_per_observation * self.__num_flat_sets) / OBS_SECONDS_PER_DAY
        self.__delta = (self.__end_flats_jd - self.__start_flats_jd) * OBS_SECONDS_PER_DAY

        if self.__log:
            self.__log.debug(f"{self.__begin[:-7]} observe {self.__num_flats} flat(s)")
            self.__log.debug(f"{self.__end_time[:-7]} finished {self.__num_flats} flats, delta={self.__delta:.1f}s")

        # if we have some time to spare, do some more flats in preferred filter
        if self.__delta > 0.0:
            for _b in self.__read_times:
                self.__time_per_observation = self.__flat_times[self.flat_filter] + self.__read_times[_b]
                if self.__log:
                    self.__log.debug(f"Filter: {self.flat_filter}, "
                                     f"exposure time={self.__flat_times[self.flat_filter]}s, "
                                     f"Binning: {_b}, readout time={self.__read_times[_b]}s, "
                                     f"time_per_observation={self.__time_per_observation}s")
                pdh(f"{jd_to_isot(self.__start_flats_jd)[:-7]} observe {self.__num_flat_sets} flat(s) "
                    f"[filter: {self.flat_filter}, binning: {_b}]", color='red')
                self.__start_flats_jd += (self.__time_per_observation * self.__num_flat_sets) / OBS_SECONDS_PER_DAY
                self.__delta = (self.__end_flats_jd - self.__start_flats_jd) * OBS_SECONDS_PER_DAY
                if self.__delta < 0.0:
                    break

        # return finish time
        return self.__end, self.__end_jd
