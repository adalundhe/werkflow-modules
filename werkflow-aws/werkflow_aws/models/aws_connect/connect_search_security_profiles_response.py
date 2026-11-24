from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_security_profile_search_summary import ConnectSecurityProfileSearchSummary


class ConnectSearchSecurityProfilesResponse(BaseModel):
    SecurityProfiles: list[ConnectSecurityProfileSearchSummary] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
