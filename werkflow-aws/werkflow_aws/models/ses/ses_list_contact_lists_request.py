from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESListContactListsRequest(BaseModel):
    PageSize: StrictInt | None = None
    NextToken: StrictStr | None = None
