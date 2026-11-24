from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionVolumesHostDetails(BaseModel):
    SourcePath: StrictStr | None = None
