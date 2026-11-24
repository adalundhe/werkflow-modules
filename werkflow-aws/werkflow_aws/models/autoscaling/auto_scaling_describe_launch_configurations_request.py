from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingDescribeLaunchConfigurationsRequest(BaseModel):
    LaunchConfigurationNames: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
