#!/usr/bin/env python3


# +
# import(s)
# -
from src import *
from src.telescopes import *

from astroplan import Observer
from astroplan import FixedTarget
from astropy.coordinates import AltAz
from astropy.coordinates import EarthLocation
from astropy.coordinates import get_moon
from astropy.coordinates import get_sun

import astropy
import math
import numpy as np
import unicodedata


# +
# constant(s)
# -
AST__4__MINUTES = 360
AST__5__MINUTES = 289
AST__EAST = 90.0
AST__HORIZON = 0.0
AST__NADIR = -90.0
AST__NORTH = 0.0
AST__PHASE = ['new', 'first quarter', 'full', 'last quarter']
AST__SOUTH = 180.0
AST__TWILIGHT = ['astronomical', 'civil', 'nautical']
AST__WEST = 270.0
AST__WHICH = ['next', 'previous', 'nearest']
AST__ZENITH = 90.0
MAX__ALTITUDE = 8000.0
MAX__DECLINATION = 90.0
MAX__LATITUDE = 90.0
MAX__LONGITUDE = 360.0
MAX__RIGHT__ASCENSION = 360.0
MIN__ALTITUDE = 0.0
MIN__DECLINATION = -90.0
MIN__LATITUDE = -90.0
MIN__LONGITUDE = -360.0
MIN__NDAYS = 1
MIN__RIGHT__ASCENSION = 0.0
MOON__CIVIL = {0: 'new', 1: 'waxing crescent', 2: 'first quarter', 3: 'waxing gibbous',
               4: 'full', 5: 'waning gibbous', 6: 'last quarter', 7: 'waning crescent'}
MOON__ILLUM = [0.0, 25.0, 50.0, 75.0, 100.0, 75.0, 50.0, 25.0]
MOON__PHASE = [math.pi, 3.0*math.pi/4.0, math.pi/2.0, math.pi/4.0,
               0.0, math.pi/4.0, math.pi/2.0, 3.0*math.pi/4.0]
VAL__NOT__OBSERVABLE = 0.0
VAL__OBSERVABLE = 1.0
UNI__DEGREE = unicodedata.lookup('DEGREE SIGN')
UNI__ARCMIN = unicodedata.lookup('PRIME')
UNI__ARCSEC = unicodedata.lookup('DOUBLE PRIME')
UNI__PROPORTIONAL = unicodedata.lookup('PROPORTIONAL TO')


# +
# (factory) class: Telescope()
# -
# noinspection PyBroadException,PyUnresolvedReferences,PyTypeChecker
class Telescope(object):

    # +
    # method: __init__
    # -
    def __init__(self, name='', log=None):

        # get input(s)
        self.name = name
        self.log = log

        # set default(s)
        self.__msg = None
        self.__aka = TEL__AKA[self.__name]
        self.__altitude = TEL__ALTITUDE[self.__name]
        self.__astronomical_dawn = TEL__ASTRONOMICAL__DAWN[self.__name]
        self.__astronomical_dusk = TEL__ASTRONOMICAL__DUSK[self.__name]
        self.__civil_dawn = TEL__CIVIL__DAWN[self.__name]
        self.__civil_dusk = TEL__CIVIL__DUSK[self.__name]
        self.__dec_limit = TEL__DEC__LIMIT[self.__name]
        self.__dome_slew_rate = TEL__DOME__SLEW__RATE[self.__name]
        self.__latitude = TEL__LATITUDE[self.__name]
        self.__longitude = TEL__LONGITUDE[self.__name]
        self.__max_moonex = TEL__MAX__MOONEX[self.__name]
        self.__max_airmass = TEL__MAX__AIRMASS[self.__name]
        self.__min_moonex = TEL__MIN__MOONEX[self.__name]
        self.__min_airmass = TEL__MIN__AIRMASS[self.__name]
        self.__nautical_dawn = TEL__NAUTICAL__DAWN[self.__name]
        self.__nautical_dusk = TEL__NAUTICAL__DUSK[self.__name]
        self.__slew_rate = TEL__SLEW__RATE[self.__name]
        self.__supported = TEL__SUPPORTED[self.__name]

        self.__observatory = EarthLocation(
            lat=self.__latitude * u.deg, lon=self.__longitude * u.deg, height=self.__altitude * u.m)
        self.__observer = Observer(location=self.__observatory, name=self.__name, timezone='US/Arizona')

    # +
    # class method: telescope()
    # -
    @classmethod
    def telescope(cls, name='', log=None):
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
        self.__name = name if (isinstance(name, str) and name in TEL__TELESCOPES) else TEL__TELESCOPES[0]

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log=None):
        self.__log = log if isinstance(log, logging.Logger) else None

    # +
    # getter(s) with no setter(s)
    # -
    @property
    def observer(self):
        return self.__observer

    @property
    def observatory(self):
        return self.__observatory

    @property
    def aka(self):
        return self.__aka

    @property
    def altitude(self):
        return float(self.__altitude)

    @property
    def astronomical_dawn(self):
        return float(self.__astronomical_dawn)

    @property
    def astronomical_dusk(self):
        return float(self.__astronomical_dusk)

    @property
    def civil_dawn(self):
        return float(self.__civil_dawn)

    @property
    def civil_dusk(self):
        return float(self.__civil_dusk)

    @property
    def dec_limit(self):
        return float(self.__dec_limit)

    @property
    def dome_slew_rate(self):
        return float(self.__dome_slew_rate)

    @property
    def latitude(self):
        return float(self.__latitude)

    @property
    def longitude(self):
        return float(self.__longitude)

    @property
    def max_moonex(self):
        return float(self.__max_moonex)

    @property
    def max_airmass(self):
        return float(self.__max_airmass)

    @property
    def min_moonex(self):
        return float(self.__min_moonex)

    @property
    def min_airmass(self):
        return float(self.__min_airmass)

    @property
    def nautical_dawn(self):
        return float(self.__nautical_dawn)

    @property
    def nautical_dusk(self):
        return float(self.__nautical_dusk)

    @property
    def slew_rate(self):
        return float(self.__slew_rate)

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

    # +
    # method: dawn()
    # -
    def dawn(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False):
        """ returns dawn time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        twilight = twilight.lower() if twilight.lower() in AST__TWILIGHT else AST__TWILIGHT[0]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            _date, _jd = None, math.nan
            _a_horizon = TEL__ASTRONOMICAL__DAWN[self.__name]*u.degree
            _c_horizon = TEL__CIVIL__DAWN[self.__name]*u.degree
            _n_horizon = TEL__NAUTICAL__DAWN[self.__name]*u.degree
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _date = obs_time
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _date = Time(obs_time)
            if twilight == 'astronomical':
                _jd = self.observer.sun_rise_time(_date, which=which, horizon=_a_horizon).jd
            elif twilight == 'civil':
                _jd = self.observer.sun_rise_time(_date, which=which, horizon=_c_horizon).jd
            elif twilight == 'nautical':
                _jd = self.observer.sun_rise_time(_date, which=which, horizon=_n_horizon).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: dusk()
    # -
    def dusk(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False):
        """ returns dusk time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        twilight = twilight.lower() if twilight.lower() in AST__TWILIGHT else AST__TWILIGHT[0]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            _date, _jd = None, math.nan
            _a_horizon = TEL__ASTRONOMICAL__DUSK[self.__name]*u.degree
            _c_horizon = TEL__CIVIL__DUSK[self.__name]*u.degree
            _n_horizon = TEL__NAUTICAL__DUSK[self.__name]*u.degree
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _date = obs_time
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _date = Time(obs_time)
            if twilight == 'astronomical':
                _jd = self.observer.sun_set_time(_date, which=which, horizon=_a_horizon).jd
            elif twilight == 'civil':
                _jd = self.observer.sun_set_time(_date, which=which, horizon=_c_horizon).jd
            elif twilight == 'nautical':
                _jd = self.observer.sun_set_time(_date, which=which, horizon=_n_horizon).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: is_day()
    # -
    def is_day(self, obs_time=Time(get_isot(0, True))):
        """ returns flag to represent daytime """
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return False if self.__observer.is_night(obs_time) else True
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return False if self.__observer.is_night(Time(obs_time)) else True
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: is_night()
    # -
    def is_night(self, obs_time=Time(get_isot(0, True))):
        """ returns flag to represent nighttime """
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.__observer.is_night(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.__observer.is_night(Time(obs_time))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: is_observable()
    # -
    def is_observable(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ return boolean for observability of target """

        # get coordinates by name or Ra, Dec
        if isinstance(obs_name, str) and obs_name.strip() != '':
            _obs_coords = FixedTarget.from_name(obs_name)
        elif isinstance(obs_coords, str) and obs_coords.strip() != '':
            _ra, _dec = obs_name.split()
            _ra = f'{_ra} hours' if 'hours' not in _ra.lower() else _ra
            _dec = f'{_dec} degrees' if 'degrees' not in _dec.lower() else _dec
            _obs_coords = SkyCoord(f"{_ra}", f"{_dec}")
        else:
            return None

        # is it above the horizon?
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.__observer.target_is_up(obs_time, target=_obs_coords)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.__observer.target_is_up(Time(obs_time), target=_obs_coords)
        except:
            if self.__log:
                self.__log.error(f'unable to convert name')
        return None

    # +
    # function: lst()
    # -
    def lst(self, obs_time=Time(get_isot(0, True))):
        """ returns local sidereal time """
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _lst_h, _lst_m, _lst_s = self.observer.local_sidereal_time(obs_time).hms
                return f'{int(_lst_h):02d}:{int(_lst_m):02d}:{float(_lst_s):06.3f}'
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _lst_h, _lst_m, _lst_s = self.observer.local_sidereal_time(Time(obs_time)).hms
                return f'{int(_lst_h):02d}:{int(_lst_m):02d}:{float(_lst_s):06.3f}'
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: midday()
    # -
    def midday(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns sun noon time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _jd = self.observer.noon(obs_time, which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _jd = self.observer.noon(Time(obs_time), which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: midnight()
    # -
    def midnight(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns sun midnight time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _jd = self.observer.midnight(obs_time, which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _jd = self.observer.midnight(Time(obs_time), which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_alt()
    # -
    def moon_alt(self, obs_time=Time(get_isot(0, True))):
        """ returns moon alt """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.moon_altaz(obs_time).alt.value
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.moon_altaz(Time(obs_time)).alt.value
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: moon_az()
    # -
    def moon_az(self, obs_time=Time(get_isot(0, True))):
        """ returns moon az """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.moon_altaz(obs_time).az.value
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.moon_altaz(Time(obs_time)).az.value
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: moon_civil()
    # -
    def moon_civil(self, obs_time=get_isot(0, True)):
        """ returns moon phase for civilians """

        # check input(s)
        if re.match(OBS_ISO_PATTERN, obs_time) is None:
            return None

        # return value or none
        try:
            _now_jd = isot_to_jd(obs_time)
            # find nearest new moon
            _near_jd = isot_to_jd(self.moon_date(obs_time=obs_time, which='nearest', phase='new'))
            # if we're within half a day either side, return
            if _near_jd-0.5 <= _now_jd <= _near_jd+0.5:
                return 'new'
            # get start
            _start_jd = _near_jd
            if _now_jd <= _near_jd:
                _start_jd = isot_to_jd(self.moon_date(obs_time=obs_time, which='previous', phase='new'))
            _start = jd_to_isot(_start_jd)
            # derive some data structure(s)
            _isots = {_v: self.moon_date(obs_time=_start, which='next', phase=_v) for _v in AST__PHASE}
            _jds = {_k: isot_to_jd(_v) for _k, _v in _isots.items()}
            _isots_r, _jds_r = {_v: _k for _k, _v in _isots.items()}, {_v: _k for _k, _v in _jds.items()}
            # get key
            _val = nearest(list(_jds.values()), _now_jd)
            _key = _jds_r.get(_val, None)
            # return result
            if _key is not None:
                if (_jds[_key]-0.5) <= _now_jd <= (_jds[_key]+0.5):
                    return _key
                _x = {_j: _i for _i, _j in MOON__CIVIL.items()}.get(_key, None)
                if _x is not None and isinstance(_x, int):
                    _x = _x + 1 if _now_jd > _jds[_key] else _x - 1
                    return MOON__CIVIL[_x % len(MOON__CIVIL)]
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_coord()
    # -
    def moon_coord(self, obs_time=Time(get_isot(0, True))):
        """ returns moon alt, az and distance as SkyCoord """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.moon_altaz(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.moon_altaz(Time(obs_time))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_date()
    # -
    def moon_date(self, obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__PHASE[0], utc=False):
        """ returns moon date for phase """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        phase = phase.lower() if phase.lower() in AST__PHASE else AST__PHASE[0]
        utc = utc if isinstance(utc, bool) else False

        # set default(s)
        _jd, _nfm_jd, _nfqm_jd, _nlqm_jd, _nnm_jd = math.nan, math.nan, math.nan, math.nan, math.nan
        _ans, _pfm_jd, _pfqm_jd, _plqm_jd, _pnm_jd = math.nan, math.nan, math.nan, math.nan, math.nan

        # return result
        try:
            _date = isot_to_ephem(obs_time)
            _jd = isot_to_jd(obs_time)
            if which == 'nearest' and phase == 'new':
                _nnm = isot_to_jd(ephem_to_isot(ephem.next_new_moon(_date)))
                _pnm = isot_to_jd(ephem_to_isot(ephem.previous_new_moon(_date)))
                _ans = _nnm if ((_jd - _pnm) > (_nnm - _jd)) else _pnm
            elif which == 'nearest' and phase == 'first quarter':
                _nfqm = isot_to_jd(ephem_to_isot(ephem.next_first_quarter_moon(_date)))
                _pfqm = isot_to_jd(ephem_to_isot(ephem.previous_first_quarter_moon(_date)))
                _ans = _nfqm if ((_jd - _pfqm) > (_nfqm - _jd)) else _pfqm
            elif which == 'nearest' and phase == 'full':
                _nfm = isot_to_jd(ephem_to_isot(ephem.next_full_moon(_date)))
                _pfm = isot_to_jd(ephem_to_isot(ephem.previous_full_moon(_date)))
                _ans = _nfm if ((_jd - _pfm) > (_nfm - _jd)) else _pfm
            elif which == 'nearest' and phase == 'last quarter':
                _nlqm = isot_to_jd(ephem_to_isot(ephem.next_last_quarter_moon(_date)))
                _plqm = isot_to_jd(ephem_to_isot(ephem.previous_last_quarter_moon(_date)))
                _ans = _nlqm if ((_jd - _plqm) > (_nlqm - _jd)) else _plqm
            elif which == 'next' and phase == 'new':
                _ans = isot_to_jd(ephem_to_isot(ephem.next_new_moon(_date)))
            elif which == 'next' and phase == 'first quarter':
                _ans = isot_to_jd(ephem_to_isot(ephem.next_first_quarter_moon(_date)))
            elif which == 'next' and phase == 'full':
                _ans = isot_to_jd(ephem_to_isot(ephem.next_full_moon(_date)))
            elif which == 'next' and phase == 'last quarter':
                _ans = isot_to_jd(ephem_to_isot(ephem.next_last_quarter_moon(_date)))
            elif which == 'previous' and phase == 'new':
                _ans = isot_to_jd(ephem_to_isot(ephem.previous_new_moon(_date)))
            elif which == 'previous' and phase == 'first quarter':
                _ans = isot_to_jd(ephem_to_isot(ephem.previous_first_quarter_moon(_date)))
            elif which == 'previous' and phase == 'full':
                _ans = isot_to_jd(ephem_to_isot(ephem.previous_full_moon(_date)))
            elif which == 'previous' and phase == 'last quarter':
                _ans = isot_to_jd(ephem_to_isot(ephem.previous_last_quarter_moon(_date)))
            return jd_to_isot(_ans) if utc else jd_to_isot(_ans - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_distance()
    # -
    def moon_distance(self, obs_time=Time(get_isot(0, True))):
        """ returns moon distance """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.moon_altaz(obs_time).distance.value
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.moon_altaz(Time(obs_time)).distance.value
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: moon_illumination()
    # -
    def moon_illumination(self, obs_time=Time(get_isot(0, True))):
        """ returns moon illumination fraction """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.moon_illumination(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.moon_illumination(Time(obs_time))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: moon_is_up()
    # -
    def moon_is_up(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg):
        """ returns True if moon has risen """

        # get position
        moon_alt = math.nan
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                moon_alt = self.observer.moon_alt(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                moon_alt = self.observer.moon_alt(Time(obs_time))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
            return None
        else:
            return None if moon_alt is math.nan else bool(moon_alt < horizon)

    # +
    # method: moon_lunation()
    # -
    def moon_lunation(self, obs_time=get_isot(0, True)):
        """ returns moon lunation in days """

        # return result
        try:
            _date = isot_to_ephem(obs_time)
            _nnm = isot_to_jd(ephem_to_isot(ephem.next_new_moon(_date)))
            _pnm = isot_to_jd(ephem_to_isot(ephem.previous_new_moon(_date)))
            return _nnm - _pnm
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_phase()
    # -
    def moon_phase(self, obs_time=Time(get_isot(0, True))):
        """ returns moon phase fraction """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.moon_phase(obs_time).value
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.moon_phase(Time(obs_time)).value
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: moon_rise()
    # -
    def moon_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns moonrise time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _jd = self.observer.moon_rise_time(obs_time, which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _jd = self.observer.moon_rise_time(Time(obs_time), which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_set()
    # -
    def moon_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns moonset time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _jd = self.observer.moon_set_time(obs_time, which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _jd = self.observer.moon_set_time(Time(obs_time), which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_steward()
    # -
    def moon_steward(self, obs_time=get_isot(0, True)):
        """ returns moon phase for steward observatory """

        # check input(s)
        if re.match(OBS_ISO_PATTERN, obs_time) is None:
            return None

        # return value or none
        try:
            _near_jd = isot_to_jd(self.moon_date(obs_time=obs_time, which='nearest', phase='new'))
            _diff = isot_to_jd(obs_time) - _near_jd
            if abs(_diff) < 5.5:
                return _diff, 'dark'
            elif 5.5 <= abs(_diff) <= 8.5:
                return _diff, 'grey'
            else:
                return _diff, 'bright'
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: observing_end()
    # -
    def observing_end(self, obs_time=Time(get_isot(0, True)), utc=False):
        """ returns isot of end of observing night """

        # reset input(s)
        utc = utc if isinstance(utc, bool) else False

        # return result
        _date = None
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _date = self.__observer.tonight(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _date = self.__observer.tonight(Time(obs_time))
            return jd_to_isot(_date[1].jd if utc else (_date[1].jd - abs(OBS_UTC_OFFSET/24.0)))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: observing_start()
    # -
    def observing_start(self, obs_time=Time(get_isot(0, True)), utc=False):
        """ returns isot of start of observing night """

        # reset input(s)
        utc = utc if isinstance(utc, bool) else False

        # return result
        _date = None
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _date = self.__observer.tonight(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _date = self.__observer.tonight(Time(obs_time))
            return jd_to_isot(_date[0].jd if utc else (_date[0].jd - abs(OBS_UTC_OFFSET/24.0)))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: radec_to_altaz()
    # -
    def radec_to_altaz(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ return Alt, Az for RA, Dec """

        # get coordinates by name or Ra, Dec
        if isinstance(obs_name, str) and obs_name.strip() != '':
            _obs_coords = FixedTarget.from_name(obs_name)
        elif isinstance(obs_coords, str) and obs_coords.strip() != '':
            _ra, _dec = obs_coords.split()
            _ra = f'{_ra} hours' if 'hours' not in _ra.lower() else _ra
            _dec = f'{_dec} degrees' if 'degrees' not in _dec.lower() else _dec
            _obs_coords = SkyCoord(f"{_ra}", f"{_dec}")
        else:
            return None

        # is it above the horizon?
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.__observer.altaz(obs_time, target=_obs_coords)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.__observer.altaz(Time(obs_time), target=_obs_coords)
        except:
            if self.__log:
                self.__log.error(f'unable to convert name')
        return None

    # +
    # method: sun_alt()
    # -
    def sun_alt(self, obs_time=Time(get_isot(0, True))):
        """ returns sun alt """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.sun_altaz(obs_time).alt.value
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.sun_altaz(Time(obs_time)).alt.value
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: sun_az()
    # -
    def sun_az(self, obs_time=Time(get_isot(0, True))):
        """ returns sun az """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.sun_altaz(obs_time).az.value
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.sun_altaz(Time(obs_time)).az.value
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return math.nan

    # +
    # method: sun_coord()
    # -
    def sun_coord(self, obs_time=Time(get_isot(0, True))):
        """ returns sun alt, az and distance as SkyCoord """

        # return value or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                return self.observer.sun_altaz(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                return self.observer.sun_altaz(Time(obs_time))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: sun_rise()
    # -
    def sun_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns sunrise time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _jd = self.observer.sun_rise_time(obs_time, which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _jd = self.observer.sun_rise_time(Time(obs_time), which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: sun_set()
    # -
    def sun_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns sunset time """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        utc = utc if isinstance(utc, bool) else False

        # return isot string or none
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _jd = self.observer.sun_set_time(obs_time, which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _jd = self.observer.sun_set_time(Time(obs_time), which=which).jd
                return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(OBS_UTC_OFFSET/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: tonight()
    # -
    def tonight(self, obs_time=Time(get_isot(0, True)), utc=False):
        """ returns isot(s) of observing night """

        # reset input(s)
        utc = utc if isinstance(utc, bool) else False

        # return result
        _date = None
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                _date = self.__observer.tonight(obs_time)
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                _date = self.__observer.tonight(Time(obs_time))
            _start = jd_to_isot(_date[0].jd if utc else (_date[0].jd - abs(OBS_UTC_OFFSET/24.0)))
            _end = jd_to_isot(_date[1].jd if utc else (_date[1].jd - abs(OBS_UTC_OFFSET/24.0)))
            return _start, _end
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # function: zenith()
    # -
    def zenith(self, obs_time=Time(get_isot(0, True))):
        """ returns RA, Dec of zenith """
        try:
            _ra = self.lst(obs_time=obs_time)
            _dec = dec_from_decimal(TEL__LATITUDE[self.name])
            return _ra, _dec
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None, None

    # +
    # +
    # method: airmass_plot()
    # -
    def airmass_plot(self, _ra=MIN__RIGHT__ASCENSION, _dec=MIN__DECLINATION, _date=get_isot(0, True),
                     _ndays=MIN__NDAYS, _from_now=False):
        """ returns an image of airmass for object for several days """

        # check input(s)
        # _ra = _ra if isinstance(_ra, float) else MIN__RIGHT__ASCENSION
        # _ra = _ra if _ra > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
        # _ra = _ra if _ra < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
        # _dec = _dec if isinstance(_dec, float) else MIN__DECLINATION
        # _dec = _dec if _dec > MIN__DECLINATION else MIN__DECLINATION
        # _dec = _dec if _dec < MAX__DECLINATION else MAX__DECLINATION
        # _date = _date if re.match(OBS_ISO_PATTERN, _date) is not None else get_isot(0, True)
        # _ndays = _ndays if isinstance(_ndays, int) else MIN__NDAYS
        # _ndays = _ndays if _ndays > 0 else MIN__NDAYS
        # _from_now = _from_now if isinstance(_from_now, bool) else False
        #
        # # set default(s)
        # _time_now = Time.now()
        # if 'T' in _date:
        #     _start = Time(_date) if _from_now else Time(_date.split('T')[0])
        # else:
        #     _start = Time(_date) if _from_now else Time(_date.split()[0])
        # _now = Time(_start.iso)
        # _start = Time(_start.iso)
        # _start = Time(_start) + (_ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES))
        # _title = f"Airmass [{_ndays} Day(s)]"
        #
        # _ra_hms = Angle(_ra, unit=u.deg).hms
        # _HH, _MM, _SS = _ra_hms[0], _ra_hms[1], _ra_hms[2]
        # _sign = '-' if str(_dec)[0] == '-' else '+'
        # _dec_dms = Angle(_dec, unit=u.deg).dms
        # _dd, _mm, _ss = abs(_dec_dms[0]), abs(_dec_dms[1]), abs(_dec_dms[2])
        # _sub_title = f"RA={int(_HH):02d}:{int(_MM):02d}:{int(_SS):02d} ({_ra:.3f}{UNI__DEGREE}), " \
        #              f"Dec={_sign}{int(_dd):02d}{UNI__DEGREE}{int(_mm):02d}{UNI__ARCMIN}{int(_ss):02d}{UNI__ARCSEC} " \
        #              f"({_dec:.3f}{UNI__DEGREE})"
        #
        # # modify to reference frame and get airmass
        # _frame = AltAz(obstime=_start, location=self.__observatory)
        # _radecs = SkyCoord(ra=_ra*u.deg, dec=_dec*u.deg)
        # _altaz = _radecs.transform_to(_frame)
        #
        # # extract axes
        # _max_airmass = TEL__MAX__AIRMASS[f'{self.__name.lower()}']
        # _min_airmass = TEL__MIN__AIRMASS[f'{self.__name.lower()}']
        # _time_axis = _start[(_altaz.secz <= _max_airmass) & (_altaz.secz >= _min_airmass)]
        # _airmass_axis = _altaz.secz[(_altaz.secz <= _max_airmass) & (_altaz.secz >= _min_airmass)]
        #
        # # plot it
        # fig, ax = plt.subplots()
        # ax.plot_date(_time_axis.plot_date, _airmass_axis, 'r-')
        # ax.plot_date([_time_now.plot_date, _time_now.plot_date], [-999, 999], 'y--')
        # xfmt = mdates.DateFormatter('%H:%M')
        # ax.xaxis.set_major_formatter(xfmt)
        # plt.gcf().autofmt_xdate()
        # ax.set_ylim([_max_airmass, _min_airmass])
        # ax.set_xlim([_start.datetime[0], _start.datetime[-1]])
        # ax.set_title(f'{_title}\n{_sub_title}')
        # ax.set_ylabel(f'Airmass ({UNI__PROPORTIONAL} secZ)')
        # ax.set_xlabel(f"{str(_now).split()[0]} (UTC)")
        # buf = io.BytesIO()
        # # plt.savefig(f'{_file}')
        # plt.savefig(buf, format='png', dpi=100)
        # plt.close()
        # data = buf.getvalue()
        data = self.__name
        return f'data:image/png;base64,{base64.b64encode(data).decode()}'

    # +
    # method: moon_coordinates()
    # -
    def moon_coordinates(self, date=get_isot(0, True), ndays=MIN__NDAYS, from_now=False):
        """ returns an array of (ra, dec, distance) for moon over several days """

        # check input(s)
        date = date if re.match(OBS_ISO_PATTERN, date) is not None else get_isot(0, True)
        ndays = ndays if isinstance(ndays, int) else MIN__NDAYS
        ndays = ndays if ndays > 0 else MIN__NDAYS
        from_now = from_now if isinstance(from_now, bool) else False

        # set default(s)
        _time = Time(date) if from_now else Time(date.split()[0])
        _time = Time(_time.iso)
        _time = Time(_time) + (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))

        # noinspection PyBroadException
        try:
            return get_moon(_time, location=self.__observatory)
        except Exception:
            return None

    # +
    # method: moon_coordinates_now()
    # -
    def moon_coordinates_now(self):
        """ returns (ra, dec, distance) for moon now """
        return self.moon_coordinates(f'{get_isot(0, True)}', ndays=1, from_now=True)[0]

    # +
    # method: moon_coordinates_today()
    # -
    def moon_coordinates_today(self):
        """ returns (ra, dec, distance) for moon now """
        return self.moon_coordinates(f'{get_isot(0, True)}', ndays=1, from_now=False)

    # +
    # method: moon_exclusion()
    # -
    def moon_exclusion(self, date=get_isot(0, True), ndays=MIN__NDAYS, from_now=False):
        """ returns an array of moon exclusion angles from object for several days """

        # check input(s)
        date = date if re.match(OBS_ISO_PATTERN, date) is not None else get_isot(0, True)
        ndays = ndays if isinstance(ndays, int) else MIN__NDAYS
        ndays = ndays if ndays > 0 else MIN__NDAYS
        from_now = from_now if isinstance(from_now, bool) else False

        # set default(s)
        _excl = None
        _time = Time(date) if from_now else Time(date.split()[0])
        _time = Time(_time.iso)
        _time = Time(_time) + (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))

        _moon_lower = TEL__MIN__MOONEX[f'{self.__name.lower()}']
        _moon_upper = TEL__MAX__MOONEX[f'{self.__name.lower()}'] - _moon_lower

        # get illumination and moon alt-az for time
        _illuminati = self.__observer.moon_illumination(_time)
        _lunar_altaz = self.__observer.moon_altaz(_time)

        # noinspection PyBroadException
        try:
            for _i in range(len(_lunar_altaz)):
                if _lunar_altaz[_i].alt <= 0:
                    # noinspection PyUnresolvedReferences
                    _illuminati[_i] = 0.0
            _excl = (_moon_lower + _moon_upper * _illuminati)
        except Exception:
            _excl = ndays * np.linspace(math.nan, math.nan, AST__5__MINUTES*ndays)

        # return result
        return _excl

    # +
    # method: moon_exclusion_now()
    # -
    def moon_exclusion_now(self):
        """ returns the value of the moon exclusion angle from object right now """
        return self.moon_exclusion(f'{get_isot(0, True)}', ndays=1, from_now=True)[0]

    # +
    # method: moon_exclusion_today()
    # -
    def moon_exclusion_today(self):
        """ returns an array of moon exclusion angles from object for today """
        return self.moon_exclusion(f'{get_isot(0, True)}', ndays=1, from_now=False)

    # +
    # method: moon_separation()
    # -
    def moon_separation(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION, date=get_isot(0, True),
                        ndays=MIN__NDAYS, from_now=False):
        """ returns an array of moon separation angles from object for several days """

        # check input(s)
        ra = ra if isinstance(ra, float) else MIN__RIGHT__ASCENSION
        ra = ra if ra > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
        ra = ra if ra < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
        dec = dec if isinstance(dec, float) else MIN__DECLINATION
        dec = dec if dec > MIN__DECLINATION else MIN__DECLINATION
        dec = dec if dec < MAX__DECLINATION else MAX__DECLINATION
        date = date if re.match(OBS_ISO_PATTERN, date) is not None else get_isot(0, True)
        ndays = ndays if isinstance(ndays, int) else MIN__NDAYS
        ndays = ndays if ndays > 0 else MIN__NDAYS
        from_now = from_now if isinstance(from_now, bool) else False

        # set default(s)
        _sep = None
        _time = Time(date) if from_now else Time(date.split()[0])
        _time = Time(_time.iso)
        _time = Time(_time) + (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))

        # noinspection PyBroadException
        try:
            _moon_coord = get_moon(_time, location=self.__observatory)
            _obj_radec = SkyCoord(ra=ra * u.deg, dec=dec * u.deg)
            _sep = _obj_radec.separation(_moon_coord).deg
        except Exception:
            _sep = ndays * np.linspace(math.nan, math.nan, AST__5__MINUTES*ndays)

        # return array
        return _sep

    # +
    # method: moon_separation_now()
    # -
    def moon_separation_now(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
        """ returns the value of the moon separation angle from object right now """
        return self.moon_separation(ra, dec, f'{get_isot(0, True)}', ndays=1, from_now=True)[0]

    # +
    # method: moon_separation_today()
    # -
    def moon_separation_today(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
        """ returns an array of moon separation angles from object for today """
        return self.moon_separation(ra, dec, f'{get_isot(0, True)}', ndays=1, from_now=False)

    # +
    # (override) method: observe()
    # -
    def observe(self, **kwargs):
        if not self.__simulation:
            if self.__log:
                self.__log.debug(f'called self.observer(), kwargs={kwargs}')

    # +
    # method: observable()
    # -
    def observable(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION, date=get_isot(0, True),
                   ndays=MIN__NDAYS, from_now=False):
        """ returns an array of observability flags for object for several days """

        # check input(s)
        ra = ra if isinstance(ra, float) else MIN__RIGHT__ASCENSION
        ra = ra if ra > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
        ra = ra if ra < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
        dec = dec if isinstance(dec, float) else MIN__DECLINATION
        dec = dec if dec > MIN__DECLINATION else MIN__DECLINATION
        dec = dec if dec < MAX__DECLINATION else MAX__DECLINATION
        date = date if re.match(OBS_ISO_PATTERN, date) is not None else get_isot(0, True)
        ndays = ndays if isinstance(ndays, int) else MIN__NDAYS
        ndays = ndays if ndays > 0 else MIN__NDAYS
        from_now = from_now if isinstance(from_now, bool) else False

        # set default(s)
        _obs = np.linspace(math.nan, math.nan, AST__5__MINUTES*ndays)
        _time = Time(date) if from_now else Time(date.split()[0])
        _time = Time(_time.iso)

        # get arrays for moon exclusion, separation and UTC time
        _mex = self.moon_exclusion(date=_time.iso, ndays=ndays, from_now=from_now)
        _msp = self.moon_separation(ra=ra, dec=dec, date=_time.iso, ndays=ndays, from_now=from_now)
        _time = Time(_time) + (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))

        # modify to reference frame and get solar position
        _frame = AltAz(obstime=_time, location=self.__observatory)
        _radecs = SkyCoord(ra=ra * u.deg, dec=dec * u.deg)
        _altaz = _radecs.transform_to(_frame)
        _solar_altaz = get_sun(_time).transform_to(_altaz)

        # get limit(s)
        _max_airmass = TEL__MAX__AIRMASS[f'{self.__name.lower()}']
        _min_airmass = TEL__MIN__AIRMASS[f'{self.__name.lower()}']
        _dusk = TEL__DUSK[f'{self.__name.lower()}'] * u.deg
        _twilight = TEL__TWILIGHT[f'{self.__name.lower()}'] * u.deg
        _horizon = AST__HORIZON * u.deg
        _north = AST__NORTH * u.deg
        _south = AST__SOUTH * u.deg

        # noinspection PyBroadException
        try:
            for i in range(len(_altaz)):

                # the Sun has risen, so not observable
                if _solar_altaz[i].alt >= _horizon:
                    _obs[i] = VAL__NOT__OBSERVABLE

                # morning or evening twilight, might be observable
                elif _twilight <= _solar_altaz.alt[i] < _horizon:

                    # the Sun is in the East, it must be rising so we are in morning twilight
                    if _north <= _solar_altaz[i].az <= _south:
                        _obs[i] = VAL__NOT__OBSERVABLE
                    # the Sun is in the West, it must be setting so we are in evening twilight
                    else:
                        _obs[i] = VAL__OBSERVABLE

                else:
                    _obs[i] = VAL__OBSERVABLE

                # modify for airmass or exclusion
                if _altaz.secz[i] >= _max_airmass:
                    _obs[i] = VAL__NOT__OBSERVABLE
                elif _msp[i] <= _mex[i]:
                    _obs[i] = VAL__NOT__OBSERVABLE

        except Exception:
            _obs = np.linspace(math.nan, math.nan, AST__5__MINUTES*ndays)

        # return result
        return _obs

    # +
    # method: observable_now()
    # -
    def observable_now(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
        """ returns the value of the observability flag for object for right now """
        return self.observable(ra, dec, f'{get_isot(0, True)}', ndays=1, from_now=True)[0]

    # +
    # method: observable_today()
    # -
    def observable_today(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
        """ returns an array of observability flags for object for today """
        return self.observable(ra, dec, f'{get_isot(0, True)}', ndays=1, from_now=False)

    # +
    # method: solar_separation()
    # -
    @staticmethod
    def solar_separation(ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION, date=get_isot(0, True),
                         ndays=MIN__NDAYS, from_now=False):
        """ returns an array of solar separation angles from object for several days """

        # check input(s)
        ra = ra if isinstance(ra, float) else MIN__RIGHT__ASCENSION
        ra = ra if ra > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
        ra = ra if ra < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
        dec = dec if isinstance(dec, float) else MIN__DECLINATION
        dec = dec if dec > MIN__DECLINATION else MIN__DECLINATION
        dec = dec if dec < MAX__DECLINATION else MAX__DECLINATION
        date = date if re.match(OBS_ISO_PATTERN, date) is not None else get_isot(0, True)
        ndays = ndays if isinstance(ndays, int) else MIN__NDAYS
        ndays = ndays if ndays > 0 else MIN__NDAYS
        from_now = from_now if isinstance(from_now, bool) else False

        # set default(s)
        _sep = None
        _time = Time(date) if from_now else Time(date.split()[0])
        _time = Time(_time.iso)
        _time = Time(_time) + (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))

        # noinspection PyBroadException
        try:
            _obj_radec = SkyCoord(ra=ra * u.deg, dec=dec * u.deg)
            _solar_coord = get_sun(_time).transform_to(_obj_radec)
            _sep = _obj_radec.separation(_solar_coord).deg
        except Exception:
            _sep = ndays * np.linspace(math.nan, math.nan, AST__5__MINUTES*ndays)

        # return array
        return _sep

    # +
    # method: solar_separation_now()
    # -
    def solar_separation_now(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
        """ returns the value of the solar separation angle from object right now """
        return self.solar_separation(ra, dec, f'{get_isot(0, True)}', ndays=1, from_now=True)[0]

    # +
    # method: solar_separation_today()
    # -
    def solar_separation_today(self, ra=MIN__RIGHT__ASCENSION, dec=MIN__DECLINATION):
        """ returns an array of solar separation angles from object for today """
        return self.solar_separation(ra, dec, f'{get_isot(0, True)}', ndays=1, from_now=False)

    # +
    # (static) method: sky_separation()
    # -
    @staticmethod
    def sky_separation(ra1=MIN__RIGHT__ASCENSION, dec1=MIN__DECLINATION,
                       ra2=MIN__RIGHT__ASCENSION, dec2=MIN__DECLINATION):
        """ returns angular separation (in degrees) of 2 objects """

        # check input(s
        ra1 = ra1 if isinstance(ra1, float) else MIN__RIGHT__ASCENSION
        ra1 = ra1 if ra1 > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
        ra1 = ra1 if ra1 < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
        dec1 = dec1 if isinstance(dec1, float) else MIN__DECLINATION
        dec1 = dec1 if dec1 > MIN__DECLINATION else MIN__DECLINATION
        dec1 = dec1 if dec1 < MAX__DECLINATION else MAX__DECLINATION
        ra2 = ra2 if isinstance(ra2, float) else MIN__RIGHT__ASCENSION
        ra2 = ra2 if ra2 > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
        ra2 = ra2 if ra2 < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
        dec2 = dec2 if isinstance(dec2, float) else MIN__DECLINATION
        dec2 = dec2 if dec2 > MIN__DECLINATION else MIN__DECLINATION
        dec2 = dec2 if dec2 < MAX__DECLINATION else MAX__DECLINATION

        # return result
        try:
            c1 = SkyCoord(ra=ra1 * u.deg, dec=dec1 * u.deg)
            c2 = SkyCoord(ra=ra2 * u.deg, dec=dec2 * u.deg)
            sep = c1.separation(c2)
            return float(sep.degree)
        except Exception:
            return float(math.nan)
