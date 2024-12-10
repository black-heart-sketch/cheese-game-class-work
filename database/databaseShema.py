import datetime
from sqlalchemy import DateTime, ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import os

current_dir = os.getcwd()

engine = create_engine(f'sqlite:///{current_dir}/cheese_game.sqlite')

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Cheese(Base):
    __tablename__ = 'cheeses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    result = Column(String)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    
    player1 = relationship('Player', foreign_keys=[player1_id])
    player2 = relationship('Player', foreign_keys=[player2_id])
    moves = relationship('Move', back_populates='game')

class Move(Base):
    __tablename__ = 'moves'
    
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    move_description = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    game = relationship('Game', back_populates='moves')

# Create all tables in the engine
Base.metadata.create_all(engine)