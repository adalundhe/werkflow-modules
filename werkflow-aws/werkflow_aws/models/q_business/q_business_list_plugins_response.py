from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_plugin import QBusinessPlugin


class QBusinessListPluginsResponse(BaseModel):
    nextToken: StrictStr | None = None
    plugins: list[QBusinessPlugin] | None = None
    ResponseMetadata: dict[str, Any] | None = None
