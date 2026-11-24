from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetHumanReadableSummaryRequest(BaseModel):
    EntityArn: StrictStr
    Locale: StrictStr | None = None
