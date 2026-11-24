from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceDescribeOrganizationConformancePacksRequest(BaseModel):
    OrganizationConformancePackNames: list[StrictStr] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
