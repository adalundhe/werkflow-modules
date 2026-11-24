from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_user import TransferListedUser


class TransferListUsersResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServerId: StrictStr | None = None
    Users: list[TransferListedUser] | None = None
    ResponseMetadata: dict[str, Any] | None = None
