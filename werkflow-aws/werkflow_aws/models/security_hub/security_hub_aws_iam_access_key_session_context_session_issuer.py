from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamAccessKeySessionContextSessionIssuer(BaseModel):
    Type: StrictStr | None = None
    PrincipalId: StrictStr | None = None
    Arn: StrictStr | None = None
    AccountId: StrictStr | None = None
    UserName: StrictStr | None = None
