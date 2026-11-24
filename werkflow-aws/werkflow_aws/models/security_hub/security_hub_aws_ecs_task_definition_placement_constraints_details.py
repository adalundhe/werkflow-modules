from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionPlacementConstraintsDetails(BaseModel):
    Expression: StrictStr | None = None
    Type: StrictStr | None = None
