from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OrganizationsListCreateAccountStatusRequest(BaseModel):
    States: list[Literal['IN_PROGRESS', 'SUCCEEDED', 'FAILED']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
