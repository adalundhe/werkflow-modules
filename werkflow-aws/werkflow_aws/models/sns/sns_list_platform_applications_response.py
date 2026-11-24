from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sns_platform_application import SNSPlatformApplication


class SNSListPlatformApplicationsResponse(BaseModel):
    PlatformApplications: list[SNSPlatformApplication] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
