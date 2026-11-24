from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerPartnerAppSummary(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
