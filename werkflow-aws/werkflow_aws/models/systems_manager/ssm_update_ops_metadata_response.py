from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMUpdateOpsMetadataResponse(BaseModel):
    OpsMetadataArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
