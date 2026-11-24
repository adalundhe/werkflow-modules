from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerAIBenchmarkJobSummary(BaseModel):
    AIBenchmarkJobName: StrictStr | None = None
    AIBenchmarkJobArn: StrictStr | None = None
    AIBenchmarkJobStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    AIWorkloadConfigName: StrictStr | None = None
