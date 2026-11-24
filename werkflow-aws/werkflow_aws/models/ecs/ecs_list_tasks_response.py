from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ECSListTasksResponse(BaseModel):
    taskArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
