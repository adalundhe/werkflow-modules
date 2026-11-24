from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_security_profile_item import ConnectSecurityProfileItem


class ConnectListEntitySecurityProfilesResponse(BaseModel):
    SecurityProfiles: list[ConnectSecurityProfileItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
