from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerAIWorkloadConfigSummary(BaseModel):
    AIWorkloadConfigName: StrictStr | None = None
    AIWorkloadConfigArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
