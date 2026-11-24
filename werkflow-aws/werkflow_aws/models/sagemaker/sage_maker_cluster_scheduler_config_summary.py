from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerClusterSchedulerConfigSummary(BaseModel):
    ClusterSchedulerConfigArn: StrictStr | None = None
    ClusterSchedulerConfigId: StrictStr | None = None
    ClusterSchedulerConfigVersion: StrictInt | None = None
    Name: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ClusterArn: StrictStr | None = None
