from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_iam_access_key_session_context import SecurityHubAwsIamAccessKeySessionContext


class SecurityHubAwsIamAccessKeyDetails(BaseModel):
    UserName: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedAt: StrictStr | None = None
    PrincipalId: StrictStr | None = None
    PrincipalType: StrictStr | None = None
    PrincipalName: StrictStr | None = None
    AccountId: StrictStr | None = None
    AccessKeyId: StrictStr | None = None
    SessionContext: SecurityHubAwsIamAccessKeySessionContext | None = None
