from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElasticBeanstalkEnvironmentEnvironmentLink(BaseModel):
    EnvironmentName: StrictStr | None = None
    LinkName: StrictStr | None = None
