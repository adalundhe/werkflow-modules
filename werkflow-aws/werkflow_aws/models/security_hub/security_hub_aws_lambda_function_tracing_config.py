from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsLambdaFunctionTracingConfig(BaseModel):
    Mode: StrictStr | None = None
