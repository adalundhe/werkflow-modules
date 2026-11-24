from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionDescribeProjectVersionsRequest(BaseModel):
    ProjectArn: StrictStr
    VersionNames: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
