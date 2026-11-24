from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAttribute(BaseModel):
    AttributeType: StrictStr | None = None
    Value: StrictStr | None = None
