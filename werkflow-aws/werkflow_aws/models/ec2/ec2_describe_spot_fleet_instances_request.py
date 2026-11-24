from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeSpotFleetInstancesRequest(BaseModel):
    SpotFleetRequestId: StrictStr
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
