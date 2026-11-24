from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_tag import SSMTag


class SSMListTagsForResourceResponse(BaseModel):
    TagList: list[SSMTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
