from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_group_members import QBusinessGroupMembers


class QBusinessPutGroupRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    groupName: StrictStr
    type: Literal['INDEX', 'DATASOURCE']
    groupMembers: QBusinessGroupMembers
    dataSourceId: StrictStr | None = None
    roleArn: StrictStr | None = None
