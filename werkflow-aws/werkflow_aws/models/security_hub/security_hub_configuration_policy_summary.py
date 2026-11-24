from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubConfigurationPolicySummary(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ServiceEnabled: StrictBool | None = None
