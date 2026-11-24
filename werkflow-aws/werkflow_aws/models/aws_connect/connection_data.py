from __future__ import annotations
from pydantic import BaseModel
from .connect_attendee import ConnectAttendee
from .connect_meeting import ConnectMeeting


class ConnectionData(BaseModel):
    Attendee: ConnectAttendee | None = None
    Meeting: ConnectMeeting | None = None
