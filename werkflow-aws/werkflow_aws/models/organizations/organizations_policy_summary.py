from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OrganizationsPolicySummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    AwsManaged: StrictBool | None = None
