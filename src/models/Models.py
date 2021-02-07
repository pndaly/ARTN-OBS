#!/usr/bin/env python3


# +
# import(s)
# -
from src import *
from sqlalchemy import not_
from sqlalchemy import func
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

import json
import sqlalchemy


# +
# constant(s)
# -
OBS_DB_URL = f'postgresql+psycopg2://{OBS_DB_USER}:{OBS_DB_PASS}@{OBS_DB_HOST}:{OBS_DB_PORT}/{OBS_DB_NAME}'


# +
# function: connect_database()
# -
# noinspection PyBroadException,PyPep8,PyPep8,PyPep8
def connect_database(url=OBS_DB_URL):
    """ returns a connection class to database """
    try:
        engine = create_engine(url)
        session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    except Exception as _e:
        raise Exception(f'invalid input, url={url}, error={_e}')
    return session


# +
# function: disconnect_database()
# -
# noinspection PyBroadException,PyPep8
def disconnect_database(session=None):
    """ disconnects from database """
    try:
        session.close()
    except Exception as _e:
        raise Exception(f'invalid input, session={session}, error={_e}')
    return None


# +
# initialize sqlalchemy
# -
Base = declarative_base()


# +
# class: ObsReq(), inherits from Base
# -
# noinspection PyUnresolvedReferences
class ObsReq(Base):

    # +
    # member variable(s)
    # -

    # define table name
    __tablename__ = 'obsreqs'
    _isot = get_isot()
    _mjd = float(isot_to_mjd(_isot))

    # +
    # table mapping
    # -
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), nullable=False)
    pi = Column(String(256), nullable=False)
    created_iso = Column(DateTime, default=_isot, nullable=False)
    created_mjd = Column(Float, default=_mjd, nullable=False)
    group_id = Column(String(128), default=get_hash(), nullable=False, unique=True)
    observation_id = Column(String(128), default=get_hash(), nullable=False, unique=True)
    priority = Column(String(16), default='Routine', nullable=False)
    priority_value = Column(Float, default=_mjd, nullable=False)
    object_name = Column(String(64), nullable=False)
    ra_hms = Column(String(16), nullable=False)
    ra_deg = Column(Float, default=math.nan, nullable=False)
    dec_dms = Column(String(16), nullable=False)
    dec_deg = Column(Float, default=math.nan, nullable=False)
    begin_iso = Column(DateTime, default=get_isot(), nullable=False)
    begin_mjd = Column(Float, default=_mjd, nullable=False)
    end_iso = Column(DateTime, default=get_isot(30), nullable=False)
    end_mjd = Column(Float, default=_mjd, nullable=False)
    airmass = Column(Float, default=1.0, nullable=False)
    lunarphase = Column(String(16), default='Dark', nullable=False)
    moonphase = Column(Float, default=0.0, nullable=False)
    photometric = Column(Boolean, default=False, nullable=False)
    guiding = Column(Boolean, default=False, nullable=False)
    non_sidereal = Column(Boolean, default=False, nullable=False)
    filter_name = Column(String(24), default='V', nullable=False)
    exp_time = Column(Float, default=0.0, nullable=False)
    num_exp = Column(Integer, default=1, nullable=False)
    binning = Column(String(16), default='Any', nullable=False)
    dither = Column(String(16), default='Any', nullable=False)
    cadence = Column(String(16), default='Any', nullable=False)
    telescope = Column(String(16), default='Any', nullable=False)
    instrument = Column(String(16), default='Any', nullable=False)
    rts2_doc = Column(JSONB, default={}, nullable=False)
    rts2_id = Column(Integer, default=-1, nullable=False)
    queued = Column(Boolean, default=False, nullable=False)
    queued_iso = Column(DateTime, default=get_isot(), nullable=False)
    queued_mjd = Column(Float, default=_mjd, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
    completed_iso = Column(DateTime, default=get_isot(), nullable=False)
    completed_mjd = Column(Float, default=_mjd, nullable=False)
    non_sidereal_json = Column(JSONB, default={}, nullable=False)

    # foreign key into another table
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # +
    # property: pretty_serialized()
    # -
    @property
    def pretty_serialized(self):
        return json.dumps(self.serialized(), indent=2)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'id': int(self.id),
            'username': self.username,
            'pi': self.pi,
            'created_iso': self.created_iso.isoformat(),
            'created_mjd': self.created_mjd,
            'group_id': self.group_id,
            'observation_id': self.observation_id,
            'priority': self.priority,
            'priority_value': self.priority_value,
            'object_name': self.object_name,
            'ra_hms': self.ra_hms,
            'ra_deg': self.ra_deg,
            'dec_dms': self.dec_dms,
            'dec_deg': self.dec_deg,
            'begin_iso': self.begin_iso.isoformat(),
            'begin_mjd': self.begin_mjd,
            'end_iso': self.end_iso.isoformat(),
            'end_mjd': self.end_mjd,
            'airmass': self.airmass,
            'lunarphase': self.lunarphase,
            'moonphase': self.moonphase,
            'photometric': True if str(self.photometric).lower() in OBS_TRUE_VALUES else False,
            'guiding': True if str(self.guiding).lower() in OBS_TRUE_VALUES else False,
            'non_sidereal': True if str(self.non_sidereal).lower() in OBS_TRUE_VALUES else False,
            'filter_name': self.filter_name,
            'exp_time': self.exp_time,
            'num_exp': self.num_exp,
            'binning': self.binning,
            'dither': self.dither,
            'cadence': self.cadence,
            'telescope': self.telescope,
            'instrument': self.instrument,
            'queued': True if str(self.queued).lower() in OBS_TRUE_VALUES else False,
            'queued_iso': self.queued_iso.isoformat(),
            'queued_mjd': self.queued_mjd,
            'completed': True if str(self.completed).lower() in OBS_TRUE_VALUES else False,
            'completed_iso': self.completed_iso.isoformat(),
            'completed_mjd': self.completed_mjd,
            'rts2_doc': str(self.rts2_doc),
            'rts2_id': self.rts2_id,
            'non_sidereal_json': str(self.non_sidereal_json),
            'user_id': self.user_id
        }

    # +
    # (overload) method: __repr__()
    # -
    def __repr__(self):
        _s = self.serialized()
        return f'<ObsReq {_s}>'

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(s_records):
        return [_s.serialized() for _s in s_records]


# +
# class: User(), inherits from Base
# -
# noinspection PyBroadException
class User(Base):

    # +
    # member variable(s)
    # -

    # define table name
    __tablename__ = 'users'
    _isot = get_isot()
    _mjd = isot_to_mjd(_isot)

    # +
    # table mapping
    # -
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(64), nullable=False)
    lastname = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    hashword = Column(String(128), nullable=False)
    passphrase = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    affiliation = Column(String(256), nullable=False)
    created_iso = Column(DateTime, default=_isot, nullable=False)
    created_mjd = Column(Float, default=_mjd, nullable=False)
    avatar = Column(String(128))
    about_me = Column(String(256))
    last_seen_iso = Column(DateTime, default=_isot, nullable=False)
    last_seen_mjd = Column(Float, default=_mjd, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_disabled = Column(Boolean, default=False, nullable=False)

    # back reference to another table
    obsreqs = relationship('ObsReq', backref='author', lazy='dynamic')

    # +
    # property: pretty_serialized()
    # -
    @property
    def pretty_serialized(self):
        return json.dumps(self.serialized(), indent=2)

    # +
    # method: get_avatar()
    # -
    def get_avatar(self, size=64):
        return f'{self.avatar}?d=identicon&s={size}'

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'id': int(self.id),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'hashword': self.hashword,
            'passphrase': self.passphrase,
            'email': self.email,
            'affiliation': self.affiliation,
            'created_iso': self.created_iso.isoformat(),
            'created_mjd': self.created_mjd,
            'avatar': self.avatar,
            'about_me': self.about_me,
            'last_seen_iso': self.last_seen_iso.isoformat(),
            'last_seen_mjd': self.last_seen_mjd,
            'is_admin': True if str(self.is_admin).lower() in OBS_TRUE_VALUES else False,
            'is_disabled': True if str(self.is_disabled).lower() in OBS_TRUE_VALUES else False
        }

    # +
    # (overload) method: __repr__()
    # -
    def __repr__(self):
        _s = self.serialized()
        return f'<Users {_s}>'

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(s_records):
        return [_s.serialized() for _s in s_records]


# +
# function: obsreq_filters()
# -
# noinspection PyBroadException
def obsreq_filters(query=None, request_args=None):

    # check input(s)
    if query is None or not isinstance(query, sqlalchemy.orm.query.Query):
        raise Exception(f'invalid input, query={query}')

    if request_args is None or not isinstance(request_args, dict) or request_args is {}:
        raise Exception(f'invalid input, request_args={request_args}')

    # obsreq records with id = value (API: ?id=20)
    if request_args.get('id'):
        query = query.filter(ObsReq.id == int(request_args['id']))

    # obsreq records with id <= value (API: ?id__lte=20)
    if request_args.get('id__lte'):
        query = query.filter(ObsReq.id <= int(request_args['id__lte']))

    # obsreq records with id >= value (API: ?id__gte=20)
    if request_args.get('id__gte'):
        query = query.filter(ObsReq.id >= int(request_args['id__gte']))

    # obsreq records with username like value (API: ?username=demo)
    if request_args.get('username'):
        query = query.filter(ObsReq.username.ilike(f"%{request_args['username']}%"))

    # obsreq records with username not like value (API: ?exclude_username=demo)
    if request_args.get('exclude_username'):
        query = query.filter(not_(ObsReq.username.ilike(f"%{request_args['exclude_username']}%")))

    # obsreq records with pi like value (API: ?pi=demo)
    if request_args.get('pi'):
        query = query.filter(ObsReq.pi.ilike(f"%{request_args['pi']}%"))

    # obsreq records with a created_iso >= date (API: ?created_iso__gte=2018-07-17)
    if request_args.get('created_iso__gte'):
        a_time = Time(request_args['created_iso__gte'], format='isot')
        query = query.filter(ObsReq.created_mjd >= float(a_time.mjd))

    # obsreq records with a created_iso <= date (API: ?created_iso__lte=2018-07-17)
    if request_args.get('created_iso__lte'):
        a_time = Time(request_args['created_iso__lte'], format='isot')
        query = query.filter(ObsReq.created_mjd <= float(a_time.mjd))

    # obsreq records with created_mjd >= value (API: ?created_mjd__gte=58526.54609935184998903)
    if request_args.get('created_mjd__gte'):
        query = query.filter(ObsReq.created_mjd >= float(request_args['created_mjd__gte']))

    # obsreq records with created_mjd <= value (API: ?created_mjd__lte=58526.54609935184998903)
    if request_args.get('created_mjd__lte'):
        query = query.filter(ObsReq.created_mjd <= float(request_args['created_mjd__lte']))

    # obsreq records with group_id like value (API: ?group_id=abcd)
    if request_args.get('group_id'):
        query = query.filter(ObsReq.group_id.ilike(f"%{request_args['group_id']}%"))

    # obsreq records with observation_id like value (API: ?observation_id=abcd)
    if request_args.get('observation_id'):
        query = query.filter(ObsReq.observation_id.ilike(f"%{request_args['observation_id']}%"))

    # obsreq records with priority like value (API: ?priority=Routine)
    if request_args.get('priority'):
        query = query.filter(ObsReq.priority.ilike(f"%{request_args['priority']}%"))

    # obsreq records with priority_value >= value (API: ?priority_value__gte=58526.54609935184998903)
    if request_args.get('priority_value__gte'):
        query = query.filter(ObsReq.priority_value >= float(request_args['priority_value__gte']))

    # obsreq records with priority_value <= value (API: ?priority_value__lte=58526.54609935184998903)
    if request_args.get('priority_value__lte'):
        query = query.filter(ObsReq.priority_value <= float(request_args['priority_value__lte']))

    # obsreq records with object_name like value (API: ?object_name=abcd)
    if request_args.get('object_name'):
        query = query.filter(ObsReq.object_name.ilike(f"%{request_args['object_name']}%"))

    # obsreq records with ra_hms like value (API: ?ra_hms=12:12:12)
    if request_args.get('ra_hms'):
        query = query.filter(ObsReq.ra_hms.ilike(f"%{request_args['ra_hms']}%"))

    # obsreq records with ra_deg >= value (API: ?ra_deg__gte=58526.54609935184998903)
    if request_args.get('ra_deg__gte'):
        query = query.filter(ObsReq.ra_deg >= float(request_args['ra_deg__gte']))

    # obsreq records with ra_deg <= value (API: ?ra_deg__lte=58526.54609935184998903)
    if request_args.get('ra_deg__lte'):
        query = query.filter(ObsReq.ra_deg <= float(request_args['ra_deg__lte']))

    # obsreq records with dec_dms like value (API: ?dec_dms=30:30:30)
    if request_args.get('dec_dms'):
        query = query.filter(ObsReq.dec_dms.ilike(f"%{request_args['dec_dms']}%"))

    # obsreq records with dec_deg >= value (API: ?dec_deg__gte=58526.54609935184998903)
    if request_args.get('dec_deg__gte'):
        query = query.filter(ObsReq.dec_deg >= float(request_args['dec_deg__gte']))

    # obsreq records with dec_deg >= value (API: ?dec_deg__lte=58526.54609935184998903)
    if request_args.get('dec_deg__lte'):
        query = query.filter(ObsReq.dec_deg <= float(request_args['dec_deg__lte']))

    # obsreq records with a begin_iso >= date (API: ?begin_iso__gte=2018-07-17)
    if request_args.get('begin_iso__gte'):
        a_time = Time(request_args['begin_iso__gte'], format='isot')
        query = query.filter(ObsReq.begin_mjd >= float(a_time.mjd))

    # obsreq records with a begin_iso <= date (API: ?begin_iso__lte=2018-07-17)
    if request_args.get('begin_iso__lte'):
        a_time = Time(request_args['begin_iso__lte'], format='isot')
        query = query.filter(ObsReq.begin_mjd <= float(a_time.mjd))

    # obsreq records with begin_mjd >= value (API: ?begin_mjd__gte=58526.54609935184998903)
    if request_args.get('begin_mjd__gte'):
        query = query.filter(ObsReq.begin_mjd >= float(request_args['begin_mjd__gte']))

    # obsreq records with begin_mjd <= value (API: ?begin_mjd__lte=58526.54609935184998903)
    if request_args.get('begin_mjd__lte'):
        query = query.filter(ObsReq.begin_mjd <= float(request_args['begin_mjd__lte']))

    # obsreq records with a end_iso >= date (API: ?end_iso__gte=2018-07-17)
    if request_args.get('end_iso__gte'):
        a_time = Time(request_args['end_iso__gte'], format='isot')
        query = query.filter(ObsReq.end_mjd >= float(a_time.mjd))

    # obsreq records with a end_iso <= date (API: ?end_iso__lte=2018-07-17)
    if request_args.get('end_iso__lte'):
        a_time = Time(request_args['end_iso__lte'], format='isot')
        query = query.filter(ObsReq.end_mjd <= float(a_time.mjd))

    # obsreq records with end_mjd >= value (API: ?end_mjd__gte=58526.54609935184998903)
    if request_args.get('end_mjd__gte'):
        query = query.filter(ObsReq.end_mjd >= float(request_args['end_mjd__gte']))

    # obsreq records with end_mjd <= value (API: ?end_mjd__lte=58526.54609935184998903)
    if request_args.get('end_mjd__lte'):
        query = query.filter(ObsReq.end_mjd <= float(request_args['end_mjd__lte']))

    # obsreq records with airmass >= value (API: ?airmass__gte=58526.54609935184998903)
    if request_args.get('airmass__gte'):
        query = query.filter(ObsReq.airmass >= float(request_args['airmass__gte']))

    # obsreq records with airmass <= value (API: ?airmass__lte=58526.54609935184998903)
    if request_args.get('airmass__lte'):
        query = query.filter(ObsReq.airmass <= float(request_args['airmass__lte']))

    # obsreq records with lunarphase like value (API: ?lunarphase=Dark)
    if request_args.get('lunarphase'):
        query = query.filter(ObsReq.lunarphase.ilike(f"%{request_args['lunarphase']}%"))

    # obsreq records with moonphase >= value (API: ?moonphase__gte=58526.54609935184998903)
    if request_args.get('moonphase__gte'):
        query = query.filter(ObsReq.moonphase >= float(request_args['moonphase__gte']))

    # obsreq records with moonphase <= value (API: ?moonphase__lte=58526.54609935184998903)
    if request_args.get('moonphase__lte'):
        query = query.filter(ObsReq.moonphase <= float(request_args['moonphase__lte']))

    # obsreq records with photometric = boolean (API: ?photometric=True)
    if request_args.get('photometric'):
        query = query.filter(ObsReq.photometric == request_args.get('photometric').lower() in OBS_TRUE_VALUES)

    # obsreq records with guiding = boolean (API: ?guiding=True)
    if request_args.get('guiding'):
        query = query.filter(ObsReq.guiding == request_args.get('guiding').lower() in OBS_TRUE_VALUES)

    # obsreq records with non_sidereal = boolean (API: ?non_sidereal=True)
    if request_args.get('non_sidereal'):
        query = query.filter(ObsReq.non_sidereal == request_args.get('non_sidereal').lower() in OBS_TRUE_VALUES)

    # obsreq records with filter_name like value (API: ?filter=V)
    if request_args.get('filter_name'):
        query = query.filter(ObsReq.filter_name.ilike(f"%{request_args['filter_name']}%"))

    # obsreq records with exp_time >= value (API: ?exp_time__gte=58526.54609935184998903)
    if request_args.get('exp_time__gte'):
        query = query.filter(ObsReq.exp_time >= float(request_args['exp_time__gte']))

    # obsreq records with exp_time <= value (API: ?exp_time__lte=58526.54609935184998903)
    if request_args.get('exp_time__lte'):
        query = query.filter(ObsReq.exp_time <= float(request_args['exp_time__lte']))

    # obsreq records with num_exp >= value (API: ?num_exp__gte=20)
    if request_args.get('num_exp__gte'):
        query = query.filter(ObsReq.num_exp >= int(request_args['num_exp__gte']))

    # obsreq records with num_exp <= value (API: ?num_exp__lte=20)
    if request_args.get('num_exp__lte'):
        query = query.filter(ObsReq.num_exp <= int(request_args['num_exp__lte']))

    # obsreq records with binning like value (API: ?binning=1x1)
    if request_args.get('binning'):
        query = query.filter(ObsReq.binning.ilike(f"%{request_args['binning']}%"))

    # obsreq records with dither like value (API: ?dither=1x1)
    if request_args.get('dither'):
        query = query.filter(ObsReq.dither.ilike(f"%{request_args['dither']}%"))

    # obsreq records with cadence like value (API: ?cadence=Once)
    if request_args.get('cadence'):
        query = query.filter(ObsReq.cadence.ilike(f"%{request_args['cadence']}%"))

    # obsreq records with telescope like value (API: ?telescope=Kuiper)
    if request_args.get('telescope'):
        query = query.filter(ObsReq.telescope.ilike(f"%{request_args['telescope']}%"))

    # obsreq records with instrument like value (API: ?instrument=Mont4k)
    if request_args.get('instrument'):
        query = query.filter(ObsReq.instrument.ilike(f"%{request_args['instrument']}%"))

    # obsreq records with queued = boolean (API: ?queued=True)
    if request_args.get('queued'):
        query = query.filter(ObsReq.queued == request_args.get('queued').lower() in OBS_TRUE_VALUES)

    # obsreq records with a queued_iso >= date (API: ?queued_iso__gte=2018-07-17)
    if request_args.get('queued_iso__gte'):
        a_time = Time(request_args['queued_iso__gte'], format='isot')
        query = query.filter(ObsReq.queued_mjd >= float(a_time.mjd))

    # obsreq records with a queued_iso <= date (API: ?queued_iso__lte=2018-07-17)
    if request_args.get('queued_iso__lte'):
        a_time = Time(request_args['queued_iso__lte'], format='isot')
        query = query.filter(ObsReq.queued_mjd <= float(a_time.mjd))

    # obsreq records with queued_mjd >= value (API: ?queued_mjd__gte=58526.54609935184998903)
    if request_args.get('queued_mjd__gte'):
        query = query.filter(ObsReq.queued_mjd >= float(request_args['queued_mjd__gte']))

    # obsreq records with queued_mjd <= value (API: ?queued_mjd__lte=58526.54609935184998903)
    if request_args.get('queued_mjd__lte'):
        query = query.filter(ObsReq.queued_mjd <= float(request_args['queued_mjd__lte']))

    # obsreq records with completed = boolean (API: ?completed=True)
    if request_args.get('completed'):
        query = query.filter(ObsReq.completed == request_args.get('completed').lower() in OBS_TRUE_VALUES)

    # obsreq records with a completed_iso >= date (API: ?completed_iso__gte=2018-07-17)
    if request_args.get('completed_iso__gte'):
        a_time = Time(request_args['completed_iso__gte'], format='isot')
        query = query.filter(ObsReq.completed_mjd >= float(a_time.mjd))

    # obsreq records with a completed_iso <= date (API: ?completed_iso__lte=2018-07-17)
    if request_args.get('completed_iso__lte'):
        a_time = Time(request_args['completed_iso__lte'], format='isot')
        query = query.filter(ObsReq.completed_mjd <= float(a_time.mjd))

    # obsreq records with completed_mjd >= value (API: ?completed_mjd__gte=58526.54609935184998903)
    if request_args.get('completed_mjd__gte'):
        query = query.filter(ObsReq.completed_mjd >= float(request_args['completed_mjd__gte']))

    # obsreq records with completed_mjd <= value (API: ?completed_mjd__lte=58526.54609935184998903)
    if request_args.get('completed_mjd__lte'):
        query = query.filter(ObsReq.completed_mjd <= float(request_args['completed_mjd__lte']))

    # obsreq records with rts2_doc__key (API: ?rts2_doc__key=obs_info)
    if request_args.get('rts2_doc__key'):
        query = query.filter(ObsReq.rts2_doc[f"{request_args['rts2_doc__key']}"].astext != '')

    # obsreq records with rts2_id = value (API: ?rts2_id=20)
    if request_args.get('rts2_id'):
        query = query.filter(ObsReq.rts2_id == int(request_args['rts2_id']))

    # obsreq records with rts2_id <= value (API: ?rts2_id__lte=20)
    if request_args.get('rts2_id__lte'):
        query = query.filter(ObsReq.rts2_id <= int(request_args['rts2_id__lte']))

    # obsreq records with rts2_id >= value (API: ?rts2_id__gte=20)
    if request_args.get('rts2_id__gte'):
        query = query.filter(ObsReq.rts2_id >= int(request_args['rts2_id__gte']))

    # obsreq records with non_sidereal__key (API: ?non_sidereal__key=RA_BiasRate)
    if request_args.get('non_sidereal__key'):
        query = query.filter(ObsReq.non_sidereal_json[f"{request_args['non_sidereal__key']}"].astext != '')

    # obsreq records with user_id = value (API: ?user_id=20)
    if request_args.get('user_id'):
        query = query.filter(ObsReq.user_id == int(request_args['user_id']))

    # obsreq records with user_id <= value (API: ?user_id__lte=20)
    if request_args.get('user_id__lte'):
        query = query.filter(ObsReq.user_id <= int(request_args['user_id__lte']))

    # obsreq records with user_id >= value (API: ?user_id__gte=20)
    if request_args.get('user_id__gte'):
        query = query.filter(ObsReq.user_id >= int(request_args['user_id__gte']))

    # return records with astronomical cone search (API: ?astro=M51,25.0)
    if request_args.get('astro'):
        try:
            _nam, _rad = request_args['astro'].split(',')
            _ra, _dec = get_astropy_coords(_nam.strip().upper())
            query = query.filter(func.q3c_radial_query(ObsReq.ra_deg, ObsReq.dec_deg, _ra, _dec, float(_rad)))
        except Exception:
            pass

    # return records with cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = map(float, request_args['cone'].split(','))
            query = query.filter(func.q3c_radial_query(ObsReq.ra_deg, ObsReq.dec_deg, _ra, _dec, _rad))
        except Exception:
            pass

    # return records with elliptical cone search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = map(float, request_args['ellipse'].split(','))
            query = query.filter(
                func.q3c_ellipse_query(ObsReq.ra_deg, ObsReq.dec_deg, _ra, _dec, _maj, _rat, _pos))
        except Exception:
            pass

    # sort results
    if request_args.get('sort_field') and request_args.get('sort_order'):
        if request_args['sort_order'].lower() == 'descending':
            query = query.order_by(getattr(ObsReq, request_args['sort_field']).desc())
        else:
            query = query.order_by(getattr(ObsReq, request_args['sort_field']).asc())

    # return query
    return query


# +
# function: user_filters()
# -
def user_filters(query=None, request_args=None):

    # check input(s)
    if query is None or not isinstance(query, sqlalchemy.orm.query.Query):
        raise Exception(f'invalid input, query={query}')

    if request_args is None or not isinstance(request_args, dict) or request_args is {}:
        raise Exception(f'invalid input, request_args={request_args}')

    # user records with id = value (API: ?id=20)
    if request_args.get('id'):
        query = query.filter(User.id == int(request_args['id']))

    # user records with id >= value (API: ?id__gte=20)
    if request_args.get('id__gte'):
        query = query.filter(User.id >= int(request_args['id__gte']))

    # user records with id <= value (API: ?id__lte=20)
    if request_args.get('id__lte'):
        query = query.filter(User.id <= int(request_args['id__lte']))

    # user records with firstname like value (API: ?firstname=demo)
    if request_args.get('firstname'):
        query = query.filter(User.firstname.ilike(f"%{request_args['firstname']}%"))

    # user records with lastname like value (API: ?lastname=demo)
    if request_args.get('lastname'):
        query = query.filter(User.lastname.ilike(f"%{request_args['lastname']}%"))

    # user records with username like value (API: ?username=demo)
    if request_args.get('username'):
        query = query.filter(User.username.ilike(f"%{request_args['username']}%"))

    # user records with email like value (API: ?email=demo@example.com)
    if request_args.get('email'):
        query = query.filter(User.email.ilike(f"%{request_args['email']}%"))

    # user records with affiliation like value (API: ?affiliation='Example Inc')
    if request_args.get('affiliation'):
        query = query.filter(User.affiliation.ilike(f"%{request_args['affiliation']}%"))

    # user records with a created_iso >= date (API: ?created_iso__gte=2018-07-17)
    if request_args.get('created_iso__gte'):
        a_time = Time(request_args['created_iso__gte'], format='isot')
        query = query.filter(User.created_mjd >= float(a_time.mjd))

    # user records with a created_iso <= date (API: ?created_iso__lte=2018-07-17)
    if request_args.get('created_iso__lte'):
        a_time = Time(request_args['created_iso__lte'], format='isot')
        query = query.filter(User.created_mjd <= float(a_time.mjd))

    # user records with created_mjd >= value (API: ?created_mjd__gte=58526.54609935184998903)
    if request_args.get('created_mjd__gte'):
        query = query.filter(User.created_mjd >= float(request_args['created_mjd__gte']))

    # user records with created_mjd <= value (API: ?created_mjd__lte=58526.54609935184998903)
    if request_args.get('created_mjd__lte'):
        query = query.filter(User.created_mjd <= float(request_args['created_mjd__lte']))

    # user records with a last_seen_iso >= date (API: ?last_seen_iso__gte=2018-07-17)
    if request_args.get('last_seen_iso__gte'):
        a_time = Time(request_args['last_seen_iso__gte'], format='isot')
        query = query.filter(User.last_seen_mjd >= float(a_time.mjd))

    # user records with a last_seen_iso <= date (API: ?last_seen_iso__lte=2018-07-17)
    if request_args.get('last_seen_iso__lte'):
        a_time = Time(request_args['last_seen_iso__lte'], format='isot')
        query = query.filter(User.last_seen_mjd <= float(a_time.mjd))

    # user records with last_seen_mjd >= value (API: ?last_seen_mjd__gte=58526.54609935184998903)
    if request_args.get('last_seen_mjd__gte'):
        query = query.filter(User.last_seen_mjd >= float(request_args['last_seen_mjd__gte']))

    # user records with last_seen_mjd <= value (API: ?last_seen_mjd__lte=58526.54609935184998903)
    if request_args.get('last_seen_mjd__lte'):
        query = query.filter(User.last_seen_mjd <= float(request_args['last_seen_mjd__lte']))

    # user records with is_admin == bool (API: ?is_admin=True)
    if request_args.get('is_admin'):
        query = query.filter(User.is_admin == request_args.get('is_admin').lower() in OBS_TRUE_VALUES)

    # user records with is_disabled == bool (API: ?is_disabled=False)
    if request_args.get('is_disabled'):
        query = query.filter(User.is_disabled == request_args.get('is_disabled').lower() in OBS_TRUE_VALUES)

    # sort results
    if request_args.get('sort_field') and request_args.get('sort_order'):
        if request_args['sort_order'].lower() == 'descending':
            query = query.order_by(getattr(ObsReq, request_args['sort_field']).desc())
        else:
            query = query.order_by(getattr(ObsReq, request_args['sort_field']).asc())

    # return query
    return query
