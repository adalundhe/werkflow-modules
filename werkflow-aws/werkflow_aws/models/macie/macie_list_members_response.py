from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_member import MacieMember


class MacieListMembersResponse(BaseModel):
    members: list[MacieMember] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
