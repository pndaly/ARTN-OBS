#!/usr/bin/env python3


# +
#  import(s)
# -
from src.observations.darks import *
from src.observations.flats import *
from src.observations.foci import *
from src.observations.non_sidereal import *
from src.observations.obsparams import *
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

    # start-of-night message
    pdh(f"{_tel.name} telescope observing schedule for {_obsp.mst.split('T')[0]}".upper(), color='green')
    if verbose:
        _msg = [_v for _v in _obsp.observing_night_jd_r]
        _msg.sort()
        for _k in _msg:
            pdh(f"{_obsp.observing_night_jd_r.get(_k, '---')[:-3].replace('_', ' '):20s}: {jd_to_isot(_k)[:-7]}",
                color='cyan')

    # evening dark(s)
    _iso, _jd = _dark.calculate(begin=jd_to_isot(_obsp.night_start_jd - ObsParams.time_for_darks), end=_obsp.sun_set)
    if verbose:
        _dark.__dump__()

    # evening flat(s)
    _iso, _jd = _flat.calculate(begin=_iso, end=_obsp.dusk_nautical)
    if verbose:
        _flat.__dump__()

    # initial foci
    _iso, _jd = _foci.calculate(begin=_iso, end=jd_to_isot(_jd + ObsParams.time_for_foci))
    if verbose:
        _foci.__dump__()

    # evening non-sidereal object(s)
    _iso, _jd = _nsid.calculate(begin=_iso, end=jd_to_isot(_jd + ObsParams.time_for_non_sidereal))
    if verbose:
        _nsid.__dump__()

    # sidereal object(s)
    _iso, _jd = _sid.calculate(begin=_iso, end=jd_to_isot(_jd + ObsParams.time_for_sidereal))
    if verbose:
        _sid.__dump__()

    # midnight foci
    _iso, _jd = _foci.calculate(begin=_iso, end=jd_to_isot(_jd + ObsParams.time_for_foci))
    if verbose:
        _foci.__dump__()

    # sidereal object(s)
    _iso, _jd = _sid.calculate(begin=_iso, end=jd_to_isot(_jd + ObsParams.time_for_sidereal))
    if verbose:
        _sid.__dump__()

    # morning non-sidereal object(s)
    _iso, _jd = _nsid.calculate(begin=_iso, end=_obsp.dawn_nautical)
    if verbose:
        _nsid.__dump__()

    # morning flat(s)
    _iso, _jd = _flat.calculate(begin=_obsp.dawn_nautical, end=_obsp.sun_rise)
    if verbose:
        _flat.__dump__()

    # morning dark(s)
    _iso, _jd = _dark.calculate(begin=_iso, end=jd_to_isot(_obsp.sun_rise_jd + ObsParams.time_for_darks))
    if verbose:
        _dark.__dump__()

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
