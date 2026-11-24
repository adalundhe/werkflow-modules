from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerHumanTaskUiSummary(BaseModel):
    HumanTaskUiName: StrictStr | None = None
    HumanTaskUiArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
