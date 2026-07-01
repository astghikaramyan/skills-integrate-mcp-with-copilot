from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    schedule = Column(String(100), nullable=False)
    max_participants = Column(Integer, nullable=False)

    participants: List["Participant"] = relationship(
        "Participant",
        back_populates="activity",
        cascade="all, delete-orphan",
    )


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    email = Column(String(255), nullable=False)

    activity = relationship("Activity", back_populates="participants")
