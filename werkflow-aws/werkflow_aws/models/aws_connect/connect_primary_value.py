from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPrimaryValue(BaseModel):
    AttributeName: StrictStr | None = None
    Value: StrictStr | None = None
