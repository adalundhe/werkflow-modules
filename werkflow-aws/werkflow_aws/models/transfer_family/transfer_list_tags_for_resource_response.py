from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferListTagsForResourceResponse(BaseModel):
    Arn: StrictStr | None = None
    NextToken: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
