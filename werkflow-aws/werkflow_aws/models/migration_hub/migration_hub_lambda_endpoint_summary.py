from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubLambdaEndpointSummary(BaseModel):
    Arn: StrictStr | None = None
