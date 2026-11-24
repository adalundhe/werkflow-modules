from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_member import DataZoneMember


class DataZoneCreateProjectMembershipRequest(BaseModel):
    domainIdentifier: StrictStr
    projectIdentifier: StrictStr
    member: DataZoneMember
    designation: Literal['PROJECT_OWNER', 'PROJECT_CONTRIBUTOR', 'PROJECT_CATALOG_VIEWER', 'PROJECT_CATALOG_CONSUMER', 'PROJECT_CATALOG_STEWARD', 'USER_CREATED_DESIGNATION']
    userCreatedDesignationId: StrictStr | None = None
