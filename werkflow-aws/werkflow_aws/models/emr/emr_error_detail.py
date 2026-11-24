from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRErrorDetail(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorData: list[dict[StrictStr, StrictStr]] | None = None
    ErrorMessage: StrictStr | None = None
