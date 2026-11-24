from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCloudFormationStackOutputsDetails(BaseModel):
    Description: StrictStr | None = None
    OutputKey: StrictStr | None = None
    OutputValue: StrictStr | None = None
