from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WorkSpacesModifyAccountResponse(BaseModel):
    Message: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
