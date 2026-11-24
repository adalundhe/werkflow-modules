from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_collection_config import SageMakerCollectionConfig


class SageMakerFeatureDefinition(BaseModel):
    FeatureName: StrictStr | None = None
    FeatureType: StrictStr | None = None
    CollectionType: StrictStr | None = None
    CollectionConfig: SageMakerCollectionConfig | None = None
