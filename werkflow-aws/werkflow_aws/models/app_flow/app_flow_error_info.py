from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppFlowErrorInfo(BaseModel):
    putFailuresCount: StrictInt | None = None
    executionMessage: StrictStr | None = None
