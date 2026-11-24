from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsErrorInfo(BaseModel):
    ErrorString: StrictStr | None = None
