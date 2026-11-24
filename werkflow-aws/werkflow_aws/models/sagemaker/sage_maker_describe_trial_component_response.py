from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_trial_component_artifact import SageMakerTrialComponentArtifact
from .sage_maker_trial_component_metric_summary import SageMakerTrialComponentMetricSummary
from .sage_maker_trial_component_parameter_value import SageMakerTrialComponentParameterValue
from .sage_maker_trial_component_source import SageMakerTrialComponentSource
from .sage_maker_trial_component_status import SageMakerTrialComponentStatus
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeTrialComponentResponse(BaseModel):
    TrialComponentName: StrictStr | None = None
    TrialComponentArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
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
    MetadataProperties: SageMakerMetadataProperties | None = None
    Metrics: list[SageMakerTrialComponentMetricSummary] | None = None
    LineageGroupArn: StrictStr | None = None
    Sources: list[SageMakerTrialComponentSource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
