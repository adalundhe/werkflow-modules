from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMListInventoryEntriesResponse(BaseModel):
    TypeName: StrictStr | None = None
    InstanceId: StrictStr | None = None
    SchemaVersion: StrictStr | None = None
    CaptureTime: StrictStr | None = None
    Entries: list[dict[StrictStr, StrictStr]] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
