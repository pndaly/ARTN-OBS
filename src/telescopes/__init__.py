#!/usr/bin/env python3


# +
# import(s)
# -
from datetime import datetime
import itertools
import pytz


# +
# telescope(s)
# -
TEL__NODES = {
    'Bok': {
        'aka': 'Bok 90-inch, Kitt Peak, AZ',
        'altitude': 6795.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 60.0,
        'dome_slew_rate': 1.0,
        'elevation': 6795.0,
        'focal_length_m': 6.08,
        'focal_length_ft': 6.08 * 3.28083,
        'primary_imperial': 2.29 * 3.28083 * 12.0,
        'latitude': 31.9629,
        'longitude': -111.6004,
        'max_airmass': 3.5,
        'max_moon_exclusion': 25.0,
        'primary_metric': 2.29,
        'min_airmass': 1.0,
        'min_moon_exclusion': 2.5,
        'name': 'bok',
        'mount': 'Equatorial',
        'telescope_slew_rate': 0.5,
        'instruments': ['90Prime', 'BCSpec'],
        'timezone': pytz.timezone('America/Phoenix'),
        'utc_offset': datetime.now(pytz.timezone('America/Phoenix')).utcoffset().total_seconds()/60.0/60.0
    },
    'Kuiper': {
        'aka': 'Kuiper 61-inch, Mount Bigelow, AZ',
        'altitude': 8235.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 58.0,
        'dome_slew_rate': 1.1,
        'elevation': 8235.0,
        'focal_length_m': 9.6,
        'focal_length_ft': 9.6 * 3.28083,
        'latitude': 32.4165,
        'longitude': -110.7345,
        'max_airmass': 2.5,
        'max_moon_exclusion': 45.0,
        'primary_imperial': 1.54 * 3.28083 * 12.0,
        'primary_metric': 1.54,
        'min_airmass': 1.0,
        'min_moon_exclusion': 3.0,
        'name': 'kuiper',
        'mount': 'Equatorial',
        'telescope_slew_rate': 0.6,
        'instruments': ['Mont4k'],
        'timezone': pytz.timezone('America/Phoenix'),
        'utc_offset': datetime.now(pytz.timezone('America/Phoenix')).utcoffset().total_seconds()/60.0/60.0
    },
    'MMT': {
        'aka': 'MMT 6.5m, Mount Hopkins, AZ',
        'altitude': 8585.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 58.0,
        'dome_slew_rate': 1.2,
        'elevation': 8585.0,
        'focal_length_m': 9.6,
        'focal_length_ft': 9.6 * 3.28083,
        'latitude': 31.6883,
        'longitude': -110.8850,
        'max_airmass': 3.5,
        'max_moon_exclusion': 45.0,
        'primary_imperial': 6.5 * 3.28083 * 12.0,
        'primary_metric': 6.5,
        'min_airmass': 1.0,
        'min_moon_exclusion': 3.0,
        'name': 'mmt',
        'mount': 'Alt-Az',
        'telescope_slew_rate': 0.7,
        'instruments': ['BinoSpec'],
        'timezone': pytz.timezone('America/Phoenix'),
        'utc_offset': datetime.now(pytz.timezone('America/Phoenix')).utcoffset().total_seconds()/60.0/60.0
    },
    'Vatt': {
        'aka': 'Vatt 1.8-metre, Mount Graham, AZ',
        'altitude': 10469.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 60.0,
        'dome_slew_rate': 1.3,
        'elevation': 10469.0,
        'focal_length_m': 16.48,
        'focal_length_ft': 16.48 * 3.28083,
        'latitude': 32.7016,
        'longitude': -109.8719,
        'max_airmass': 3.5,
        'max_moon_exclusion': 25.0,
        'primary_imperial': 1.8 * 3.28083 * 12.0,
        'primary_metric': 1.8,
        'min_airmass': 1.0,
        'min_moon_exclusion': 2.5,
        'name': 'vatt',
        'mount': 'Alt-Az',
        'telescope_slew_rate': 0.8,
        'instruments': ['Vatt4k'],
        'timezone': pytz.timezone('America/Phoenix'),
        'utc_offset': datetime.now(pytz.timezone('America/Phoenix')).utcoffset().total_seconds()/60.0/60.0
    },
    'Steward': {
        'aka': 'Raymond White 21-inch, Tucson, AZ',
        'altitude': 0.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 60.0,
        'dome_slew_rate': 1.3,
        'elevation': 0.0,
        'focal_length_m': 1.0,
        'focal_length_ft': 1.0 * 3.28083,
        'latitude': 32.233184,
        'longitude': -110.948944,
        'max_airmass': 2.5,
        'max_moon_exclusion': 25.0,
        'primary_imperial': 21.0,
        'primary_metric': 0.5334,
        'min_airmass': 1.0,
        'min_moon_exclusion': 2.5,
        'name': 'steward',
        'mount': 'Alt-Az',
        'telescope_slew_rate': 0.8,
        'instruments': [],
        'timezone': pytz.timezone('America/Phoenix'),
        'utc_offset': datetime.now(pytz.timezone('America/Phoenix')).utcoffset().total_seconds()/60.0/60.0
    },
    'Greenwich': {
        'aka': "Airy's Transit Circle, Greenwich, UK",
        'altitude': 0.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 60.0,
        'dome_slew_rate': 1.0,
        'elevation': 0.0,
        'focal_length_m': 3.5,
        'focal_length_ft': 1.0 * 3.28083,
        'latitude': 51.477754,
        'longitude': -0.001138,
        'max_airmass': 2.5,
        'max_moon_exclusion': 25.0,
        'primary_imperial': 8.1,
        'primary_metric': 0.20574,
        'min_airmass': 1.0,
        'min_moon_exclusion': 2.5,
        'name': 'rgo',
        'mount': 'Alt-Az',
        'telescope_slew_rate': 1.0,
        'instruments': [],
        'timezone': pytz.timezone('Greenwich'),
        'utc_offset': datetime.now(pytz.timezone('Greenwich')).utcoffset().total_seconds()/60.0/60.0
    },
    'Colombieres': {
        'aka': "La Basse Riviere, Colombieres, France",
        'altitude': 0.0 / 3.28083,
        'civil_dawn': -6.0,
        'nautical_dawn': -12.0,
        'astronomical_dawn': -18.0,
        'civil_dusk': -6.0,
        'nautical_dusk': -12.0,
        'astronomical_dusk': -18.0,
        'declination_limit': 60.0,
        'dome_slew_rate': 1.0,
        'elevation': 0.0,
        'focal_length_m': 1.0,
        'focal_length_ft': 1.0 * 3.28083,
        'latitude': 49.301919,
        'longitude': -0.967320,
        'max_airmass': 2.5,
        'max_moon_exclusion': 25.0,
        'primary_imperial': 6.0,
        'primary_metric': 0.1524,
        'min_airmass': 1.0,
        'min_moon_exclusion': 2.5,
        'name': 'colombieres',
        'mount': 'Alt-Az',
        'telescope_slew_rate': 1.0,
        'instruments': [],
        'timezone': pytz.timezone('Europe/Paris'),
        'utc_offset': datetime.now(pytz.timezone('Europe/Paris')).utcoffset().total_seconds()/60.0/60.0
    }
}


# +
# structure(s)
# -
TEL__AKA = {_k: _v['aka'] for _k, _v in TEL__NODES.items() if 'aka' in _v}
TEL__ALTITUDE = {_k: _v['altitude'] for _k, _v in TEL__NODES.items() if 'altitude' in _v}
TEL__ASTRONOMICAL__DAWN = \
    {_k: _v['astronomical_dawn'] for _k, _v in TEL__NODES.items() if 'astronomical_dawn' in _v}
TEL__ASTRONOMICAL__DUSK = \
    {_k: _v['astronomical_dusk'] for _k, _v in TEL__NODES.items() if 'astronomical_dusk' in _v}
TEL__CIVIL__DAWN = \
    {_k: _v['civil_dawn'] for _k, _v in TEL__NODES.items() if 'civil_dawn' in _v}
TEL__CIVIL__DUSK = \
    {_k: _v['civil_dusk'] for _k, _v in TEL__NODES.items() if 'civil_dusk' in _v}
TEL__DEC__LIMIT = {_k: _v['declination_limit'] for _k, _v in TEL__NODES.items() if 'declination_limit' in _v}
TEL__DOME__SLEW__RATE = {_k: _v['dome_slew_rate'] for _k, _v in TEL__NODES.items() if 'dome_slew_rate' in _v}
TEL__LATITUDE = {_k: _v['latitude'] for _k, _v in TEL__NODES.items() if 'latitude' in _v}
TEL__LONGITUDE = {_k: _v['longitude'] for _k, _v in TEL__NODES.items() if 'longitude' in _v}
TEL__MAX__AIRMASS = {_k: _v['max_airmass'] for _k, _v in TEL__NODES.items() if 'max_airmass' in _v}
TEL__MAX__MOONEX = {_k: _v['max_moon_exclusion'] for _k, _v in TEL__NODES.items() if 'max_moon_exclusion' in _v}
TEL__MIN__AIRMASS = {_k: _v['min_airmass'] for _k, _v in TEL__NODES.items() if 'min_airmass' in _v}
TEL__MIN__MOONEX = {_k: _v['min_moon_exclusion'] for _k, _v in TEL__NODES.items() if 'min_moon_exclusion' in _v}
TEL__NAME = [_k.lower() for _k in TEL__NODES]
TEL__NAUTICAL__DAWN = \
    {_k: _v['nautical_dawn'] for _k, _v in TEL__NODES.items() if 'nautical_dawn' in _v}
TEL__NAUTICAL__DUSK = \
    {_k: _v['nautical_dusk'] for _k, _v in TEL__NODES.items() if 'nautical_dusk' in _v}
TEL__SLEW__RATE = {_k: _v['telescope_slew_rate'] for _k, _v in TEL__NODES.items() if 'telescope_slew_rate' in _v}
TEL__TIMEZONE = {_k: _v['timezone'] for _k, _v in TEL__NODES.items() if 'timezone' in _v}
TEL__UTC__OFFSET = {_k: _v['utc_offset'] for _k, _v in TEL__NODES.items() if 'utc_offset' in _v}


# +
# derived structure(s)
# -
TEL__INSTRUMENTS = list(itertools.chain.from_iterable([_v['instruments'] for _k, _v in TEL__NODES.items()]))
TEL__SUPPORTED = {_k: _v['instruments'] for _k, _v in TEL__NODES.items()}
TEL__TELESCOPES = [_k for _k in TEL__NODES]
