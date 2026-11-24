from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MacieDetection(BaseModel):
    arn: StrictStr | None = None
    count: StrictInt | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    suppressed: StrictBool | None = None
    type: StrictStr | None = None
