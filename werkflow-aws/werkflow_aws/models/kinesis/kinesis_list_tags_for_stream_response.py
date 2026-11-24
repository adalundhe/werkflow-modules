from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .kinesis_tag import KinesisTag


class KinesisListTagsForStreamResponse(BaseModel):
    Tags: list[KinesisTag] | None = None
    HasMoreTags: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
