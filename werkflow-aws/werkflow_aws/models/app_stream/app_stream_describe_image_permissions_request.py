from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeImagePermissionsRequest(BaseModel):
    Name: StrictStr
    MaxResults: StrictInt | None = None
    SharedAwsAccountIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
