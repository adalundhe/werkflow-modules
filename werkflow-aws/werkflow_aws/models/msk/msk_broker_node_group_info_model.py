from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_connectivity_info_model import MSKConnectivityInfoModel
from .msk_storage_info import MSKStorageInfo


class MSKBrokerNodeGroupInfoModel(BaseModel):
    BrokerAZDistribution: StrictStr | None = None
    ClientSubnets: list[StrictStr] | None = None
    InstanceType: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    StorageInfo: MSKStorageInfo | None = None
    ConnectivityInfo: MSKConnectivityInfoModel | None = None
    ZoneIds: list[StrictStr] | None = None
