from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails(BaseModel):
    Namespace: StrictStr | None = None
    Value: StrictStr | None = None
