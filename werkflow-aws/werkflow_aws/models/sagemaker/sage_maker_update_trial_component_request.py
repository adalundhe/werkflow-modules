from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_trial_component_artifact import SageMakerTrialComponentArtifact
from .sage_maker_trial_component_parameter_value import SageMakerTrialComponentParameterValue
from .sage_maker_trial_component_status import SageMakerTrialComponentStatus


class SageMakerUpdateTrialComponentRequest(BaseModel):
    TrialComponentName: StrictStr
    DisplayName: StrictStr | None = None
    Status: SageMakerTrialComponentStatus | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Parameters: dict[StrictStr, SageMakerTrialComponentParameterValue] | None = None
    ParametersToRemove: list[StrictStr] | None = None
    InputArtifacts: dict[StrictStr, SageMakerTrialComponentArtifact] | None = None
    InputArtifactsToRemove: list[StrictStr] | None = None
    OutputArtifacts: dict[StrictStr, SageMakerTrialComponentArtifact] | None = None
    OutputArtifactsToRemove: list[StrictStr] | None = None
