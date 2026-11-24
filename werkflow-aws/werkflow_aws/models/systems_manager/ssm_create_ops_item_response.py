from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMCreateOpsItemResponse(BaseModel):
    OpsItemId: StrictStr | None = None
    OpsItemArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
