from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_action_source import SageMakerActionSource


class SageMakerActionSummary(BaseModel):
    ActionArn: StrictStr | None = None
    ActionName: StrictStr | None = None
    Source: SageMakerActionSource | None = None
    ActionType: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
