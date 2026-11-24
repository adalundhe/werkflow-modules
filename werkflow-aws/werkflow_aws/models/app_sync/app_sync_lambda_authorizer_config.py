from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncLambdaAuthorizerConfig(BaseModel):
    authorizerResultTtlInSeconds: StrictInt | None = None
    authorizerUri: StrictStr | None = None
    identityValidationExpression: StrictStr | None = None
