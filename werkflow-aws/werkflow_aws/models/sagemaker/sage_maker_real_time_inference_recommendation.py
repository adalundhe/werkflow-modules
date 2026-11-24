from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_production_variant_instance_type import SageMakerProductionVariantInstanceType


class SageMakerRealTimeInferenceRecommendation(BaseModel):
    RecommendationId: StrictStr | None = None
    InstanceType: SageMakerProductionVariantInstanceType | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
