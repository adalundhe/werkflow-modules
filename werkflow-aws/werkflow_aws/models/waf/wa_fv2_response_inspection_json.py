from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2ResponseInspectionJson(BaseModel):
    Identifier: StrictStr | None = None
    SuccessValues: list[StrictStr] | None = None
    FailureValues: list[StrictStr] | None = None
