from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOpsEntityItem(BaseModel):
    CaptureTime: StrictStr | None = None
    Content: list[dict[StrictStr, StrictStr]] | None = None
