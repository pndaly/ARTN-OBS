#!/usr/bin/env python3


# +
# import(s)
# -
from src import *
from src.telescopes import *

from astroplan import Observer
from astroplan import FixedTarget
from astropy.coordinates import EarthLocation
from astropy.coordinates import get_moon
from astropy.coordinates import get_sun

import astropy
import math
import numpy as np


# +
# constant(s)
# -
AST__4__MINUTES = int(24.0 * 60.0 / 4.0)
AST__5__MINUTES = int(24.0 * 60.0 / 5.0)
AST__MOON__CIVIL = {0: 'new', 1: 'waxing crescent', 2: 'first quarter', 3: 'waxing gibbous',
                    4: 'full', 5: 'waning gibbous', 6: 'last quarter', 7: 'waning crescent'}
AST__MOON__ILLUM = [0.0, 25.0, 50.0, 75.0, 100.0, 75.0, 50.0, 25.0]
AST__MOON__PHASE = [math.pi, 3.0*math.pi/4.0, math.pi/2.0, math.pi/4.0,
                    0.0, math.pi/4.0, math.pi/2.0, 3.0*math.pi/4.0]
AST__MOON__WHICH = ['new', 'first quarter', 'full', 'last quarter']
AST__NDAYS = 1
AST__TWILIGHT = ['astronomical', 'civil', 'nautical']
AST__WHICH = ['next', 'previous', 'nearest']


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
        self.__coords = None
        self.__msg = None
        self.__time = None

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
        self.__timezone = TEL__TIMEZONE[self.__name]
        self.__utc_offset = TEL__UTC__OFFSET[self.__name]

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
        if isinstance(name, str) and name in TEL__TELESCOPES:
            self.__name = name
        else:
            raise Exception(f'invalid input, name={name}')

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log=None):
        self.__log = log if isinstance(log, logging.Logger) else None

    # +
    # getter(s) without setter(s)
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
    def coords(self):
        return self.__coords

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

    @property
    def time(self):
        return self.__time.isot if hasattr(self.__time, 'isot') else self.__time

    @property
    def timezone(self):
        return self.__timezone

    @property
    def utc_offset(self):
        return self.__utc_offset

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
    # method: __convert_coords__()
    # -
    def __convert_coords__(self, obs_name='', obs_coords=''):
        """ convert coords to suitable format for calculation(s) """
        try:
            if isinstance(obs_name, str) and obs_name.strip() != '':
                try:
                    self.__coords = FixedTarget.from_name(obs_name)
                except:
                    self.__coords = None
            elif isinstance(obs_coords, str) and obs_coords.strip() != '':
                try:
                    _ra, _dec = obs_coords.split()
                    _ra = f'{_ra} hours' if 'hours' not in _ra.lower() else _ra
                    _dec = f'{_dec} degrees' if 'degrees' not in _dec.lower() else _dec
                    self.__coords = SkyCoord(f"{_ra}", f"{_dec}")
                except:
                    self.__coords = None
            else:
                self.__coords = None
        except:
            self.__coords = None
        return self.__coords

    # +
    # method: __convert_time__()
    # -
    def __convert_time__(self, obs_time=Time(get_isot(0, True)), ndays=0):
        """ convert time to suitable format for calculation(s) """
        try:
            if isinstance(obs_time, astropy.time.core.Time) and obs_time.scale.lower() == 'utc':
                if isinstance(ndays, int) and ndays > 0:
                    self.__time = Time(obs_time.iso) + (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))
                else:
                    self.__time = obs_time
            elif re.match(OBS_ISO_PATTERN, obs_time) is not None:
                if isinstance(ndays, int) and ndays > 0:
                    self.__time = Time(obs_time.replace('T', ' ')) + \
                                  (ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES*ndays))
                else:
                    self.__time = Time(obs_time)
            else:
                self.__time = None
        except:
            self.__time = None
        return self.__time

    # +
    # method: dawn()
    # -
    def dawn(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False):
        """ returns dawn time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            twilight = twilight.lower() if twilight.lower() in AST__TWILIGHT else AST__TWILIGHT[0]
            utc = utc if isinstance(utc, bool) else False
            _jd = math.nan
            self.__convert_time__(obs_time=obs_time)
            if twilight == 'astronomical':
                _jd = self.__observer.sun_rise_time(
                    self.__time, which=which, horizon=self.__astronomical_dawn * u.degree).jd
            elif twilight == 'civil':
                _jd = self.__observer.sun_rise_time(
                    self.__time, which=which, horizon=self.__civil_dawn * u.degree).jd
            elif twilight == 'nautical':
                _jd = self.__observer.sun_rise_time(
                    self.__time, which=which, horizon=self.__nautical_dawn * u.degree).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: dusk()
    # -
    def dusk(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], twilight=AST__TWILIGHT[0], utc=False):
        """ returns dusk time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            twilight = twilight.lower() if twilight.lower() in AST__TWILIGHT else AST__TWILIGHT[0]
            utc = utc if isinstance(utc, bool) else False
            _jd = math.nan
            self.__convert_time__(obs_time=obs_time)
            if twilight == 'astronomical':
                _jd = self.__observer.sun_set_time(
                    self.__time, which=which, horizon=self.__astronomical_dusk * u.degree).jd
            elif twilight == 'civil':
                _jd = self.__observer.sun_set_time(
                    self.__time, which=which, horizon=self.__civil_dusk * u.degree).jd
            elif twilight == 'nautical':
                _jd = self.__observer.sun_set_time(
                    self.__time, which=which, horizon=self.__nautical_dusk * u.degree).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: is_day()
    # -
    def is_day(self, obs_time=Time(get_isot(0, True))):
        """ returns daytime flag """
        try:
            self.__convert_time__(obs_time=obs_time)
            return False if self.__observer.is_night(self.__time) else True
        except:
            return None

    # +
    # method: is_night()
    # -
    def is_night(self, obs_time=Time(get_isot(0, True))):
        """ returns nighttime flag """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.is_night(self.__time)
        except:
            return None

    # +
    # method: is_observable()
    # -
    def is_observable(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ return target observability flag """
        try:
            self.__convert_time__(obs_time=obs_time)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            return self.__observer.target_is_up(self.__time, target=self.__coords)
        except:
            return False

    # +
    # method: is_observable_ndays()
    # -
    def is_observable_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS):
        """ return target observability flag(s) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            return self.__observer.target_is_up(self.__time, target=self.__coords)
        except:
            return None

    # +
    # method: is_observable_now()
    # -
    def is_observable_now(self, obs_name='', obs_coords=''):
        """ returns target observability flag now """
        try:
            return self.is_observable_ndays(obs_time=f'{get_isot(0, True)}', obs_name=obs_name,
                                            obs_coords=obs_coords, ndays=1)[0]
        except:
            return False

    # +
    # method: is_observable_today()
    # -
    def is_observable_today(self, obs_name='', obs_coords=''):
        """ returns target observability flag(s) today """
        try:
            return self.is_observable_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000",
                                            obs_name=obs_name, obs_coords=obs_coords, ndays=1)
        except:
            return None

    # +
    # function: lst()
    # -
    def lst(self, obs_time=Time(get_isot(0, True))):
        """ returns local sidereal time """
        try:
            self.__convert_time__(obs_time=obs_time)
            _lst_h, _lst_m, _lst_s = self.__observer.local_sidereal_time(self.__time).hms
            return f'{int(_lst_h):02d}:{int(_lst_m):02d}:{float(_lst_s):06.3f}'
        except:
            return None

    # +
    # method: midday()
    # -
    def midday(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns sun midday time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _jd = self.__observer.noon(self.__time, which=which).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: midnight()
    # -
    def midnight(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns sun midnight time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _jd = self.__observer.midnight(self.__time, which=which).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: moon_altaz()
    # -
    def moon_altaz(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar (alt, az, distance) """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_altaz(self.__time)
        except:
            return None

    # +
    # method: moon_altaz_ndays()
    # -
    def moon_altaz_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns lunar (alt, az, distance) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            return self.__observer.moon_altaz(self.__time)
        except:
            return None

    # +
    # method: moon_altaz_now()
    # -
    def moon_altaz_now(self):
        """ returns lunar (alt, az, distance) now """
        try:
            return self.moon_altaz_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return None

    # +
    # method: moon_altaz_today()
    # -
    def moon_altaz_today(self):
        """ returns lunar (alt, az, distance) today """
        try:
            return self.moon_altaz_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: moon_alt()
    # -
    def moon_alt(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar alt """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_altaz(self.__time).alt.value
        except:
            return math.nan

    # +
    # method: moon_az()
    # -
    def moon_az(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar az """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_altaz(self.__time).az.value
        except:
            return math.nan

    # +
    # method: moon_civil() - TO DO
    # -
    def moon_civil(self, obs_time=get_isot(0, True)):
        """ returns lunar phase for civilians """

        # check input(s)
        if not isinstance(obs_time, str) or (isinstance(obs_time, str) and re.match(OBS_ISO_PATTERN, obs_time) is None):
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
            _isots = {_v: self.moon_date(obs_time=_start, which='next', phase=_v) for _v in AST__MOON__WHICH}
            _jds = {_k: isot_to_jd(_v) for _k, _v in _isots.items()}
            _isots_r, _jds_r = {_v: _k for _k, _v in _isots.items()}, {_v: _k for _k, _v in _jds.items()}
            # get key
            _val = nearest(list(_jds.values()), _now_jd)
            _key = _jds_r.get(_val, None)
            # return result
            if _key is not None:
                if (_jds[_key]-0.5) <= _now_jd <= (_jds[_key]+0.5):
                    return _key
                _x = {_j: _i for _i, _j in AST__MOON__CIVIL.items()}.get(_key, None)
                if _x is not None and isinstance(_x, int):
                    _x = _x + 1 if _now_jd > _jds[_key] else _x - 1
                    return AST__MOON__CIVIL[_x % len(AST__MOON__CIVIL)]
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_date() - TO DO
    # -
    def moon_date(self, obs_time=get_isot(0, True), which=AST__WHICH[-1], phase=AST__MOON__WHICH[0], utc=False):
        """ returns lunar date for phase """

        # reset input(s)
        which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
        phase = phase.lower() if phase.lower() in AST__MOON__WHICH else AST__MOON__WHICH[0]
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
            return jd_to_isot(_ans) if utc else jd_to_isot(_ans - abs(self.__utc_offset/24.0))
        except:
            if self.__log:
                self.__log.error(f'unable to convert time')
        return None

    # +
    # method: moon_distance()
    # -
    def moon_distance(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar distance """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_altaz(self.__time).distance.value
        except:
            return math.nan

    # +
    # method: moon_exclusion()
    # -
    def moon_exclusion(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar exclusion angle """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__min_moonex + ((self.__max_moonex - self.__min_moonex) *
                                        self.__observer.moon_illumination(self.__time))
        except:
            return math.nan

    # +
    # method: moon_exclusion_ndays()
    # -
    def moon_exclusion_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns lunar exclusion angle(s) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            _illuminati = self.__observer.moon_illumination(self.__time)
            _moon_altaz = self.__observer.moon_altaz(self.__time)
            _illuminati[_moon_altaz.alt < 0.0] = 0.0
            return self.__min_moonex + ((self.__max_moonex - self.__min_moonex) * _illuminati)
        except:
            return None

    # +
    # method: moon_exclusion_now()
    # -
    def moon_exclusion_now(self):
        """ returns lunar exclusion angle now """
        try:
            return self.moon_exclusion_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return math.nan

    # +
    # method: moon_exclusion_today()
    # -
    def moon_exclusion_today(self):
        """ returns lunar exclusion angle(s) today """
        try:
            return self.moon_exclusion_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: moon_illumination()
    # -
    def moon_illumination(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar illumination """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_illumination(self.__time)
        except:
            return math.nan

    # +
    # method: moon_illumination_ndays()
    # -
    def moon_illumination_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns lunar illumination over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            return self.__observer.moon_illumination(self.__time)
        except:
            return None

    # +
    # method: moon_illumination_now()
    # -
    def moon_illumination_now(self):
        """ returns lunar illumination now """
        try:
            return self.moon_illumination_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return math.nan

    # +
    # method: moon_illumination_today()
    # -
    def moon_illumination_today(self):
        """ returns lunar illumination today """
        try:
            return self.moon_illumination_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: moon_is_up()
    # -
    def moon_is_up(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg):
        """ returns lunar  """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_alt(self.__time) > horizon
        except:
            return False

    # +
    # method: moon_is_down()
    # -
    def moon_is_down(self, obs_time=Time(get_isot(0, True)), horizon=0*u.deg):
        """ returns True if moon has below horizon """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_alt(self.__time) < horizon
        except:
            return False

    # +
    # method: moon_phase()
    # -
    def moon_phase(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar phase """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.moon_phase(self.__time).value
        except:
            return math.nan

    # +
    # method: moon_phase_ndays()
    # -
    def moon_phase_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns lunar phase over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            return self.__observer.moon_phase(self.__time).value
        except:
            return None

    # +
    # method: moon_phase_now()
    # -
    def moon_phase_now(self):
        """ returns lunar phase now """
        try:
            return self.moon_phase_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return math.nan

    # +
    # method: moon_phase_today()
    # -
    def moon_phase_today(self):
        """ returns lunar phase today """
        try:
            return self.moon_phase_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: moon_radec()
    # -
    def moon_radec(self, obs_time=Time(get_isot(0, True))):
        """ returns lunar (ra_deg, dec_deg, distance) """
        try:
            self.__convert_time__(obs_time=obs_time)
            return get_moon(self.__time, location=self.__observatory)
        except:
            return None

    # +
    # method: moon_radec_ndays()
    # -
    def moon_radec_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns lunar (ra, dec, distance) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            return get_moon(self.__time, location=self.__observatory)
        except:
            return None

    # +
    # method: moon_radec_now()
    # -
    def moon_radec_now(self):
        """ returns lunar (ra, dec, distance) now """
        try:
            return self.moon_radec_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return None

    # +
    # method: moon_radec_today()
    # -
    def moon_radec_today(self):
        """ returns lunar (ra, dec, distance) today """
        try:
            return self.moon_radec_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: moon_rise()
    # -
    def moon_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns lunar rise time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _jd = self.__observer.moon_rise_time(self.__time, which=which).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: moon_separation()
    # -
    def moon_separation(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ returns lunar separation angle """
        try:
            _moon_coord = self.moon_radec(obs_time=obs_time)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            _obj_radec = SkyCoord(ra=self.__coords.ra.value * u.deg, dec=self.__coords.dec.value * u.deg)
            return _obj_radec.separation(_moon_coord).deg
        except:
            return math.nan

    # +
    # method: moon_separation_ndays()
    # -
    def moon_separation_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS):
        """ returns lunar separation angle(s) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            _moon_coords = self.moon_radec_ndays(obs_time=obs_time, ndays=ndays)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            _obj_radec = SkyCoord(ra=self.__coords.ra.value * u.deg, dec=self.__coords.dec.value * u.deg)
            return _obj_radec.separation(_moon_coords).deg
        except:
            return None

    # +
    # method: moon_separation_now()
    # -
    def moon_separation_now(self, obs_name='', obs_coords=''):
        """ returns lunar separation angle now """
        try:
            return self.moon_separation_ndays(obs_time=f'{get_isot(0, True)}', obs_name=obs_name,
                                              obs_coords=obs_coords, ndays=1)[0]
        except:
            return math.nan

    # +
    # method: moon_separation_today()
    # -
    def moon_separation_today(self, obs_name='', obs_coords=''):
        """ returns lunar separation angle(s) today """
        try:
            return self.moon_separation_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000",
                                              obs_name=obs_name, obs_coords=obs_coords, ndays=1)
        except:
            return None

    # +
    # method: moon_set()
    # -
    def moon_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns lunar set time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _jd = self.__observer.moon_set_time(self.__time, which=which).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: moon_steward() - TO DO
    # -
    def moon_steward(self, obs_time=get_isot(0, True)):
        """ returns lunar phase for steward observatory """

        # check input(s)
        if not isinstance(obs_time, str) or (isinstance(obs_time, str) and re.match(OBS_ISO_PATTERN, obs_time) is None):
            return None, None

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
        return None, None

    # +
    # (override) method: observe()
    # -
    def observe(self, **kwargs):
        if self.__log:
            self.__log.debug(f'called self.observe, kwargs={kwargs}')

    # +
    # method: observing_end()
    # -
    def observing_end(self, obs_time=Time(get_isot(0, True)), utc=False):
        """ returns isot of end of observing night """
        try:
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _date = self.__observer.tonight(self.__time)
            return jd_to_isot(_date[1].jd if utc else (_date[1].jd - abs(self.__utc_offset/24.0)))
        except:
            return None

    # +
    # method: observing_start()
    # -
    def observing_start(self, obs_time=Time(get_isot(0, True)), utc=False):
        """ returns isot of start of observing night """
        try:
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _date = self.__observer.tonight(self.__time)
            return jd_to_isot(_date[0].jd if utc else (_date[0].jd - abs(self.__utc_offset/24.0)))
        except:
            return None

    # +
    # method: parallactic_angle()
    # -
    def parallactic_angle(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ returns parallactic angle """
        try:
            self.__convert_time__(obs_time=obs_time)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            return self.__observer.parallactic_angle(time=self.__time, target=self.__coords)
        except:
            return math.nan

    # +
    # method: radec_to_altaz()
    # -
    def radec_to_altaz(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ return Alt, Az for RA, Dec """
        try:
            self.__convert_time__(obs_time=obs_time)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            _ans = self.__observer.altaz(time=self.__time, target=self.__coords)
            return _ans if (hasattr(_ans, 'alt') and hasattr(_ans, 'az')) else None
        except:
            return None

    # +
    # method: sun_altaz()
    # -
    def sun_altaz(self, obs_time=Time(get_isot(0, True))):
        """ returns solar (alt, az, distance) """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.sun_altaz(self.__time)
        except:
            return None

    # +
    # method: sun_altaz_ndays()
    # -
    def sun_altaz_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns solar (alt, az, distance) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            return self.__observer.sun_altaz(self.__time)
        except:
            return None

    # +
    # method: sun_altaz_now()
    # -
    def sun_altaz_now(self):
        """ returns solar (alt, az, distance) now """
        try:
            return self.sun_altaz_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return None

    # +
    # method: sun_altaz_today()
    # -
    def sun_altaz_today(self):
        """ returns solar (alt, az, distance) today """
        try:
            return self.sun_altaz_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: sun_alt()
    # -
    def sun_alt(self, obs_time=Time(get_isot(0, True))):
        """ returns solar alt """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.sun_altaz(self.__time).alt.value
        except:
            return math.nan

    # +
    # method: sun_az()
    # -
    def sun_az(self, obs_time=Time(get_isot(0, True))):
        """ returns solar az """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.__observer.sun_altaz(self.__time).az.value
        except:
            return math.nan

    # +
    # method: sun_radec()
    # -
    def sun_radec(self, obs_time=Time(get_isot(0, True))):
        """ returns solar (ra_deg, dec_deg, distance) """
        try:
            self.__convert_time__(obs_time=obs_time)
            return get_sun(self.__time)
        except:
            return None

    # +
    # method: sun_radec_ndays()
    # -
    def sun_radec_ndays(self, obs_time=Time(get_isot(0, True)), ndays=AST__NDAYS):
        """ returns solar (ra, dec, distance) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            self.__convert_time__(obs_time=obs_time, ndays=ndays)
            return get_sun(self.__time)
        except:
            return None

    # +
    # method: sun_radec_now()
    # -
    def sun_radec_now(self):
        """ returns solar (ra, dec, distance) now """
        try:
            return self.sun_radec_ndays(obs_time=f'{get_isot(0, True)}', ndays=1)[0]
        except:
            return None

    # +
    # method: sun_radec_today()
    # -
    def sun_radec_today(self):
        """ returns solar (ra, dec, distance) today """
        try:
            return self.sun_radec_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000", ndays=1)
        except:
            return None

    # +
    # method: sun_rise()
    # -
    def sun_rise(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns solar rise time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _jd = self.__observer.sun_rise_time(self.__time, which=which).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: sun_separation()
    # -
    def sun_separation(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords=''):
        """ returns solar separation angle """
        try:
            _sun_coord = self.sun_radec(obs_time=obs_time)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            _obj_radec = SkyCoord(ra=self.__coords.ra.value * u.deg, dec=self.__coords.dec.value * u.deg)
            return _obj_radec.separation(_sun_coord).deg
        except:
            return math.nan

    # +
    # method: sun_separation_ndays()
    # -
    def sun_separation_ndays(self, obs_time=Time(get_isot(0, True)), obs_name='', obs_coords='', ndays=AST__NDAYS):
        """ returns solar separation angle(s) over ndays """
        try:
            ndays = ndays if (isinstance(ndays, int) and ndays > 0) else AST__NDAYS
            _sun_coords = self.sun_radec_ndays(obs_time=obs_time, ndays=ndays)
            self.__convert_coords__(obs_name=obs_name, obs_coords=obs_coords)
            _obj_radec = SkyCoord(ra=self.__coords.ra.value * u.deg, dec=self.__coords.dec.value * u.deg)
            return _obj_radec.separation(_sun_coords).deg
        except:
            return None

    # +
    # method: sun_separation_now()
    # -
    def sun_separation_now(self, obs_name='', obs_coords=''):
        """ returns solar separation angle now """
        try:
            return self.sun_separation_ndays(obs_time=f'{get_isot(0, True)}', obs_name=obs_name,
                                             obs_coords=obs_coords, ndays=1)[0]
        except:
            return math.nan

    # +
    # method: sun_separation_today()
    # -
    def sun_separation_today(self, obs_name='', obs_coords=''):
        """ returns solar separation angle(s) today """
        try:
            return self.sun_separation_ndays(obs_time=f"{get_isot(0, False).split('T')[0]}T00:00:00.000000",
                                             obs_name=obs_name, obs_coords=obs_coords, ndays=1)
        except:
            return None

    # +
    # method: sun_set()
    # -
    def sun_set(self, obs_time=Time(get_isot(0, True)), which=AST__WHICH[-1], utc=False):
        """ returns solar set time """
        try:
            which = which.lower() if which.lower() in AST__WHICH else AST__WHICH[-1]
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _jd = self.__observer.sun_set_time(self.__time, which=which).jd
            return jd_to_isot(_jd) if utc else jd_to_isot(_jd - abs(self.__utc_offset/24.0))
        except:
            return None

    # +
    # method: tonight()
    # -
    def tonight(self, obs_time=Time(get_isot(0, True)), utc=False):
        """ returns isot(s) of observing night """
        try:
            utc = utc if isinstance(utc, bool) else False
            self.__convert_time__(obs_time=obs_time)
            _date = self.__observer.tonight(self.__time)
            _start = jd_to_isot(_date[0].jd if utc else (_date[0].jd - abs(self.__utc_offset/24.0)))
            _end = jd_to_isot(_date[1].jd if utc else (_date[1].jd - abs(self.__utc_offset/24.0)))
            return _start, _end
        except:
            return None, None

    # +
    # function: zenith()
    # -
    def zenith(self, obs_time=Time(get_isot(0, True))):
        """ returns RA, Dec of zenith """
        try:
            self.__convert_time__(obs_time=obs_time)
            return self.lst(obs_time=self.__time), dec_from_decimal(self.__latitude)
        except:
            return None, None

    # +
    # method: airmass_plot()
    # -
    # def airmass_plot(self, _ra=MIN__RIGHT__ASCENSION, _dec=MIN__DECLINATION, _date=get_isot(0, True),
    #                  _ndays=AST__NDAYS, _from_now=False):
    #     """ returns an image of airmass for object for several days """
    #
    #     # check input(s)
    #     # _ra = _ra if isinstance(_ra, float) else MIN__RIGHT__ASCENSION
    #     # _ra = _ra if _ra > MIN__RIGHT__ASCENSION else MIN__RIGHT__ASCENSION
    #     # _ra = _ra if _ra < MAX__RIGHT__ASCENSION else MAX__RIGHT__ASCENSION
    #     # _dec = _dec if isinstance(_dec, float) else MIN__DECLINATION
    #     # _dec = _dec if _dec > MIN__DECLINATION else MIN__DECLINATION
    #     # _dec = _dec if _dec < MAX__DECLINATION else MAX__DECLINATION
    #     # _date = _date if re.match(OBS_ISO_PATTERN, _date) is not None else get_isot(0, True)
    #     # _ndays = _ndays if isinstance(_ndays, int) else AST__NDAYS
    #     # _ndays = _ndays if _ndays > 0 else AST__NDAYS
    #     # _from_now = _from_now if isinstance(_from_now, bool) else False
    #     #
    #     # # set default(s)
    #     # _time_now = Time.now()
    #     # if 'T' in _date:
    #     #     _start = Time(_date) if _from_now else Time(_date.split('T')[0])
    #     # else:
    #     #     _start = Time(_date) if _from_now else Time(_date.split()[0])
    #     # _now = Time(_start.iso)
    #     # _start = Time(_start.iso)
    #     # _start = Time(_start) + (_ndays * u.day * np.linspace(0.0, 1.0, AST__5__MINUTES))
    #     # _title = f"Airmass [{_ndays} Day(s)]"
    #     #
    #     # _ra_hms = Angle(_ra, unit=u.deg).hms
    #     # _HH, _MM, _SS = _ra_hms[0], _ra_hms[1], _ra_hms[2]
    #     # _sign = '-' if str(_dec)[0] == '-' else '+'
    #     # _dec_dms = Angle(_dec, unit=u.deg).dms
    #     # _dd, _mm, _ss = abs(_dec_dms[0]), abs(_dec_dms[1]), abs(_dec_dms[2])
    #     # _sub_title = f"RA={int(_HH):02d}:{int(_MM):02d}:{int(_SS):02d} ({_ra:.3f}{UNI__DEGREE}), " \
    #     #              f"Dec={_sign}{int(_dd):02d}{UNI__DEGREE}{int(_mm):02d}{UNI__ARCMIN}{int(_ss):02d}{UNI__ARCSEC} " \
    #     #              f"({_dec:.3f}{UNI__DEGREE})"
    #     #
    #     # # modify to reference frame and get airmass
    #     # _frame = AltAz(obstime=_start, location=self.__observatory)
    #     # _radecs = SkyCoord(ra=_ra*u.deg, dec=_dec*u.deg)
    #     # _altaz = _radecs.transform_to(_frame)
    #     #
    #     # # extract axes
    #     # _max_airmass = TEL__MAX__AIRMASS[f'{self.__name.lower()}']
    #     # _min_airmass = TEL__MIN__AIRMASS[f'{self.__name.lower()}']
    #     # _time_axis = _start[(_altaz.secz <= _max_airmass) & (_altaz.secz >= _min_airmass)]
    #     # _airmass_axis = _altaz.secz[(_altaz.secz <= _max_airmass) & (_altaz.secz >= _min_airmass)]
    #     #
    #     # # plot it
    #     # fig, ax = plt.subplots()
    #     # ax.plot_date(_time_axis.plot_date, _airmass_axis, 'r-')
    #     # ax.plot_date([_time_now.plot_date, _time_now.plot_date], [-999, 999], 'y--')
    #     # xfmt = mdates.DateFormatter('%H:%M')
    #     # ax.xaxis.set_major_formatter(xfmt)
    #     # plt.gcf().autofmt_xdate()
    #     # ax.set_ylim([_max_airmass, _min_airmass])
    #     # ax.set_xlim([_start.datetime[0], _start.datetime[-1]])
    #     # ax.set_title(f'{_title}\n{_sub_title}')
    #     # ax.set_ylabel(f'Airmass ({UNI__PROPORTIONAL} secZ)')
    #     # ax.set_xlabel(f"{str(_now).split()[0]} (UTC)")
    #     # buf = io.BytesIO()
    #     # # plt.savefig(f'{_file}')
    #     # plt.savefig(buf, format='png', dpi=100)
    #     # plt.close()
    #     # data = buf.getvalue()
    #     data = self.__name
    #     return f'data:image/png;base64,{base64.b64encode(data).decode()}'

    # +
    # (static) method: lunation()
    # -
    @staticmethod
    def lunation(obs_time=get_isot(0, True)):
        """ returns lunation """
        try:
            _date = isot_to_ephem(obs_time)
            _nnm = isot_to_jd(ephem_to_isot(ephem.next_new_moon(_date)))
            _pnm = isot_to_jd(ephem_to_isot(ephem.previous_new_moon(_date)))
            return _nnm - _pnm
        except:
            return math.nan

    # +
    # method: alt_lunation()
    # -
    def alt_lunation(self, obs_time=get_isot(0, True)):
        """ returns lunation """
        try:
            _nnm = isot_to_jd(self.moon_date(obs_time=obs_time, phase='new', which='next'))
            _pnm = isot_to_jd(self.moon_date(obs_time=obs_time, phase='new', which='previous'))
            return _nnm - _pnm
        except:
            return math.nan

    # +
    # method: sky_separation()
    # -
    def sky_separation(self, obs_name_1='', obs_coords_1='', obs_name_2='', obs_coords_2=''):
        """ returns angular separation (in degrees) of 2 objects """
        try:
            _c1 = self.__convert_coords__(obs_name=obs_name_1, obs_coords=obs_coords_1).coord
            _c2 = self.__convert_coords__(obs_name=obs_name_2, obs_coords=obs_coords_2).coord
            return _c1.separation(_c2).degree
        except:
            return math.nan
