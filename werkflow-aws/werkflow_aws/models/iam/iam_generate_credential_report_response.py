from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IAMGenerateCredentialReportResponse(BaseModel):
    State: StrictStr | None = None
    Description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
