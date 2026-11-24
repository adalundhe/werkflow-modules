from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESMetricDataError(BaseModel):
    Id: StrictStr | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
