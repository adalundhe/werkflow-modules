from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EMRStartSessionResponse(BaseModel):
    Id: StrictStr | None = None
    ClusterId: StrictStr | None = None
    Arn: StrictStr | None = None
    AccountId: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
