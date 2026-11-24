from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyClusterIamRolesRequest(BaseModel):
    ClusterIdentifier: StrictStr
    AddIamRoles: list[StrictStr] | None = None
    RemoveIamRoles: list[StrictStr] | None = None
    DefaultIamRoleArn: StrictStr | None = None
