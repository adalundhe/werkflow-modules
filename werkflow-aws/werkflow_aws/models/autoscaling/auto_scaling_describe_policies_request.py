from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AutoScalingDescribePoliciesRequest(BaseModel):
    AutoScalingGroupName: StrictStr | None = None
    PolicyNames: list[StrictStr] | None = None
    PolicyTypes: list[StrictStr] | None = None
    IncludeManagedResources: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
