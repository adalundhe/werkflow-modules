from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_broker_ebs_volume_info import MSKBrokerEBSVolumeInfo


class MSKUpdateBrokerStorageRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    TargetBrokerEBSVolumeInfo: list[MSKBrokerEBSVolumeInfo]
