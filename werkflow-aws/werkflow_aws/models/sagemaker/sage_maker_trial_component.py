from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_parent import SageMakerParent
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_trial_component_artifact import SageMakerTrialComponentArtifact
from .sage_maker_trial_component_metric_summary import SageMakerTrialComponentMetricSummary
from .sage_maker_trial_component_parameter_value import SageMakerTrialComponentParameterValue
from .sage_maker_trial_component_source import SageMakerTrialComponentSource
from .sage_maker_trial_component_source_detail import SageMakerTrialComponentSourceDetail
from .sage_maker_trial_component_status import SageMakerTrialComponentStatus
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerTrialComponent(BaseModel):
    TrialComponentName: StrictStr | None = None
    DisplayName: StrictStr | None = None
    TrialComponentArn: StrictStr | None = None
    Source: SageMakerTrialComponentSource | None = None
    Status: SageMakerTrialComponentStatus | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    Parameters: dict[StrictStr, SageMakerTrialComponentParameterValue] | None = None
    InputArtifacts: dict[StrictStr, SageMakerTrialComponentArtifact] | None = None
    OutputArtifacts: dict[StrictStr, SageMakerTrialComponentArtifact] | None = None
    Metrics: list[SageMakerTrialComponentMetricSummary] | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    SourceDetail: SageMakerTrialComponentSourceDetail | None = None
    LineageGroupArn: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    Parents: list[SageMakerParent] | None = None
    RunName: StrictStr | None = None
