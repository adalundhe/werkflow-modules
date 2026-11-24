from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_profile import TransferListedProfile


class TransferListProfilesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Profiles: list[TransferListedProfile] | None = None
    ResponseMetadata: dict[str, Any] | None = None
