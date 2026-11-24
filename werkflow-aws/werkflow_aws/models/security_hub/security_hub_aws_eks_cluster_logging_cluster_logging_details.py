from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEksClusterLoggingClusterLoggingDetails(BaseModel):
    Enabled: StrictBool | None = None
    Types: list[StrictStr] | None = None
