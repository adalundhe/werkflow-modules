from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_prefix_aware_routing_config_model import SageMakerPrefixAwareRoutingConfigModel


class SageMakerProductionVariantRoutingConfigModel(BaseModel):
    RoutingStrategy: StrictStr | None = None
    PrefixAwareRoutingConfig: SageMakerPrefixAwareRoutingConfigModel | None = None
