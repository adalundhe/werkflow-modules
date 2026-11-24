from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_trial_component_artifact import SageMakerTrialComponentArtifact
from .sage_maker_trial_component_parameter_value import SageMakerTrialComponentParameterValue
from .sage_maker_trial_component_status import SageMakerTrialComponentStatus


class SageMakerCreateTrialComponentRequest(BaseModel):
    TrialComponentName: StrictStr
    DisplayName: StrictStr | None = None
    Status: SageMakerTrialComponentStatus | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Parameters: dict[StrictStr, SageMakerTrialComponentParameterValue] | None = None
    InputArtifacts: dict[StrictStr, SageMakerTrialComponentArtifact] | None = None
    OutputArtifacts: dict[StrictStr, SageMakerTrialComponentArtifact] | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    Tags: list[SageMakerTagModel] | None = None
