from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_label_counters_for_workteam import SageMakerLabelCountersForWorkteam


class SageMakerLabelingJobForWorkteamSummary(BaseModel):
    LabelingJobName: StrictStr | None = None
    JobReferenceCode: StrictStr | None = None
    WorkRequesterAccountId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LabelCounters: SageMakerLabelCountersForWorkteam | None = None
    NumberOfHumanWorkersPerDataObject: StrictInt | None = None
