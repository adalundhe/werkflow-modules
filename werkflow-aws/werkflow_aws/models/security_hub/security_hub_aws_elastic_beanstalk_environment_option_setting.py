from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElasticBeanstalkEnvironmentOptionSetting(BaseModel):
    Namespace: StrictStr | None = None
    OptionName: StrictStr | None = None
    ResourceName: StrictStr | None = None
    Value: StrictStr | None = None
