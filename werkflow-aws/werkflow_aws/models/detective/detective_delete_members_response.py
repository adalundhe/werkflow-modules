from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_unprocessed_account import DetectiveUnprocessedAccount


class DetectiveDeleteMembersResponse(BaseModel):
    AccountIds: list[StrictStr] | None = None
    UnprocessedAccounts: list[DetectiveUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
