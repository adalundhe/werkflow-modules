from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppVersionResponse(BaseModel):
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
