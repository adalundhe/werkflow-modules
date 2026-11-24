from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DevOpsGuruDescribeOrganizationResourceCollectionHealthRequest(BaseModel):
    OrganizationResourceCollectionType: Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_ACCOUNT', 'AWS_TAGS']
    AccountIds: list[StrictStr] | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
