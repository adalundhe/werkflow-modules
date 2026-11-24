from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_policy import SecurityHubPolicy


class SecurityHubUpdateConfigurationPolicyResponse(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ConfigurationPolicy: SecurityHubPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
