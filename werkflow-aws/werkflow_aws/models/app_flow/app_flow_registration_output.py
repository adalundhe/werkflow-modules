from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowRegistrationOutput(BaseModel):
    message: StrictStr | None = None
    result: StrictStr | None = None
    status: StrictStr | None = None
