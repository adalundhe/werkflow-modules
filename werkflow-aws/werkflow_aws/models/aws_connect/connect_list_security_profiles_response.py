from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_security_profile_summary import ConnectSecurityProfileSummary


class ConnectListSecurityProfilesResponse(BaseModel):
    SecurityProfileSummaryList: list[ConnectSecurityProfileSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
