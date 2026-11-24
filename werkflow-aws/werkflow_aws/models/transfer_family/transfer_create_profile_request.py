from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferCreateProfileRequest(BaseModel):
    As2Id: StrictStr
    ProfileType: Literal['LOCAL', 'PARTNER']
    CertificateIds: list[StrictStr] | None = None
    Tags: list[TransferTag] | None = None
