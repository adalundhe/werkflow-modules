from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2OperatorResponse(BaseModel):
    Managed: StrictBool | None = None
    Principal: StrictStr | None = None
    HiddenByDefault: StrictBool | None = None
