from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_login_attribute import GuardDutyLoginAttribute
from .guard_duty_remote_ip_details import GuardDutyRemoteIpDetails


class GuardDutyRdsLoginAttemptAction(BaseModel):
    RemoteIpDetails: GuardDutyRemoteIpDetails | None = None
    LoginAttributes: list[GuardDutyLoginAttribute] | None = None
