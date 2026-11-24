from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieCreateMemberResponse(BaseModel):
    arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
