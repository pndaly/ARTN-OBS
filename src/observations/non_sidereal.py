#!/usr/bin/env python3


# +
#  import(s)
# -
from src.models.Models import *
from src.instruments.factory import *
from src.telescopes.factory import *


# +
# __doc__
# -
__doc__ = """

  class NonSidereal(object) - Creates an object to calculate non_sidereal observation(s) between limits
  
  Example:
    from src.observations.non_sidereal import *
    _l = Logger().logger
    _t = Telescope('Kuiper')
    _i = Instrument('Mont4k')
    _o = NonSidereal(telescope=_t, instrument=_i, log=_l)
    _o.__dump__()
    _o.calculate()

"""


# +
# class: NonSidereal()
# -
# noinspection PyBroadException,PyUnresolvedReferences
class NonSidereal(object):
    """ generate focus observation(s) """

    # +
    # class variable(s) - TO BE REMOVED!
    # -
    binning = 'None'   # preferred binning
    cone_angle = 35.0  # preferred cone search
    filter = 'V'       # preferred filter

    # +
    # method: __init__()
    # -
    def __init__(self, telescope=None, instrument=None, log=None):

        # get input(s)
        self.telescope = telescope
        self.instrument = instrument
        self.log = log

        # initialize all variable(s)
        self.__begin = None
        self.__begin_jd = None
        self.__db = None
        self.__dec_min = None
        self.__dec_max = None
        self.__delta = None
        self.__elapsed_seconds = None
        self.__elapsed_time_jd = None
        self.__end = None
        self.__end_non_sidereal_jd = None
        self.__end_jd = None
        self.__end_time = None
        self.__end_time_jd = None
        self.__non_sidereal_utc = None
        self.__non_sidereal_utc_jd = None
        self.__mjd_end = None
        self.__mjd_start = None
        self.__msg = None
        self.__num_non_sidereal = None
        self.__query = None
        self.__request_args = None
        self.__ra_min = None
        self.__ra_max = None
        self.__seconds = None
        self.__start_non_sidereal_jd = None
        self.__target = None
        self.__targets = None
        self.__target_exp_time = None
        self.__target_name = None
        self.__target_num_exp = None
        self.__target_readout = None
        self.__time_per_observation = None
        self.__zenith_dec = None
        self.__zenith_dec_deg = None
        self.__zenith_ra = None
        self.__zenith_ra_deg = None

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
            self.__log.debug(f'self={self}')
            self.__log.debug(f"self.__begin = {self.__begin}")
            self.__log.debug(f"self.__begin_jd = {self.__begin_jd}")
            self.__log.debug(f"self.__delta = {self.__delta}")
            self.__log.debug(f"self.__db = {self.__db}")
            self.__log.debug(f"self.__dec_min = {self.__dec_min}")
            self.__log.debug(f"self.__dec_max = {self.__dec_max}")
            self.__log.debug(f"self.__elapsed_seconds = {self.__elapsed_seconds}")
            self.__log.debug(f"self.__elapsed_time_jd = {self.__elapsed_time_jd}")
            self.__log.debug(f"self.__end = {self.__end}")
            self.__log.debug(f"self.__end_non_sidereal_jd = {self.__end_non_sidereal_jd}")
            self.__log.debug(f"self.__end_jd = {self.__end_jd}")
            self.__log.debug(f"self.__end_time = {self.__end_time}")
            self.__log.debug(f"self.__end_time_jd = {self.__end_time_jd}")
            self.__log.debug(f"self.__non_sidereal_utc = {self.__non_sidereal_utc}")
            self.__log.debug(f"self.__non_sidereal_utc_jd = {self.__non_sidereal_utc_jd}")
            self.__log.debug(f'self.__instrument={self.__instrument}')
            self.__log.debug(f'self.__mjd_end={self.__mjd_end}')
            self.__log.debug(f'self.__mjd_start={self.__mjd_start}')
            self.__log.debug(f'self.__msg={self.__msg}')
            self.__log.debug(f"self.__num_non_sidereal = {self.__num_non_sidereal}")
            self.__log.debug(f'self.__query={self.__query}')
            self.__log.debug(f'self.__request_args={self.__request_args}')
            self.__log.debug(f"self.__ra_min = {self.__ra_min}")
            self.__log.debug(f"self.__ra_max = {self.__ra_max}")
            self.__log.debug(f"self.__seconds = {self.__seconds}")
            self.__log.debug(f"self.__start_non_sidereal_jd = {self.__start_non_sidereal_jd}")
            self.__log.debug(f"self.__target = {self.__target}")
            self.__log.debug(f"self.__targets = {self.__targets}")
            self.__log.debug(f"self.__target_exp_time = {self.__target_exp_time}")
            self.__log.debug(f"self.__target_name = {self.__target_name}")
            self.__log.debug(f"self.__target_num_exp = {self.__target_num_exp}")
            self.__log.debug(f"self.__target_readout = {self.__target_readout}")
            self.__log.debug(f'self.__telescope={self.__telescope}')
            self.__log.debug(f'self.__time_per_observation ={self.__time_per_observation}')
            self.__log.debug(f'self.__zenith_dec={self.__zenith_dec}')
            self.__log.debug(f'self.__zenith_dec_deg={self.__zenith_dec_deg}')
            self.__log.debug(f'self.__zenith_ra={self.__zenith_ra}')
            self.__log.debug(f'self.__zenith_ra_deg={self.__zenith_ra_deg}')

    # +
    # method: calculate()
    # -
    def calculate(self, begin=get_isot(0, True), end=jd_to_isot(isot_to_jd(get_isot(0, True))+OBS_ONE_HOUR)):
        """ calculate focus observing schedule """

        # connect to database
        self.__db = connect_database()()

        # initialize
        self.__begin = begin
        self.__end = end
        self.__begin_jd = isot_to_jd(self.__begin)
        self.__end_jd = isot_to_jd(self.__end)
        self.__seconds = (self.__end_jd - self.__begin_jd) * OBS_SECONDS_PER_DAY
        self.__num_non_sidereal = math.ceil(self.__seconds / INS__READOUT[self.__instrument.name])
        self.__elapsed_time_jd = self.__num_non_sidereal * self.__instrument.readout / OBS_SECONDS_PER_DAY
        self.__end_time_jd = self.__begin_jd + self.__elapsed_time_jd
        self.__end_time = jd_to_isot(self.__end_time_jd)
        self.__delta = (self.__end_time_jd - self.__end_jd) * OBS_SECONDS_PER_DAY

        # calculate some value(s)
        self.__zenith_ra, self.__zenith_dec = self.__telescope.zenith(self.__begin)
        self.__zenith_ra_deg, self.__zenith_dec_deg = ra_to_decimal(self.__zenith_ra), dec_to_decimal(self.__zenith_dec)
        self.__non_sidereal_utc_jd = self.__begin_jd + abs(OBS_UTC_OFFSET/24.0)
        self.__non_sidereal_utc = jd_to_isot(self.__non_sidereal_utc_jd)
        self.__mjd_start = self.__begin_jd - OBS_MJD_OFFSET
        self.__mjd_end = self.__end_jd - OBS_MJD_OFFSET

        if self.__log:
            self.__log.debug(f"self.__zenith_ra={self.__zenith_ra}")
            self.__log.debug(f"self.__zenith_ra_deg={self.__zenith_ra_deg}")
            self.__log.debug(f"self.__zenith_dec={self.__zenith_dec}")
            self.__log.debug(f"self.__zenith_dec_deg={self.__zenith_dec_deg}")
            self.__log.debug(f"self.__dec_min={self.__dec_min}")
            self.__log.debug(f"self.__dec_max={self.__dec_max}")
            self.__log.debug(f"self.__ra_min={self.__ra_min}")
            self.__log.debug(f"self.__ra_max={self.__ra_max}")
            self.__log.debug(f"self.__non_sidereal_utc={self.__non_sidereal_utc}")
            self.__log.debug(f"self.__non_sidereal_utc_jd={self.__non_sidereal_utc_jd}")
            self.__log.debug(f"self.__mjd_start={self.__mjd_start}")
            self.__log.debug(f"self.__mjd_end={self.__mjd_end}")

        # filter query for non_sidereal and make SQL do much of the work ... here's where the Q3C cone search wins!
        self.__query = None
        self.__request_args = {
            'airmass__gte': self.__telescope.min_airmass,
            'airmass__lte': self.__telescope.max_airmass,
            'binning': NonSidereal.binning,
            'begin_mjd__lte': self.__mjd_end,
            'dec_deg__gte': self.__dec_min,
            'dec_deg__lte': self.__dec_max,
            'end_mjd__gte': self.__mjd_start,
            'filter_name': NonSidereal.filter,
            'instrument': self.__instrument.name,
            'ra_deg__gte': self.__ra_min,
            'ra_deg__lte': self.__ra_max,
            'non_sidereal': False,
            'telescope': self.__telescope.name,
            'exclude_username': 'rts2'
        }
        if self.__log:
            self.__log.debug(f"self.request_args={self.__request_args}")

        try:
            self.__query = self.__db.query(ObsReq)
            self.__query = obsreq_filters(query=self.__query, request_args=self.__request_args)
            self.__query = self.__query.order_by(ObsReq.id.desc())
        except:
            if self.__log:
                self.__log.error(f'failed to execute query={self.__query}')
            return self.__end, self.__end_jd

        # save result(s)
        self.__targets = {}
        self.__elapsed_seconds = 0.0
        for _e in ObsReq.serialize_list(self.__query.all()):
            if self.__telescope.is_observable(self.__begin, f"{_e['ra_hms']} {_e['dec_dms']}"):
                if self.__log:
                    self.__log.debug(f"{_e['object_name']} is up and within "
                                     f"RA={NonSidereal.cone_angle}{UNI__DEGREE}, "
                                     f"Dec={NonSidereal.cone_angle}{UNI__DEGREE} of zenith")
                if _e['binning'] not in self.__targets:
                    self.__targets[f"{_e['binning']}"] = [_e]
                else:
                    self.__targets[_e['binning']].append(_e)
        self.__num_non_sidereal = len(self.__targets)

        if self.__log:
            self.__log.debug(f"Calculating non_sidereal observation(s) before {self.__end}")
            self.__log.debug(f"{self.__begin[:-7]} < non_sidereal < {self.__end[:-7]}")
            self.__log.debug(f"Verify telescope is ready and dome is open")

        pdh(f"Calculating non_sidereal observation(s) before {self.__end}", color='blue')
        pdh(f"{self.__begin[:-7]} < non_sidereal < {self.__end[:-7]}", color='blue')
        pdh(f"Verify telescope is ready and dome is open", color='yellow')

        # refine target(s)
        # >>>>> 00TODO00 <<<<<<
        # self.__num_non_sidereal = 0
        # self.__start_non_sidereal_jd = self.__begin_jd
        # self.__end_non_sidereal_jd = self.__end_jd
        # for _t in self.__targets:
        #     self.__target = random.choice(self.__targets[_t])
        #     self.__target_name = self.__target['object_name']
        #     self.__target_exp_time = self.__target['exp_time']
        #     self.__target_num_exp = self.__target['num_exp']
        #     self.__target_readout = self.__instrument.readout_times[_t]
        #     self.__time_per_observation = (self.__target_exp_time + self.__target_readout) * self.__target_num_exp
        #     if self.__log:
        #         self.__log.debug(f'filter: {NonSidereal.filter}, '
        #                          f'exp_time={self.__target_exp_time}s, '
        #                          f'num_exp={self.__target_num_exp}, '
        #                          f'binning: {_t}, '
        #                          f'readout time={self.__instrument.readout_times[_t]}s, '
        #                          f'time_per_observation={self.__time_per_observation}s')
        #     pdh(f"{jd_to_isot(self.__start_non_sidereal_jd)[:-7]} observe {self.__target_num_exp} non_sidereal "
        #         f"[{self.__target_name} filter: {NonSidereal.filter}, binning: {_t}]")
        #     self.__start_non_sidereal_jd += self.__time_per_observation / OBS_SECONDS_PER_DAY
        # self.__delta = (self.__end_non_sidereal_jd - self.__start_non_sidereal_jd) * OBS_SECONDS_PER_DAY

        # if self.__log:
        #     self.__log.debug(f"{self.__begin[:-7]} observe {self.__num_non_sidereal} non_sidereal")
        #     self.__log.debug(f"{self.__end_time[:-7]} finished {self.__num_non_sidereal} non_sidereal, delta={self.__delta:.1f}s")

        # disconnect database
        disconnect_database(self.__db)

        # return finish time
        return self.__end, self.__end_jd

    # is the airmass within limits?
    # is it non-sidereal?
    # query = obsreq_filters(query, {'non-sidereal': False})
    # has it been observed within the last n days?
    # query = obsreq_filters(query, {'completed_mjd__lte': _mjd})
    # query = obsreq_filters(query, {'completed_mjd__gte': _mjd-60.0})
    # is it in the sky within the next n hours (has it risen / set)
    # is the moonphase ok
    # is the moon exclusion ok
