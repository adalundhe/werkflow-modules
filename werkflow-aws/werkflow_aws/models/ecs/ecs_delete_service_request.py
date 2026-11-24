from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSDeleteServiceRequest(BaseModel):
    service: StrictStr
    cluster: StrictStr | None = None
    force: StrictBool | None = None
