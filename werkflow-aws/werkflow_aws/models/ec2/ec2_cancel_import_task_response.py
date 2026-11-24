from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2CancelImportTaskResponse(BaseModel):
    ImportTaskId: StrictStr | None = None
    PreviousState: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
