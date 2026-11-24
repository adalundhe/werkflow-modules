from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_tag import KinesisTag


class KinesisListTagsForResourceResponse(BaseModel):
    Tags: list[KinesisTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
