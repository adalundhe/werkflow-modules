from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubRemediationParameter(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    Required: StrictBool | None = None
