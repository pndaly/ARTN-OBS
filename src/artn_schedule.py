#!/usr/bin/env python3


# +
#  import(s)
# -
from src.observations.darks import *
from src.observations.flats import *
from src.observations.foci import *
from src.observations.non_sidereal import *
from src.observations.sidereal import *

import argparse


# +
# function: artn_schedule()
# -
# noinspection PyBroadException,PyUnresolvedReferences
def artn_schedule(instrument=random.choice(TEL__INSTRUMENTS),
                  telescope=random.choice(TEL__TELESCOPES), verbose=False):

    # check input(s)
    if not isinstance(instrument, str) or instrument not in TEL__INSTRUMENTS:
        raise Exception(f'invalid input, instrument={instrument}')
    if not isinstance(telescope, str) or telescope not in TEL__TELESCOPES:
        raise Exception(f'invalid input, telescope={telescope}')
    if instrument not in TEL__SUPPORTED[f'{telescope}']:
        raise Exception(f'invalid combination, instrument={instrument}, telescope={telescope}')
    verbose = verbose if isinstance(verbose, bool) else False

    # create observing object(s)
    try:
        if verbose:
            _log = Logger(f'{telescope}-{instrument}').logger
        else:
            _log = None
        _tel = Telescope(name=telescope, log=_log)
        _ins = Instrument(name=instrument, log=_log)
        _obsp = ObsParams(instrument=_ins, telescope=_tel, log=_log)
        _dark = Darks(instrument=_ins, telescope=_tel, log=_log)
        _flat = Flats(instrument=_ins, telescope=_tel, log=_log)
        _foci = Foci(instrument=_ins, telescope=_tel, log=_log)
        _nsid = NonSidereal(instrument=_ins, telescope=_tel, log=_log)
        _sid = Sidereal(instrument=_ins, telescope=_tel, log=_log)
    except:
        raise Exception(f'failed to create critical observing components')
    else:
        if verbose:
            _obsp.__dump__()

    # start-of-night message
    pdh(f"{_tel.name} telescope observing schedule for {_obsp.mst.split('T')[0]}".upper(), color='green')
    if verbose:
        _msg = [_v for _v in _obsp.observing_night_jd_r]
        _msg.sort()
        for _k in _msg:
            pdh(f"{_obsp.observing_night_jd_r.get(_k, '---')[:-3].replace('_', ' '):20s}: {jd_to_isot(_k)[:-7]}",
                color='cyan')

    # +
    # evening dark(s), typically and hour or so before sunset
    # -
    _dark_end_iso, _dark_end_jd = _dark.calculate(begin=jd_to_isot(_dark.night_start_jd - _dark.time_for_darks),
                                                  end=_dark.sun_set)
    if verbose:
        _dark.__darks_dump__()

    # +
    # evening flat(s), typically after sunset and before nautical dusk
    # -
    _flat_end_iso, _flat_end_jd = _flat.calculate(begin=_dark_end_iso, end=_flat.dusk_nautical)
    if verbose:
        _flat.__flats_dump__()

    # +
    # initial foci, typically after nautical dusk
    # -
    _foci_end_iso, _foci_end_jd = _foci.calculate(begin=_flat_end_iso,
                                                  end=jd_to_isot(_flat_end_jd + _foci.time_for_foci))
    if verbose:
        _foci.__foci_dump__()

    # foci - an example of widening the search area
    _foci.foci_cone_angle = 180.0
    if verbose:
        _foci.__dump__()
    _foci_end_iso, _foci_end_jd = _foci.calculate(begin=_foci_end_iso,
                                                  end=jd_to_isot(_foci_end_jd + _foci.time_for_foci))
    if verbose:
        _foci.__foci_dump__()

    # +
    # evening non-sidereal object(s), typically for half an hour or so at the start and end of night
    # -
    _nsid.non_sidereal_cone_angle = 90.0
    _nsid_end_iso, _nsid_end_jd = _nsid.calculate(begin=_foci_end_iso,
                                                  end=jd_to_isot(_foci_end_jd + _nsid.time_for_non_sidereal))
    if verbose:
        _nsid.__non_sidereal_dump__()

    # +
    # sidereal object(s), typically a 3-hour observing block
    # -
    _sid.sidereal_cone_angle = 180.0
    _sid_end_iso, _sid_end_jd = _sid.calculate(begin=_nsid_end_iso,
                                               end=jd_to_isot(_nsid_end_jd + _sid.time_for_sidereal))
    if verbose:
        _sid.__sidereal_dump__()

    # +
    # midnight foci, typically re-check focus around midnight
    # -
    _foci_end_iso, _foci_end_jd = _foci.calculate(begin=_sid_end_iso,
                                                  end=jd_to_isot(_sid_end_jd + _foci.time_for_foci))
    if verbose:
        _foci.__foci_dump__()

    # +
    # sidereal object(s), typically a 3-hour observing block
    # -
    _sid.sidereal_cone_angle = 180.0
    _sid_end_iso, _sid_end_jd = _sid.calculate(begin=_foci_end_iso,
                                               end=jd_to_isot(_foci_end_jd + _sid.time_for_sidereal))
    if verbose:
        _sid.__sidereal_dump__()

    # +
    # morning non-sidereal object(s), typically for half an hour or so before nautical dawn
    # -
    _nsid.non_sidereal_cone_angle = 180.0
    _nsid_end_iso, _nsid_end_jd = _nsid.calculate(begin=_sid_end_iso, end=_nsid.dawn_nautical)
    if verbose:
        _nsid.__non_sidereal_dump__()

    # +
    # morning flat(s), typically after nautical dawn but before sunrise
    # -
    _flat_end_iso, _flat_end_jd = _flat.calculate(begin=_flat.dawn_nautical, end=_flat.sun_rise)
    if verbose:
        _flat.__flats_dump__()

    # +
    # morning dark(s), typically an hour or so after sunrise
    # -
    _dark_end_iso, _dark_end_jd = _dark.calculate(begin=_flat_end_iso,
                                                  end=jd_to_isot(_dark.sun_rise_jd + _dark.time_for_darks))
    if verbose:
        _dark.__darks_dump__()

    # end-of-night message
    pdh(f"{_tel.name} telescope observing schedule for {_obsp.mst.split('T')[0]}".upper(), color='green')


# +
# main()
# -
if __name__ == '__main__':

    # get command line argument(s)
    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'ARTN Telescope Scheduler', 
                                 formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--instrument', default='Mont4k',
                    help=f"""Instrument, defaults to '%(default)s', choices: {TEL__INSTRUMENTS}""")
    _p.add_argument(f'--telescope', default=f'Kuiper',
                    help=f"""Telescope, defaults to '%(default)s', choices: {TEL__TELESCOPES}""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce verbose output')
    args = _p.parse_args()
    artn_schedule(instrument=args.instrument, telescope=args.telescope, verbose=bool(args.verbose))
