from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_error_detail import ResilienceHubErrorDetail


class ResilienceHubDescribeDraftAppVersionResourcesImportStatusResponse(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    errorDetails: list[ResilienceHubErrorDetail] | None = None
    errorMessage: StrictStr | None = None
    status: StrictStr | None = None
    statusChangeTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
