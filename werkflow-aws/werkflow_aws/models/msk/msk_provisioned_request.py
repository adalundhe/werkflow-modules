from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_broker_node_group_info_model import MSKBrokerNodeGroupInfoModel
from .msk_client_authentication_model import MSKClientAuthenticationModel
from .msk_configuration_info_model import MSKConfigurationInfoModel
from .msk_encryption_info_model import MSKEncryptionInfoModel
from .msk_logging_info_model import MSKLoggingInfoModel
from .msk_open_monitoring_info import MSKOpenMonitoringInfo
from .msk_rebalancing import MSKRebalancing


class MSKProvisionedRequest(BaseModel):
    BrokerNodeGroupInfo: MSKBrokerNodeGroupInfoModel
    KafkaVersion: StrictStr
    NumberOfBrokerNodes: StrictInt
    Rebalancing: MSKRebalancing | None = None
    ClientAuthentication: MSKClientAuthenticationModel | None = None
    ConfigurationInfo: MSKConfigurationInfoModel | None = None
    EncryptionInfo: MSKEncryptionInfoModel | None = None
    EnhancedMonitoring: Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION'] | None = None
    OpenMonitoring: MSKOpenMonitoringInfo | None = None
    LoggingInfo: MSKLoggingInfoModel | None = None
    StorageMode: Literal['LOCAL', 'TIERED'] | None = None
