from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOpsItemDataValue(BaseModel):
    Value: StrictStr | None = None
    Type: StrictStr | None = None
