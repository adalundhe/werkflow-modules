from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeSpotFleetRequestsRequest(BaseModel):
    DryRun: StrictBool | None = None
    SpotFleetRequestIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
