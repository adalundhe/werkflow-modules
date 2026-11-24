from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppRunnerListServicesForAutoScalingConfigurationRequest(BaseModel):
    AutoScalingConfigurationArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
