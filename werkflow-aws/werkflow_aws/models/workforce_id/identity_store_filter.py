from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreFilter(BaseModel):
    AttributePath: StrictStr
    AttributeValue: StrictStr
