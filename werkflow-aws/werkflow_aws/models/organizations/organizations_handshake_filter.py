from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OrganizationsHandshakeFilter(BaseModel):
    ActionType: Literal['INVITE', 'ENABLE_ALL_FEATURES', 'APPROVE_ALL_FEATURES', 'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE', 'TRANSFER_RESPONSIBILITY'] | None = None
    ParentHandshakeId: StrictStr | None = None
