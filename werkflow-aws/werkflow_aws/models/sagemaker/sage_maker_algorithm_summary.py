from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerAlgorithmSummary(BaseModel):
    AlgorithmName: StrictStr | None = None
    AlgorithmArn: StrictStr | None = None
    AlgorithmDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    AlgorithmStatus: StrictStr | None = None
