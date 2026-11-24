from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FSxCancelDataRepositoryTaskResponse(BaseModel):
    Lifecycle: StrictStr | None = None
    TaskId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
