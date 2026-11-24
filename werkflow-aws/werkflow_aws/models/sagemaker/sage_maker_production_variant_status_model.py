from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerProductionVariantStatusModel(BaseModel):
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
