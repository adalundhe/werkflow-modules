from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_trial_component_source import SageMakerTrialComponentSource
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerTrialComponentSimpleSummary(BaseModel):
    TrialComponentName: StrictStr | None = None
    TrialComponentArn: StrictStr | None = None
    TrialComponentSource: SageMakerTrialComponentSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
