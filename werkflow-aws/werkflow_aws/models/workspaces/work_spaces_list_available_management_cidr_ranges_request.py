from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesListAvailableManagementCidrRangesRequest(BaseModel):
    ManagementCidrRangeConstraint: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
