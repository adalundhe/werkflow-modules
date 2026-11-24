from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPrimaryValueResponse(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeId: StrictStr | None = None
    Value: StrictStr | None = None
