from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisUpdateShardCountResponse(BaseModel):
    StreamName: StrictStr | None = None
    CurrentShardCount: StrictInt | None = None
    TargetShardCount: StrictInt | None = None
    StreamARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
