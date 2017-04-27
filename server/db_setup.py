from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, Text
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()


class MatchV1(Base):
	__tablename__ = 'MatchV1'
	pk = Column(Integer, primary_key=True)
	match_id = Column(String(36))
	event_name = Column(String(100))
	team_number = Column(Integer)
	match_number = Column(String(10))
	auto_line_cross = Column(Boolean)
	auto_low_goal = Column(Boolean)
	auto_hopper = Column(Boolean)
	auto_collect = Column(Boolean)
	auto_gear_pos = Column(String(10))
	auto_high_goal_pos = Column(String(10))
	climb_rating = Column(String(10))
	gear_rating = Column(String(10))
	total_gears = Column(Integer)
	gear_dispense_method = Column(String(15))
	got_gear_from_human = Column(Boolean)
	got_gear_from_floor = Column(Boolean)
	high_goal_rating = Column(String(10))
	high_goal_shoot_from_key = Column(Boolean)
	high_goal_shoot_from_wall = Column(Boolean)
	high_goal_shoot_from_afar = Column(Boolean)
	low_goal_rating = Column(String(10))
	total_hoppers = Column(Integer)
	collected_from_hopper = Column(Boolean)
	last_modified = Column(String(30))


class MatchV2(Base):
	__tablename__ = 'MatchV2'
	pk = Column(Integer, primary_key=True)
	match_id = Column(String(36))
	event_name = Column(String(100))
	team_number = Column(Integer)
	match_number = Column(Integer)
	auto_line_cross = Column(Boolean)
	auto_low_goal = Column(Boolean)
	auto_hopper = Column(Boolean)
	auto_collect = Column(Boolean)
	auto_gear_pos = Column(String(10))
	auto_high_goal_pos = Column(String(10))
	climb_rating = Column(String(10))
	gear_rating = Column(String(10))
	total_gears = Column(Integer)
	gear_dispense_method = Column(String(15))
	got_gear_from_human = Column(Boolean)
	got_gear_from_floor = Column(Boolean)
	high_goal_rating = Column(String(10))
	high_goal_shoot_from_key = Column(Boolean)
	high_goal_shoot_from_wall = Column(Boolean)
	high_goal_shoot_from_afar = Column(Boolean)
	low_goal_rating = Column(String(10))
	total_hoppers = Column(Integer)
	collected_from_hopper = Column(Boolean)
	last_modified = Column(String(30))


class MatchV3(Base):
	__tablename__ = 'MatchV3'
	pk = Column(Integer, primary_key=True)
	match_id = Column(String(36))
	event_name = Column(String(100))
	team_number = Column(Integer)
	match_number = Column(Integer)
	auto_line_cross = Column(Boolean)
	auto_low_goal = Column(Boolean)
	auto_hopper = Column(Boolean)
	auto_collect = Column(Boolean)
	auto_gear_pos = Column(String(10))
	auto_high_goal_pos = Column(String(10))
	climb_rating = Column(String(10))
	gear_rating = Column(String(10))
	total_gears = Column(Integer)
	gear_dispense_method = Column(String(15))
	got_gear_from_human = Column(Boolean)
	got_gear_from_floor = Column(Boolean)
	high_goal_rating = Column(String(10))
	high_goal_shoot_from_key = Column(Boolean)
	high_goal_shoot_from_wall = Column(Boolean)
	high_goal_shoot_from_afar = Column(Boolean)
	low_goal_rating = Column(String(10))
	total_hoppers = Column(Integer)
	collected_from_hopper = Column(Boolean)
	last_modified = Column(String(30))
	notes = Column(String(200))


class MatchV4(Base):
	__tablename__ = 'MatchV4'
	pk = Column(Integer, primary_key=True)
	match_id = Column(String(36))
	event_name = Column(String(100))
	team_number = Column(Integer)
	match_number = Column(Integer)
	auto_line_cross = Column(Boolean)
	auto_low_goal = Column(Boolean)
	auto_hopper = Column(Boolean)
	auto_collect = Column(Boolean)
	auto_gear_pos = Column(String(10))
	auto_high_goal_pos = Column(String(10))
	auto_kpa = Column(Integer)
	climb_rating = Column(String(10))
	gear_rating = Column(String(10))
	total_gears = Column(Integer)
	total_kpa = Column(Integer)
	gear_dispense_method = Column(String(15))
	got_gear_from_human = Column(Boolean)
	got_gear_from_floor = Column(Boolean)
	high_goal_rating = Column(String(10))
	high_goal_shoot_from_key = Column(Boolean)
	high_goal_shoot_from_wall = Column(Boolean)
	high_goal_shoot_from_afar = Column(Boolean)
	low_goal_rating = Column(String(10))
	total_hoppers = Column(Integer)
	collected_from_hopper = Column(Boolean)
	collected_fuel_from_floor = Column(Boolean)
	last_modified = Column(String(30))
	notes = Column(String(200))


class MatchV5(Base):
	__tablename__ = 'MatchV5'
	pk = Column(Integer, primary_key=True)
	match_id = Column(String(36))
	event_name = Column(String(100))
	team_number = Column(Integer)
	match_number = Column(Integer)
	auto_line_cross = Column(Boolean)
	auto_low_goal = Column(Boolean)
	auto_hopper = Column(Boolean)
	auto_collect = Column(Boolean)
	auto_gear_pos = Column(String(10))
	auto_high_goal_pos = Column(String(10))
	auto_kpa = Column(Integer)
	climb_rating = Column(String(10))
	gear_rating = Column(String(10))
	total_gears = Column(Integer)
	total_kpa = Column(Integer)
	gear_dispense_method = Column(String(15))
	got_gear_from_human = Column(Boolean)
	got_gear_from_floor = Column(Boolean)
	high_goal_rating = Column(String(10))
	high_goal_shoot_from_key = Column(Boolean)
	high_goal_shoot_from_wall = Column(Boolean)
	high_goal_shoot_from_afar = Column(Boolean)
	low_goal_rating = Column(String(10))
	total_hoppers = Column(Integer)
	collected_from_hopper = Column(Boolean)
	collected_fuel_from_floor = Column(Boolean)
	last_modified = Column(String(30))
	notes = Column(String(200))
	scout_name = Column(String(30))


class MatchV6(Base):
	__tablename__ = 'MatchV6'
	pk = Column(Integer, primary_key=True)
	match_id = Column(String(36))
	event_name = Column(Text())
	team_number = Column(Integer)
	match_number = Column(Integer)
	auto_line_cross = Column(Boolean)
	auto_low_goal = Column(Boolean)
	auto_hopper = Column(Boolean)
	auto_collect = Column(Boolean)
	auto_gear_pos = Column(Text())
	auto_high_goal_pos = Column(Text())
	auto_kpa = Column(Integer)
	climb_rating = Column(Text())
	gear_rating = Column(Text())
	total_gears = Column(Integer)
	total_kpa = Column(Integer)
	gear_dispense_method = Column(Text())
	got_gear_from_human = Column(Boolean)
	got_gear_from_floor = Column(Boolean)
	high_goal_rating = Column(Text())
	high_goal_shoot_from_key = Column(Boolean)
	high_goal_shoot_from_wall = Column(Boolean)
	high_goal_shoot_from_afar = Column(Boolean)
	low_goal_rating = Column(Text())
	total_hoppers = Column(Integer)
	collected_from_hopper = Column(Boolean)
	collected_fuel_from_floor = Column(Boolean)
	last_modified = Column(Text())
	notes = Column(Text())
	scout_name = Column(Text())


engine = create_engine(os.environ['db_address'])
Base.metadata.create_all(engine)
