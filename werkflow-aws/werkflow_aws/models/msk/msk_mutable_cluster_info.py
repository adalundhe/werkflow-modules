from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_broker_count_update_info import MSKBrokerCountUpdateInfo
from .msk_broker_ebs_volume_info import MSKBrokerEBSVolumeInfo
from .msk_client_authentication_model import MSKClientAuthenticationModel
from .msk_configuration_info_model import MSKConfigurationInfoModel
from .msk_connectivity_info_model import MSKConnectivityInfoModel
from .msk_encryption_info_model import MSKEncryptionInfoModel
from .msk_logging_info_model import MSKLoggingInfoModel
from .msk_open_monitoring_model import MSKOpenMonitoringModel
from .msk_rebalancing import MSKRebalancing
from .msk_zookeeper_access import MSKZookeeperAccess


class MSKMutableClusterInfo(BaseModel):
    BrokerEBSVolumeInfo: list[MSKBrokerEBSVolumeInfo] | None = None
    ConfigurationInfo: MSKConfigurationInfoModel | None = None
    NumberOfBrokerNodes: StrictInt | None = None
    EnhancedMonitoring: StrictStr | None = None
    OpenMonitoring: MSKOpenMonitoringModel | None = None
    ZookeeperAccess: MSKZookeeperAccess | None = None
    KafkaVersion: StrictStr | None = None
    LoggingInfo: MSKLoggingInfoModel | None = None
    InstanceType: StrictStr | None = None
    ClientAuthentication: MSKClientAuthenticationModel | None = None
    EncryptionInfo: MSKEncryptionInfoModel | None = None
    ConnectivityInfo: MSKConnectivityInfoModel | None = None
    StorageMode: StrictStr | None = None
    BrokerCountUpdateInfo: MSKBrokerCountUpdateInfo | None = None
    Rebalancing: MSKRebalancing | None = None
