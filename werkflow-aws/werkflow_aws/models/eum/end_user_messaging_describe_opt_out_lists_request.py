from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingDescribeOptOutListsRequest(BaseModel):
    OptOutListNames: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Owner: Literal['SELF', 'SHARED'] | None = None
