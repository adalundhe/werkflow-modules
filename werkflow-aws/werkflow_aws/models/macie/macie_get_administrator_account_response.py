from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_invitation import MacieInvitation


class MacieGetAdministratorAccountResponse(BaseModel):
    administrator: MacieInvitation | None = None
    ResponseMetadata: dict[str, Any] | None = None
