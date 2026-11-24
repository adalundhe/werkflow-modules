from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_trial_component_simple_summary import SageMakerTrialComponentSimpleSummary
from .sage_maker_trial_source import SageMakerTrialSource
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerTrial(BaseModel):
    TrialName: StrictStr | None = None
    TrialArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
    ExperimentName: StrictStr | None = None
    Source: SageMakerTrialSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    Tags: list[SageMakerTagModel] | None = None
    TrialComponentSummaries: list[SageMakerTrialComponentSimpleSummary] | None = None
