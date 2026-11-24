from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerClusterSummary(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ClusterStatus: StrictStr | None = None
    TrainingPlanArns: list[StrictStr] | None = None
    ImageVersionStatus: StrictStr | None = None
