from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails(BaseModel):
    Command: list[StrictStr] | None = None
    Interval: StrictInt | None = None
    Retries: StrictInt | None = None
    StartPeriod: StrictInt | None = None
    Timeout: StrictInt | None = None
