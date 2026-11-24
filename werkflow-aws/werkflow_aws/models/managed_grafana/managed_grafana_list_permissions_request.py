from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedGrafanaListPermissionsRequest(BaseModel):
    workspaceId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    userType: Literal['SSO_USER', 'SSO_GROUP'] | None = None
    userId: StrictStr | None = None
    groupId: StrictStr | None = None
