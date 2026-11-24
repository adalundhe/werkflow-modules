from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubLambdaEndpointInput(BaseModel):
    Arn: StrictStr | None = None
