from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPrimaryAttributeValue(BaseModel):
    AccessType: StrictStr | None = None
    AttributeName: StrictStr | None = None
    Values: list[StrictStr] | None = None
