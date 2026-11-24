from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMInventoryResultItem(BaseModel):
    TypeName: StrictStr | None = None
    SchemaVersion: StrictStr | None = None
    CaptureTime: StrictStr | None = None
    ContentHash: StrictStr | None = None
    Content: list[dict[StrictStr, StrictStr]] | None = None
