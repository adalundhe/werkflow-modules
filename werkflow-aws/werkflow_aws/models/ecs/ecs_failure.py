from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSFailure(BaseModel):
    arn: StrictStr | None = None
    reason: StrictStr | None = None
    detail: StrictStr | None = None
