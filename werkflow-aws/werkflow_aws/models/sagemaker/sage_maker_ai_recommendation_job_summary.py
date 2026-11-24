from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerAIRecommendationJobSummary(BaseModel):
    AIRecommendationJobName: StrictStr | None = None
    AIRecommendationJobArn: StrictStr | None = None
    AIRecommendationJobStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
