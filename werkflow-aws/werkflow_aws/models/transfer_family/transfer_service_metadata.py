from __future__ import annotations
from pydantic import BaseModel
from .transfer_user_details import TransferUserDetails


class TransferServiceMetadata(BaseModel):
    UserDetails: TransferUserDetails | None = None
