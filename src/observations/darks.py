#!/usr/bin/env python3


# +
#  import(s)
# -
from src.observations.obsparams import *


# +
# __doc__
# -
__doc__ = """

  class Darks(ObsParams) - Creates an object to calculate dark observation(s) between limits
  
  Example:
    from src.observations.darks import *
    _l = Logger().logger
    _t = Telescope('Kuiper')
    _i = Instrument('Mont4k')
    _o = Darks(telescope=_t, instrument=_i, log=_l)
    _o.__dump__()
    _o.__darks_dump__()
    _o.calculate()

"""


# +
# class: Darks()
# -
# noinspection PyBroadException,PyUnresolvedReferences
class Darks(ObsParams):
    """ generate dark observation(s) """

    # +
    # method: __init__()
    # -
    def __init__(self, telescope=None, instrument=None, log=None):

        # init super-class
        super().__init__(telescope, instrument, log)

        # initialize other variable(s)
        self.__telescope = self.telescope
        self.__instrument = self.instrument
        self.__log = self.log
        self.__begin = None
        self.__begin_jd = None
        self.__delta = None
        self.__elapsed_time_jd = None
        self.__end = None
        self.__end_jd = None
        self.__end_time = None
        self.__end_time_jd = None
        self.__msg = None
        self.__num_darks = None
        self.__seconds = None

    # +
    # method: __darks_dump__()
    # -
    def __darks_dump__(self, item=None):
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
            self.__log.debug(f"self.__begin = {self.__begin}")
            self.__log.debug(f"self.__begin_jd = {self.__begin_jd}")
            self.__log.debug(f"self.__delta = {self.__delta}")
            self.__log.debug(f"self.__elapsed_time_jd = {self.__elapsed_time_jd}")
            self.__log.debug(f"self.__end = {self.__end}")
            self.__log.debug(f"self.__end_jd = {self.__end_jd}")
            self.__log.debug(f"self.__end_time = {self.__end_time}")
            self.__log.debug(f"self.__end_time_jd = {self.__end_time_jd}")
            self.__log.debug(f'self.__instrument={self.__instrument}')
            self.__log.debug(f'self.__msg={self.__msg}')
            self.__log.debug(f"self.__num_darks = {self.__num_darks}")
            self.__log.debug(f"self.__seconds = {self.__seconds}")
            self.__log.debug(f'self.__telescope={self.__telescope}')

    # +
    # method: calculate()
    # -
    def calculate(self, begin=get_isot(0, True), end=jd_to_isot(isot_to_jd(get_isot(0, True))+OBS_ONE_HOUR)):
        """ calculate dark observing schedule """

        # initialize
        self.__begin = begin
        self.__end = end
        self.__begin_jd = isot_to_jd(self.__begin)
        self.__end_jd = isot_to_jd(self.__end)

        self.__seconds = (self.__end_jd - self.__begin_jd) * OBS_SECONDS_PER_DAY
        self.__num_darks = math.ceil(self.__seconds / INS__READOUT[self.__instrument.name])
        self.__elapsed_time_jd = self.__num_darks * self.__instrument.readout / OBS_SECONDS_PER_DAY
        self.__end_time_jd = self.__begin_jd + self.__elapsed_time_jd
        self.__end_time = jd_to_isot(self.__end_time_jd)
        self.__delta = (self.__end_time_jd - self.__end_jd) * OBS_SECONDS_PER_DAY

        if self.__log:
            self.__log.debug(f"Calculating dark observation(s) before {self.__end}")
            self.__log.debug(f"{self.__begin[:-7]} < dark(s) < {self.__end[:-7]}")
            self.__log.debug(f"Verify telescope is stowed and dome is closed")
            self.__log.debug(f"{self.__begin[:-7]} observe {self.__num_darks} dark(s)")
            self.__log.debug(f"{self.__end_time[:-7]} finished {self.__num_darks} darks, delta={self.__delta:.1f}s")

        pdh(f"Calculating dark observation(s) before {self.__end}", color='blue')
        pdh(f"{self.__begin[:-7]} < dark(s) < {self.__end[:-7]}", color='blue')
        pdh(f"Verify telescope is stowed and dome is closed", color='yellow')
        pdh(f"{self.__begin[:-7]} observe {self.__num_darks} dark(s)")

        # return finish time
        return self.__end, self.__end_jd
