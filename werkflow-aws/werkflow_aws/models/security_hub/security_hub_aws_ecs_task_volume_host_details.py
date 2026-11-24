from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskVolumeHostDetails(BaseModel):
    SourcePath: StrictStr | None = None
