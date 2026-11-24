from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateTaskTemplateResponse(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
