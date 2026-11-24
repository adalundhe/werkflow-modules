from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectReference(BaseModel):
    Value: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    Arn: StrictStr | None = None
    StatusReason: StrictStr | None = None
