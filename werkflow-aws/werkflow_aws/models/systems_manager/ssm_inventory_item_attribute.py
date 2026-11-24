from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMInventoryItemAttribute(BaseModel):
    Name: StrictStr | None = None
    DataType: StrictStr | None = None
