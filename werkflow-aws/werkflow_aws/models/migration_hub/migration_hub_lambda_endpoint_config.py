from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubLambdaEndpointConfig(BaseModel):
    Arn: StrictStr | None = None
