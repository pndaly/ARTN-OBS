#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.tests import *
from src.models.Models import *

import sqlalchemy


# +
# doc string(s)
# -
__doc__ = """
  % python3.7 -m pytest -p no:warnings test_models.py
"""


# +
# connect_database()
# -
def test_connect_database_0():
    with ptr(Exception):
        connect_database(url=random.choice(TEST_INVALID_INPUTS))


def test_connect_database_1():
    # noinspection PyUnresolvedReferences
    assert isinstance(connect_database(), sqlalchemy.orm.session.sessionmaker)


# +
# disconnect_database()
# -
def test_disconnect_database_0():
    with ptr(Exception):
        disconnect_database(session=random.choice(TEST_INVALID_INPUTS))


def test_disconnect_database_1():
    assert disconnect_database(session=connect_database()()) is None


# +
# obsreq_filters()
# -
def test_obsreq_filters_0():
    with ptr(Exception):
        obsreq_filters(query=random.choice(TEST_INVALID_INPUTS))


def test_obsreq_filters_1():
    with ptr(Exception):
        obsreq_filters(query=connect_database()().query(ObsReq),
                       request_args=random.choice(TEST_INVALID_INPUTS))


def test_obsreq_filters_2():
    # noinspection PyUnresolvedReferences
    assert isinstance(
        obsreq_filters(query=connect_database()().query(ObsReq), request_args={'username': get_hash()}),
        sqlalchemy.orm.query.Query)


def test_obsreq_filters_3():
    _q = connect_database()().query(ObsReq)
    _q = obsreq_filters(query=_q, request_args={'id__gte': 0})
    assert isinstance(ObsReq.serialize_list(_q.all())[0], dict)


# +
# user_filters()
# -
def test_user_filters_0():
    with ptr(Exception):
        user_filters(query=random.choice(TEST_INVALID_INPUTS))


def test_user_filters_1():
    with ptr(Exception):
        user_filters(query=connect_database()().query(User),
                     request_args=random.choice(TEST_INVALID_INPUTS))


def test_user_filters_2():
    # noinspection PyUnresolvedReferences
    assert isinstance(
        user_filters(query=connect_database()().query(User), request_args={'username': get_hash()}),
        sqlalchemy.orm.query.Query)


def test_user_filters_3():
    _q = connect_database()().query(User)
    _q = user_filters(query=_q, request_args={'id__gte': 0})
    assert isinstance(User.serialize_list(_q.all())[0], dict)
