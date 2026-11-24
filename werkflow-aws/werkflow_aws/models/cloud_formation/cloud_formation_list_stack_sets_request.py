from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListStackSetsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Status: Literal['ACTIVE', 'DELETED'] | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
