from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateTrialRequest(BaseModel):
    TrialName: StrictStr
    ExperimentName: StrictStr
    DisplayName: StrictStr | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    Tags: list[SageMakerTagModel] | None = None
