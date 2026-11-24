from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_work_group import AthenaWorkGroup


class AthenaGetWorkGroupResponse(BaseModel):
    WorkGroup: AthenaWorkGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
