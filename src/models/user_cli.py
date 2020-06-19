#!/usr/bin/env python3


# +
# import(s)
# -
from src.models.Models import *

import argparse


# +
# doc
# -
__doc__ = """
    % python3.7 user_cli.py --help
"""


# +
# user_cli()
# -
# noinspection PyBroadException,PyPep8
def user_cli(iargs=None):

    # check input(s)
    if iargs is None:
        raise Exception(f'invalid input, iargs={iargs}')

    # set default(s)
    request_args = {}

    # get input(s)
    if iargs.id:
        request_args['id'] = f'{iargs.id}'
    if iargs.id__gte:
        request_args['id__gte'] = int(f'{iargs.id__gte}')
    if iargs.id__lte:
        request_args['id__lte'] = f'{iargs.id__lte}'
    if iargs.firstname:
        request_args['firstname'] = f'{iargs.firstname}'
    if iargs.lastname:
        request_args['lastname'] = f'{iargs.lastname}'
    if iargs.username:
        request_args['username'] = f'{iargs.username}'
    if iargs.email:
        request_args['email'] = f'{iargs.email}'
    if iargs.affiliation:
        request_args['affiliation'] = f'{iargs.affiliation}'
    if iargs.created_isot__gte:
        request_args['created_isot__gte'] = f'{iargs.created_isot__gte}'
    if iargs.created_isot__lte:
        request_args['created_isot__lte'] = f'{iargs.created_isot__lte}'
    if iargs.created_mjd__gte:
        request_args['created_mjd__gte'] = f'{iargs.created_mjd__gte}'
    if iargs.created_mjd__lte:
        request_args['created_mjd__lte'] = f'{iargs.created_mjd__lte}'
    if iargs.last_seen_isot__gte:
        request_args['last_seen_isot__gte'] = f'{iargs.last_seen_isot__gte}'
    if iargs.last_seen_isot__lte:
        request_args['last_seen_isot__lte'] = f'{iargs.last_seen_isot__lte}'
    if iargs.last_seen_mjd__gte:
        request_args['last_seen_mjd__gte'] = f'{iargs.last_seen_mjd__gte}'
    if iargs.last_seen_mjd__lte:
        request_args['last_seen_mjd__lte'] = f'{iargs.last_seen_mjd__lte}'
    if iargs.is_admin:
        request_args['is_admin'] = f'{iargs.is_admin}'
    if iargs.is_disabled:
        request_args['is_disabled'] = f'{iargs.is_disabled}'

    # connect to database
    db = connect_database()()

    # execute query
    query = None
    try:
        query = db.query(User)
        query = user_filters(query, request_args)
        query = query.order_by(User.id.desc())
    except:
        raise Exception(f'failed to execute query={query}')

    # output result(s)
    res = ''
    for _e in User.serialize_list(query.all()):
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
    # noinspection PyTypeChecker,PyTypeChecker,PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query User Database', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--id', help=f'id <int>')
    _p.add_argument(f'--id__gte', help=f'id >= <int>')
    _p.add_argument(f'--id__lte', help=f'id <= <int>')
    _p.add_argument(f'--firstname', help=f'firstname <str>')
    _p.add_argument(f'--lastname', help=f'lastname <str>')
    _p.add_argument(f'--username', help=f'username <str>')
    _p.add_argument(f'--email', help=f'email <str>')
    _p.add_argument(f'--affiliation', help=f'affiliation <str>')
    _p.add_argument(f'--created_isot__gte', help=f'created_isot >= <YYYY-MM-DD>')
    _p.add_argument(f'--created_isot__lte', help=f'created_isot <= <YYYY-MM-DD>')
    _p.add_argument(f'--created_mjd__gte', help=f'created_mjd >= <float>')
    _p.add_argument(f'--created_mjd__lte', help=f'created_mjd <= <float>')
    _p.add_argument(f'--last_seen_isot__gte', help=f'last_seen_isot >= <YYYY-MM-DD>')
    _p.add_argument(f'--last_seen_isot__lte', help=f'last_seen_isot <= <YYYY-MM-DD>')
    _p.add_argument(f'--last_seen_mjd__gte', help=f'last_seen_mjd >= <float>')
    _p.add_argument(f'--last_seen_mjd__lte', help=f'last_seen_mjd <= <float>')
    _p.add_argument(f'--is_admin', help=f'is_admin == <bool>')
    _p.add_argument(f'--is_disabled', help=f'is_disabled == <bool>')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')

    # execute
    _res = user_cli(_p.parse_args())
    print(f'{_res}')
