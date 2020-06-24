#!/usr/bin/env python3


# +
# import(s)
# -
from pytest import raises as ptr
from src.models.Models import *

import sqlalchemy


# +
# doc string(s)
# -
__doc__ = """
  % python3 -m pytest test_models.py
"""


# +
# test: connect_database()
# -
def test_connect_database_1():
    """ test connect_database() for incorrect input(s) """
    with ptr(Exception):
        connect_database(url=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_connect_database_2():
    """ test connect_database() for correct input(s) """
    assert isinstance(connect_database(), sqlalchemy.orm.session.sessionmaker) in OBS_TRUE_VALUES


# +
# test: disconnect_database()
# -
def test_disconnect_database_1():
    """ test disconnect_database() for incorrect input(s) """
    with ptr(Exception):
        disconnect_database(session=random.choice([None, get_hash(), {}, [], ()]))


def test_disconnect_database_2():
    """ test disconnect_database() for correct input(s) """
    assert disconnect_database(session=connect_database()()) is None


# +
# test: obsreq_filters()
# -
def test_obsreq_filters_1():
    """ test obsreq_filters() for incorrect input(s) """
    with ptr(Exception):
        obsreq_filters(query=random.choice([None, get_hash(), {}, [], ()]))


def test_obsreq_filters_2():
    """ test obsreq_filters() for incorrect input(s) """
    with ptr(Exception):
        obsreq_filters(query=connect_database()().query(ObsReq),
                       request_args=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_obsreq_filters_3():
    """ test obsreq_filters() for correct input(s) """
    assert isinstance(
        obsreq_filters(query=connect_database()().query(ObsReq), request_args={'username': get_hash()}),
        sqlalchemy.orm.query.Query) in OBS_TRUE_VALUES


def test_obsreq_filters_4():
    """ test obsreq_filters() returns dictionary of value(s) """
    _q = connect_database()().query(ObsReq)
    _q = obsreq_filters(query=_q, request_args={'id__gte': 0})
    assert isinstance(ObsReq.serialize_list(_q.all())[0], dict) in OBS_TRUE_VALUES


# +
# test: user_filters()
# -
def test_user_filters_1():
    """ test user_filters() for incorrect input(s) """
    with ptr(Exception):
        user_filters(query=random.choice([None, get_hash(), {}, [], ()]))


def test_user_filters_2():
    """ test user_filters() for incorrect input(s) """
    with ptr(Exception):
        user_filters(query=connect_database()().query(User),
                     request_args=random.choice([None, get_hash(), {}, [], ()]))


# noinspection PyUnresolvedReferences
def test_user_filters_3():
    """ test user_filters() for correct input(s) """
    assert isinstance(
        user_filters(query=connect_database()().query(User), request_args={'username': get_hash()}),
        sqlalchemy.orm.query.Query) in OBS_TRUE_VALUES


def test_user_filters_4():
    """ test user_filters() returns dictionary of value(s) """
    _q = connect_database()().query(User)
    _q = user_filters(query=_q, request_args={'id__gte': 0})
    assert isinstance(User.serialize_list(_q.all())[0], dict) in OBS_TRUE_VALUES
