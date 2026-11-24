from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeDeclarativePoliciesReportsRequest(BaseModel):
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ReportIds: list[StrictStr] | None = None
