from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsLambdaFunctionDeadLetterConfig(BaseModel):
    TargetArn: StrictStr | None = None
