from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCloudFormationStackDriftInformationDetails(BaseModel):
    StackDriftStatus: StrictStr | None = None
