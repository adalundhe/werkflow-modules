from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .firehose_tag import FirehoseTag


class FirehoseListTagsForDeliveryStreamResponse(BaseModel):
    Tags: list[FirehoseTag] | None = None
    HasMoreTags: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
