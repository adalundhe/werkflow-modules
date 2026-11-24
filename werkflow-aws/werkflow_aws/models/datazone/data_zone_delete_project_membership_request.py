from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_member import DataZoneMember


class DataZoneDeleteProjectMembershipRequest(BaseModel):
    domainIdentifier: StrictStr
    projectIdentifier: StrictStr
    member: DataZoneMember
