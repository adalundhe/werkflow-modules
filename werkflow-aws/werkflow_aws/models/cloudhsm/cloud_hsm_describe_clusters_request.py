from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudHSMDescribeClustersRequest(BaseModel):
    Filters: dict[StrictStr, list[StrictStr]] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
