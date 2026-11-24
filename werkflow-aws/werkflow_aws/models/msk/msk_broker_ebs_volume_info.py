from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_provisioned_throughput import MSKProvisionedThroughput


class MSKBrokerEBSVolumeInfo(BaseModel):
    KafkaBrokerNodeId: StrictStr | None = None
    ProvisionedThroughput: MSKProvisionedThroughput | None = None
    VolumeSizeGB: StrictInt | None = None
