from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerTrainingSessionSummary(BaseModel):
    TrainingSessionArn: StrictStr | None = None
    TrainingSessionStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
