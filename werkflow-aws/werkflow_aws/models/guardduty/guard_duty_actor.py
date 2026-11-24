from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_actor_process import GuardDutyActorProcess
from .guard_duty_session import GuardDutySession
from .guard_duty_user import GuardDutyUser


class GuardDutyActor(BaseModel):
    Id: StrictStr | None = None
    User: GuardDutyUser | None = None
    Session: GuardDutySession | None = None
    Process: GuardDutyActorProcess | None = None
