from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerGlobalInferenceGatewaySummary(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
