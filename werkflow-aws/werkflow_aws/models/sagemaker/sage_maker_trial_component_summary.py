from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_trial_component_source import SageMakerTrialComponentSource
from .sage_maker_trial_component_status import SageMakerTrialComponentStatus
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerTrialComponentSummary(BaseModel):
    TrialComponentName: StrictStr | None = None
    TrialComponentArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
    TrialComponentSource: SageMakerTrialComponentSource | None = None
    Status: SageMakerTrialComponentStatus | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
