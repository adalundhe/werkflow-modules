from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTListTagsForResourceResponse(BaseModel):
    tags: list[IoTTag] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
