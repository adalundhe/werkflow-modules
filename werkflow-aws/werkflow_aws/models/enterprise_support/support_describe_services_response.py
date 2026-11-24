from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_service import SupportService


class SupportDescribeServicesResponse(BaseModel):
    services: list[SupportService] | None = None
    ResponseMetadata: dict[str, Any] | None = None
