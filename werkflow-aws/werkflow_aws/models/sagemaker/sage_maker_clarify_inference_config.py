from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_clarify_feature_type import SageMakerClarifyFeatureType


class SageMakerClarifyInferenceConfig(BaseModel):
    FeaturesAttribute: StrictStr | None = None
    ContentTemplate: StrictStr | None = None
    MaxRecordCount: StrictInt | None = None
    MaxPayloadInMB: StrictInt | None = None
    ProbabilityIndex: StrictInt | None = None
    LabelIndex: StrictInt | None = None
    ProbabilityAttribute: StrictStr | None = None
    LabelAttribute: StrictStr | None = None
    LabelHeaders: list[StrictStr] | None = None
    FeatureHeaders: list[StrictStr] | None = None
    FeatureTypes: list[SageMakerClarifyFeatureType] | None = None
