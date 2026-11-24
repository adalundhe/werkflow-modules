from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMTargetPreview(BaseModel):
    Count: StrictInt | None = None
    TargetType: StrictStr | None = None
