from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class TransferListProfilesRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ProfileType: Literal['LOCAL', 'PARTNER'] | None = None
