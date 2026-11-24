from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMMetadataValue(BaseModel):
    Value: StrictStr | None = None
