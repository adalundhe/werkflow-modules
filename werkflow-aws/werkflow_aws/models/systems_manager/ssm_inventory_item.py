from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMInventoryItem(BaseModel):
    TypeName: StrictStr
    SchemaVersion: StrictStr
    CaptureTime: StrictStr
    ContentHash: StrictStr | None = None
    Content: list[dict[StrictStr, StrictStr]] | None = None
    Context: dict[StrictStr, StrictStr] | None = None
