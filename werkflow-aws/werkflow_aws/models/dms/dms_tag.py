from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    ResourceArn: StrictStr | None = None
