from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_broker_node_group_info import MSKBrokerNodeGroupInfo
from .msk_client_authentication import MSKClientAuthentication
from .msk_configuration_info import MSKConfigurationInfo
from .msk_encryption_info import MSKEncryptionInfo
from .msk_enhanced_monitoring import MSKEnhancedMonitoring
from .msk_logging_info import MSKLoggingInfo
from .msk_open_monitoring import MSKOpenMonitoring
from .msk_storage_mode import MSKStorageMode


class MSKCreateClusterRequest(BaseModel):
    BrokerNodeGroupInfo: MSKBrokerNodeGroupInfo | None = None
    ClusterName: StrictStr | None = None
    KafkaVersion: StrictStr | None = None
    NumberOfBrokerNodes: StrictInt | None = None
    ClientAuthentication: MSKClientAuthentication | None = None
    ConfigurationInfo: MSKConfigurationInfo | None = None
    EncryptionInfo: MSKEncryptionInfo | None = None
    EnhancedMonitoring: MSKEnhancedMonitoring | None = None
    OpenMonitoring: MSKOpenMonitoring | None = None
    LoggingInfo: MSKLoggingInfo | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    StorageMode: MSKStorageMode | None = None
