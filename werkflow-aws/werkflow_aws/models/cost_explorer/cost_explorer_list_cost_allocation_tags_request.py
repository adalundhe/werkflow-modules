from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerListCostAllocationTagsRequest(BaseModel):
    Status: Literal['Active', 'Inactive'] | None = None
    TagKeys: list[StrictStr] | None = None
    Type: Literal['AWSGenerated', 'UserDefined'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
