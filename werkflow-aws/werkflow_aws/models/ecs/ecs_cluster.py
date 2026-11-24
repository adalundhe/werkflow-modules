from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_attachment import ECSAttachment
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_cluster_configuration import ECSClusterConfiguration
from .ecs_cluster_service_connect_defaults import ECSClusterServiceConnectDefaults
from .ecs_cluster_setting import ECSClusterSetting
from .ecs_key_value_pair import ECSKeyValuePair
from .ecs_tag import ECSTag


class ECSCluster(BaseModel):
    clusterArn: StrictStr | None = None
    clusterName: StrictStr | None = None
    configuration: ECSClusterConfiguration | None = None
    status: StrictStr | None = None
    registeredContainerInstancesCount: StrictInt | None = None
    runningTasksCount: StrictInt | None = None
    pendingTasksCount: StrictInt | None = None
    activeServicesCount: StrictInt | None = None
    statistics: list[ECSKeyValuePair] | None = None
    tags: list[ECSTag] | None = None
    settings: list[ECSClusterSetting] | None = None
    capacityProviders: list[StrictStr] | None = None
    defaultCapacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    attachments: list[ECSAttachment] | None = None
    attachmentsStatus: StrictStr | None = None
    serviceConnectDefaults: ECSClusterServiceConnectDefaults | None = None
