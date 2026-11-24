from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_standards_managed_by import SecurityHubStandardsManagedBy


class SecurityHubStandard(BaseModel):
    StandardsArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    EnabledByDefault: StrictBool | None = None
    Provider: StrictStr | None = None
    StandardsManagedBy: SecurityHubStandardsManagedBy | None = None
