from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2GetInstanceTpmEkPubResponse(BaseModel):
    InstanceId: StrictStr | None = None
    KeyType: StrictStr | None = None
    KeyFormat: StrictStr | None = None
    KeyValue: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
