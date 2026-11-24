from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AttributeValue(BaseModel):
    Value: StrictStr | None = None
