from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppVersionResourcesResolutionStatusResponse(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    errorMessage: StrictStr | None = None
    resolutionId: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
