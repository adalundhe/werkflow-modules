from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_group_members import KendraGroupMembers


class KendraPutPrincipalMappingRequest(BaseModel):
    IndexId: StrictStr
    GroupId: StrictStr
    GroupMembers: KendraGroupMembers
    DataSourceId: StrictStr | None = None
    OrderingId: StrictInt | None = None
    RoleArn: StrictStr | None = None
