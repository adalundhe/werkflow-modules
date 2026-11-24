from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElasticBeanstalkEnvironmentTier(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Version: StrictStr | None = None
