from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EKSDescribeClusterVersionsRequest(BaseModel):
    clusterType: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    defaultOnly: StrictBool | None = None
    includeAll: StrictBool | None = None
    clusterVersions: list[StrictStr] | None = None
    status: Literal['unsupported', 'standard-support', 'extended-support'] | None = None
    versionStatus: Literal['UNSUPPORTED', 'STANDARD_SUPPORT', 'EXTENDED_SUPPORT'] | None = None
