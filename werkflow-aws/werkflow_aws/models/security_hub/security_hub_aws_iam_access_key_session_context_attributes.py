from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsIamAccessKeySessionContextAttributes(BaseModel):
    MfaAuthenticated: StrictBool | None = None
    CreationDate: StrictStr | None = None
