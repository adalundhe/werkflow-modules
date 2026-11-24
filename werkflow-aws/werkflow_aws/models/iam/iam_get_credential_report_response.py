from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class IAMGetCredentialReportResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Content: StrictBytes | Any | None = None
    ReportFormat: StrictStr | None = None
    GeneratedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
