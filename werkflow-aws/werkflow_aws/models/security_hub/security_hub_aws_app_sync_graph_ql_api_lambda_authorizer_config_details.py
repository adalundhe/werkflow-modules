from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails(BaseModel):
    AuthorizerResultTtlInSeconds: StrictInt | None = None
    AuthorizerUri: StrictStr | None = None
    IdentityValidationExpression: StrictStr | None = None
