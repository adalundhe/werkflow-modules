from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeRegionsRequest(BaseModel):
    DirectoryId: StrictStr
    RegionName: StrictStr | None = None
    NextToken: StrictStr | None = None
