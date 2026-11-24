from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IAMGetHumanReadableSummaryResponse(BaseModel):
    SummaryContent: StrictStr | None = None
    Locale: StrictStr | None = None
    SummaryState: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
