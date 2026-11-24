from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferTagResourceRequest(BaseModel):
    Arn: StrictStr
    Tags: list[TransferTag]
