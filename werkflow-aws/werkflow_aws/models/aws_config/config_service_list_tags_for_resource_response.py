from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_tag import ConfigServiceTag


class ConfigServiceListTagsForResourceResponse(BaseModel):
    Tags: list[ConfigServiceTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
