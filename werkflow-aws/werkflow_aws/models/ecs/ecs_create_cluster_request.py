from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_cluster_configuration import ECSClusterConfiguration
from .ecs_cluster_service_connect_defaults_request import ECSClusterServiceConnectDefaultsRequest
from .ecs_cluster_setting import ECSClusterSetting
from .ecs_tag import ECSTag


class ECSCreateClusterRequest(BaseModel):
    clusterName: StrictStr | None = None
    tags: list[ECSTag] | None = None
    settings: list[ECSClusterSetting] | None = None
    configuration: ECSClusterConfiguration | None = None
    capacityProviders: list[StrictStr] | None = None
    defaultCapacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    serviceConnectDefaults: ECSClusterServiceConnectDefaultsRequest | None = None
