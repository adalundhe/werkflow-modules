from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_cluster_configuration import ECSClusterConfiguration
from .ecs_cluster_service_connect_defaults_request import ECSClusterServiceConnectDefaultsRequest
from .ecs_cluster_setting import ECSClusterSetting


class ECSUpdateClusterRequest(BaseModel):
    cluster: StrictStr
    settings: list[ECSClusterSetting] | None = None
    configuration: ECSClusterConfiguration | None = None
    serviceConnectDefaults: ECSClusterServiceConnectDefaultsRequest | None = None
