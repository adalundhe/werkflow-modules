from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerEdgeModel(BaseModel):
    ModelName: StrictStr | None = None
    ModelVersion: StrictStr | None = None
    LatestSampleTime: datetime.datetime | StrictStr | None = None
    LatestInference: datetime.datetime | StrictStr | None = None
