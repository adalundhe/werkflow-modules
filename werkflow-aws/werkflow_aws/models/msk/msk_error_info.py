from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKErrorInfo(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorString: StrictStr | None = None
