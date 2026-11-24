from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesListAccountLinksRequest(BaseModel):
    LinkStatusFilter: list[Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
