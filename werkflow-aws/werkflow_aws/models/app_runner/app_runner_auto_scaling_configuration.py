from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AppRunnerAutoScalingConfiguration(BaseModel):
    AutoScalingConfigurationArn: StrictStr | None = None
    AutoScalingConfigurationName: StrictStr | None = None
    AutoScalingConfigurationRevision: StrictInt | None = None
    Latest: StrictBool | None = None
    Status: StrictStr | None = None
    MaxConcurrency: StrictInt | None = None
    MinSize: StrictInt | None = None
    MaxSize: StrictInt | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    DeletedAt: datetime.datetime | StrictStr | None = None
    HasAssociatedService: StrictBool | None = None
    IsDefault: StrictBool | None = None
