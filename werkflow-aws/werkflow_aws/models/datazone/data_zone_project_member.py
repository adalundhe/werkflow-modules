from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_member_details import DataZoneMemberDetails


class DataZoneProjectMember(BaseModel):
    memberDetails: DataZoneMemberDetails | None = None
    designation: StrictStr | None = None
    userCreatedDesignationId: StrictStr | None = None
