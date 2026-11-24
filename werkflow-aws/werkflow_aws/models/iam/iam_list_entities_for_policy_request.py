from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListEntitiesForPolicyRequest(BaseModel):
    PolicyArn: StrictStr
    EntityFilter: Literal['User', 'Role', 'Group', 'LocalManagedPolicy', 'AWSManagedPolicy'] | None = None
    PathPrefix: StrictStr | None = None
    PolicyUsageFilter: Literal['PermissionsPolicy', 'PermissionsBoundary'] | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
