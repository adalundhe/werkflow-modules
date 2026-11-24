from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OrganizationsListChildrenRequest(BaseModel):
    ParentId: StrictStr
    ChildType: Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
