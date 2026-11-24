from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_secondary_status import SageMakerSecondaryStatus


class SageMakerSecondaryStatusTransition(BaseModel):
    Status: SageMakerSecondaryStatus | None = None
    StartTime: datetime.datetime | None = None
    EndTime: datetime.datetime | None = None
    StatusMessage: StrictStr | None = None
