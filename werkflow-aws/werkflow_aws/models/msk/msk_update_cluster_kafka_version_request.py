from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_configuration_info_model import MSKConfigurationInfoModel


class MSKUpdateClusterKafkaVersionRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    TargetKafkaVersion: StrictStr
    ConfigurationInfo: MSKConfigurationInfoModel | None = None
