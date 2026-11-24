from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_trial_source import SageMakerTrialSource


class SageMakerTrialSummary(BaseModel):
    TrialArn: StrictStr | None = None
    TrialName: StrictStr | None = None
    DisplayName: StrictStr | None = None
    TrialSource: SageMakerTrialSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
