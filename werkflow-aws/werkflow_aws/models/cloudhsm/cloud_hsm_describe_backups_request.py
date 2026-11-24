from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudHSMDescribeBackupsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: dict[StrictStr, list[StrictStr]] | None = None
    Shared: StrictBool | None = None
    SortAscending: StrictBool | None = None
