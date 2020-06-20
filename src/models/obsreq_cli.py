#!/usr/bin/env python3


# +
# import(s)
# -
from src.models.Models import *

import argparse


# +
# __doc__ string
# -
__doc__ = """
    % python3.7 obsreq_cli.py --help
"""


# +
# obsreq_cli()
# -
# noinspection PyBroadException,PyPep8
def obsreq_cli(iargs=None):

    # check input(s)
    if iargs is None:
        raise Exception(f'invalid input, iargs={iargs}')

    # set default(s)
    request_args = {}

    # get input(s)
    if iargs.id:
        request_args['id'] = f'{iargs.id}'
    if iargs.id__gte:
        request_args['id__gte'] = f'{iargs.id__gte}'
    if iargs.id__lte:
        request_args['id__lte'] = f'{iargs.id__lte}'
    if iargs.username:
        request_args['username'] = f'{iargs.username}'
    if iargs.exclude_username:
        request_args['exclude_username'] = f'{iargs.exclude_username}'
    if iargs.pi:
        request_args['pi'] = f'{iargs.pi}'
    if iargs.created_iso__gte:
        request_args['created_iso__gte'] = f'{iargs.created_iso__gte}'
    if iargs.created_iso__lte:
        request_args['created_iso__lte'] = f'{iargs.created_iso__lte}'
    if iargs.created_mjd__gte:
        request_args['created_mjd__gte'] = f'{iargs.created_mjd__gte}'
    if iargs.created_mjd__lte:
        request_args['created_mjd__lte'] = f'{iargs.created_mjd__lte}'
    if iargs.group_id:
        request_args['group_id'] = f'{iargs.group_id}'
    if iargs.observation_id:
        request_args['observation_id'] = f'{iargs.observation_id}'
    if iargs.priority:
        request_args['priority'] = f'{iargs.priority}'
    if iargs.priority_value__gte:
        request_args['priority_value__gte'] = f'{iargs.priority_value__gte}'
    if iargs.priority_value__lte:
        request_args['priority_value__lte'] = f'{iargs.priority_value__lte}'
    if iargs.object_name:
        request_args['object_name'] = f'{iargs.object_name}'
    if iargs.ra_hms:
        request_args['ra_hms'] = f'{iargs.ra_hms}'
    if iargs.ra_deg__gte:
        request_args['ra_deg__gte'] = f'{iargs.ra_deg__gte}'
    if iargs.ra_deg__lte:
        request_args['ra_deg__lte'] = f'{iargs.ra_deg__lte}'
    if iargs.dec_dms:
        request_args['dec_dms'] = f'{iargs.dec_dms}'
    if iargs.dec_deg__gte:
        request_args['dec_deg__gte'] = f'{iargs.dec_deg__gte}'
    if iargs.dec_deg__lte:
        request_args['dec_deg__lte'] = f'{iargs.dec_deg__lte}'
    if iargs.begin_iso__gte:
        request_args['begin_iso__gte'] = f'{iargs.begin_iso__gte}'
    if iargs.begin_iso__lte:
        request_args['begin_iso__lte'] = f'{iargs.begin_iso__lte}'
    if iargs.begin_mjd__gte:
        request_args['begin_mjd__gte'] = f'{iargs.begin_mjd__gte}'
    if iargs.begin_mjd__lte:
        request_args['begin_mjd__lte'] = f'{iargs.begin_mjd__lte}'
    if iargs.end_iso__gte:
        request_args['end_iso__gte'] = f'{iargs.end_iso__gte}'
    if iargs.end_iso__lte:
        request_args['end_iso__lte'] = f'{iargs.end_iso__lte}'
    if iargs.end_mjd__gte:
        request_args['end_mjd__gte'] = f'{iargs.end_mjd__gte}'
    if iargs.end_mjd__lte:
        request_args['end_mjd__lte'] = f'{iargs.end_mjd__lte}'
    if iargs.airmass__gte:
        request_args['airmass__gte'] = f'{iargs.airmass__gte}'
    if iargs.airmass__lte:
        request_args['airmass__lte'] = f'{iargs.airmass__lte}'
    if iargs.lunarphase:
        request_args['lunarphase'] = f'{iargs.lunarphase}'
    if iargs.moonphase__gte:
        request_args['moonphase__gte'] = f'{iargs.moonphase__gte}'
    if iargs.moonphase__lte:
        request_args['moonphase__lte'] = f'{iargs.moonphase__lte}'
    if iargs.photometric:
        request_args['photometric'] = f'{iargs.photometric}'
    if iargs.guiding:
        request_args['guiding'] = f'{iargs.guiding}'
    if iargs.non_sidereal:
        request_args['non_sidereal'] = f'{iargs.non_sidereal}'
    if iargs.filter_name:
        request_args['filter_name'] = f'{iargs.filter_name}'
    if iargs.exp_time__gte:
        request_args['exp_time__gte'] = f'{iargs.exp_time__gte}'
    if iargs.exp_time__lte:
        request_args['exp_time__lte'] = f'{iargs.exp_time__lte}'
    if iargs.num_exp__gte:
        request_args['num_exp__gte'] = f'{iargs.num_exp__gte}'
    if iargs.num_exp__lte:
        request_args['num_exp__lte'] = f'{iargs.num_exp__lte}'
    if iargs.binning:
        request_args['binning'] = f'{iargs.binning}'
    if iargs.dither:
        request_args['dither'] = f'{iargs.dither}'
    if iargs.cadence:
        request_args['cadence'] = f'{iargs.cadence}'
    if iargs.telescope:
        request_args['telescope'] = f'{iargs.telescope}'
    if iargs.instrument:
        request_args['instrument'] = f'{iargs.instrument}'
    if iargs.queued:
        request_args['queued'] = f'{iargs.queued}'
    if iargs.queued_iso__gte:
        request_args['queued_iso__gte'] = f'{iargs.queued_iso__gte}'
    if iargs.queued_iso__lte:
        request_args['queued_iso__lte'] = f'{iargs.queued_iso__lte}'
    if iargs.queued_mjd__gte:
        request_args['queued_mjd__gte'] = f'{iargs.queued_mjd__gte}'
    if iargs.queued_mjd__lte:
        request_args['queued_mjd__lte'] = f'{iargs.queued_mjd__lte}'
    if iargs.completed:
        request_args['completed'] = f'{iargs.completed}'
    if iargs.completed_iso__gte:
        request_args['completed_iso__gte'] = f'{iargs.completed_iso__gte}'
    if iargs.completed_iso__lte:
        request_args['completed_iso__lte'] = f'{iargs.completed_iso__lte}'
    if iargs.completed_mjd__gte:
        request_args['completed_mjd__gte'] = f'{iargs.completed_mjd__gte}'
    if iargs.completed_mjd__lte:
        request_args['completed_mjd__lte'] = f'{iargs.completed_mjd__lte}'
    if iargs.rts2_doc__key:
        request_args['rts2_doc__key'] = f'{iargs.rts2_doc__key}'
    if iargs.rts2_id:
        request_args['rts2_id'] = f'{iargs.rts2_id}'
    if iargs.rts2_id__gte:
        request_args['rts2_id__gte'] = f'{iargs.rts2_id__gte}'
    if iargs.rts2_id__lte:
        request_args['rts2_id__lte'] = f'{iargs.rts2_id__lte}'
    if iargs.non_sidereal__key:
        request_args['non_sidereal__key'] = f'{iargs.non_sidereal__key}'
    if iargs.user_id:
        request_args['user_id'] = f'{iargs.user_id}'
    if iargs.user_id__gte:
        request_args['user_id__gte'] = f'{iargs.user_id__gte}'
    if iargs.user_id__lte:
        request_args['user_id__lte'] = f'{iargs.user_id__lte}'
    if iargs.astro:
        request_args['astro'] = f'{iargs.astro}'
    if iargs.cone:
        request_args['cone'] = f'{iargs.cone}'
    if iargs.ellipse:
        request_args['ellipse'] = f'{iargs.ellipse}'

    # connect to database
    db = connect_database()()

    # execute query
    query = None
    try:
        query = db.query(ObsReq)
        query = obsreq_filters(query, request_args)
        query = query.order_by(ObsReq.id.desc())
    except:
        raise Exception(f'failed to execute query={query}')

    # output result(s)
    res = ''
    for _e in ObsReq.serialize_list(query.all()):
        _s = ''.join("{}='{}' ".format(str(k), str(v)) for k, v in _e.items())[:-1]
        res = f'{res}\n{_s}'

    # return
    disconnect_database(db)
    return res[1:] if (res != '' and res[0] == '\n') else res


# +
# main()
# -
if __name__ == '__main__':

    # get command line argument(s)
    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(
        description=f'Query ObsReq Database', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--id', help=f'id = <int>')
    _p.add_argument(f'--id__gte', help=f'id >= <int>')
    _p.add_argument(f'--id__lte', help=f'id <= <int>')
    _p.add_argument(f'--username', help=f'username <str>')
    _p.add_argument(f'--exclude-username', help=f'exclude username <str>')
    _p.add_argument(f'--pi', help=f'pi <str>')
    _p.add_argument(f'--created_iso__gte', help=f'created_iso >= <YYYY-MM-DD>')
    _p.add_argument(f'--created_iso__lte', help=f'created_iso <= <YYYY-MM-DD>')
    _p.add_argument(f'--created_mjd__gte', help=f'created_mjd >= <float>')
    _p.add_argument(f'--created_mjd__lte', help=f'created_mjd <= <float>')
    _p.add_argument(f'--group_id', help=f'group_id <str>')
    _p.add_argument(f'--observation_id', help=f'observation_id <str>')
    _p.add_argument(f'--priority', help=f'priority <str>')
    _p.add_argument(f'--priority_value__gte', help=f'priority_value >= <float>')
    _p.add_argument(f'--priority_value__lte', help=f'priority_value <= <float>')
    _p.add_argument(f'--object_name', help=f'object_name <str>')
    _p.add_argument(f'--ra_hms', help=f'ra_hms <str>')
    _p.add_argument(f'--ra_deg__gte', help=f'ra_deg__gte >= <float>')
    _p.add_argument(f'--ra_deg__lte', help=f'ra_deg__lte <= <float>')
    _p.add_argument(f'--dec_dms', help=f'dec_dms <str>')
    _p.add_argument(f'--dec_deg__gte', help=f'dec_deg__gte >= <float>')
    _p.add_argument(f'--dec_deg__lte', help=f'dec_deg__lte <= <float>')
    _p.add_argument(f'--begin_iso__gte', help=f'begin_iso >= <YYYY-MM-DD>')
    _p.add_argument(f'--begin_iso__lte', help=f'begin_iso <= <YYYY-MM-DD>')
    _p.add_argument(f'--begin_mjd__gte', help=f'begin_mjd >= <float>')
    _p.add_argument(f'--begin_mjd__lte', help=f'begin_mjd <= <float>')
    _p.add_argument(f'--end_iso__gte', help=f'end_iso >= <YYYY-MM-DD>')
    _p.add_argument(f'--end_iso__lte', help=f'end_iso <= <YYYY-MM-DD>')
    _p.add_argument(f'--end_mjd__gte', help=f'end_mjd >= <float>')
    _p.add_argument(f'--end_mjd__lte', help=f'end_mjd <= <float>')
    _p.add_argument(f'--airmass__gte', help=f'airmass >= <float>')
    _p.add_argument(f'--airmass__lte', help=f'airmass <= <float>')
    _p.add_argument(f'--lunarphase', help=f'lunarphase <str>')
    _p.add_argument(f'--moonphase__gte', help=f'moonphase >= <float>')
    _p.add_argument(f'--moonphase__lte', help=f'moonphase <= <float>')
    _p.add_argument(f'--photometric', help=f'photometric == <bool>')
    _p.add_argument(f'--guiding', help=f'guiding == <bool>')
    _p.add_argument(f'--non_sidereal', help=f'non_sidereal == <bool>')
    _p.add_argument(f'--filter_name', help=f'filter_name <str>')
    _p.add_argument(f'--exp_time__gte', help=f'exp_time >= <float>')
    _p.add_argument(f'--exp_time__lte', help=f'exp_time <= <float>')
    _p.add_argument(f'--num_exp__lte', help=f'num_exp <= <int>')
    _p.add_argument(f'--num_exp__gte', help=f'num_exp >= <int>')
    _p.add_argument(f'--binning', help=f'binning <str>')
    _p.add_argument(f'--dither', help=f'dither <str>')
    _p.add_argument(f'--cadence', help=f'cadence <str>')
    _p.add_argument(f'--telescope', help=f'telescope <str>')
    _p.add_argument(f'--instrument', help=f'instrument <str>')
    _p.add_argument(f'--queued', help=f'queued == <bool>')
    _p.add_argument(f'--queued_iso__gte', help=f'queued_iso >= <YYYY-MM-DD>')
    _p.add_argument(f'--queued_iso__lte', help=f'queued_iso <= <YYYY-MM-DD>')
    _p.add_argument(f'--queued_mjd__gte', help=f'queued_mjd >= <float>')
    _p.add_argument(f'--queued_mjd__lte', help=f'queued_mjd <= <float>')
    _p.add_argument(f'--completed', help=f'completed == <bool>')
    _p.add_argument(f'--completed_iso__gte', help=f'completed_iso >= <YYYY-MM-DD>')
    _p.add_argument(f'--completed_iso__lte', help=f'completed_iso <= <YYYY-MM-DD>')
    _p.add_argument(f'--completed_mjd__gte', help=f'completed_mjd >= <float>')
    _p.add_argument(f'--completed_mjd__lte', help=f'completed_mjd <= <float>')
    _p.add_argument(f'--rts2_doc__key', help=f'rts2_doc key <str>')
    _p.add_argument(f'--rts2_id', help=f'rts2_id = <int>')
    _p.add_argument(f'--rts2_id__gte', help=f'rts2_id >= <int>')
    _p.add_argument(f'--rts2_id__lte', help=f'rts2_id <= <int>')
    _p.add_argument(f'--non_sidereal__key', help=f'non_sidereal_json key <str>')
    _p.add_argument(f'--user_id', help=f'user_id = <int>')
    _p.add_argument(f'--user_id__gte', help=f'user_id >= <int>')
    _p.add_argument(f'--user_id__lte', help=f'user_id <= <int>')
    _p.add_argument(f'--astro', help=f'Astronomical cone search <name,radius>')
    _p.add_argument(f'--cone', help=f'Cone search <ra,dec,radius>')
    _p.add_argument(f'--ellipse', help=f'Ellipse search <ra,dec,major_axis,axis_ratio,position_angle>')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')

    # execute
    _res = obsreq_cli(_p.parse_args())
    print(f'{_res}')
