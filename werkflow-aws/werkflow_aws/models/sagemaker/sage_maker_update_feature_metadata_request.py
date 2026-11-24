from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_feature_parameter import SageMakerFeatureParameter


class SageMakerUpdateFeatureMetadataRequest(BaseModel):
    FeatureGroupName: StrictStr
    FeatureName: StrictStr
    Description: StrictStr | None = None
    ParameterAdditions: list[SageMakerFeatureParameter] | None = None
    ParameterRemovals: list[StrictStr] | None = None
