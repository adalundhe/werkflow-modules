from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetAccountAuthorizationDetailsRequest(BaseModel):
    Filter: list[Literal['User', 'Role', 'Group', 'LocalManagedPolicy', 'AWSManagedPolicy']] | None = None
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
