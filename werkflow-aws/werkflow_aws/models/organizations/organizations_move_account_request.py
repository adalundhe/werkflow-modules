from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsMoveAccountRequest(BaseModel):
    AccountId: StrictStr
    SourceParentId: StrictStr
    DestinationParentId: StrictStr
