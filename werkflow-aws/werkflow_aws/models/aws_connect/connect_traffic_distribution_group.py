from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectTrafficDistributionGroup(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    InstanceArn: StrictStr | None = None
    Status: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    IsDefault: StrictBool | None = None
