from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingDescribeAccountSettingsRequest(BaseModel):
    Name: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
