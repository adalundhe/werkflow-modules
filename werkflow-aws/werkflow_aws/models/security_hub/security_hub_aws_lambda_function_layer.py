from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsLambdaFunctionLayer(BaseModel):
    Arn: StrictStr | None = None
    CodeSize: StrictInt | None = None
