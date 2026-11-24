from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAttributeValueTarget(BaseModel):
    AttributeValue: StrictStr | None = None
