from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AppRunnerAutoScalingConfigurationSummary(BaseModel):
    AutoScalingConfigurationArn: StrictStr | None = None
    AutoScalingConfigurationName: StrictStr | None = None
    AutoScalingConfigurationRevision: StrictInt | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    HasAssociatedService: StrictBool | None = None
    IsDefault: StrictBool | None = None
