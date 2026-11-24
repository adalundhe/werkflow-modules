from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeTrainingPlanExtensionHistoryRequest(BaseModel):
    TrainingPlanArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
