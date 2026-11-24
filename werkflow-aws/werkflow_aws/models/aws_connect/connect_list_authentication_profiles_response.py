from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_authentication_profile_summary import ConnectAuthenticationProfileSummary


class ConnectListAuthenticationProfilesResponse(BaseModel):
    AuthenticationProfileSummaryList: list[ConnectAuthenticationProfileSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
