from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AccountAttributeValue(BaseModel):
    AttributeValue: StrictStr | None = None
