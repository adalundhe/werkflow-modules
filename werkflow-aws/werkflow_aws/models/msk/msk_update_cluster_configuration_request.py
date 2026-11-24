from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_configuration_info_model import MSKConfigurationInfoModel


class MSKUpdateClusterConfigurationRequest(BaseModel):
    ClusterArn: StrictStr
    ConfigurationInfo: MSKConfigurationInfoModel
    CurrentVersion: StrictStr
