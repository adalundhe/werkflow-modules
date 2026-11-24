from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .q_business_group_status_detail import QBusinessGroupStatusDetail


class QBusinessGetGroupResponse(BaseModel):
    status: QBusinessGroupStatusDetail | None = None
    statusHistory: list[QBusinessGroupStatusDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
