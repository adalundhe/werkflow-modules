from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerModelSummary(BaseModel):
    ModelName: StrictStr | None = None
    ModelArn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
