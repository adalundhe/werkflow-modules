from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class FirehoseListDeliveryStreamsResponse(BaseModel):
    DeliveryStreamNames: list[StrictStr] | None = None
    HasMoreDeliveryStreams: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
