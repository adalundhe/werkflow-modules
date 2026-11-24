from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_prefix_aware_routing_config import SageMakerPrefixAwareRoutingConfig
from .sage_maker_routing_strategy import SageMakerRoutingStrategy


class SageMakerProductionVariantRoutingConfig(BaseModel):
    RoutingStrategy: SageMakerRoutingStrategy | None = None
    PrefixAwareRoutingConfig: SageMakerPrefixAwareRoutingConfig | None = None
