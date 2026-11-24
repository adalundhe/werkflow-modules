from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem


class ECSPutClusterCapacityProvidersRequest(BaseModel):
    cluster: StrictStr
    capacityProviders: list[StrictStr]
    defaultCapacityProviderStrategy: list[ECSCapacityProviderStrategyItem]
