from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_cluster_setting import ECSClusterSetting


class ECSUpdateClusterSettingsRequest(BaseModel):
    cluster: StrictStr
    settings: list[ECSClusterSetting]
