from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerLabelingJobSnsDataSource(BaseModel):
    SnsTopicArn: StrictStr | None = None
