from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyServiceQuotaExceededException(BaseModel):
    message: StrictStr | None = None
    quotaCode: StrictStr | None = None
    serviceCode: StrictStr | None = None
