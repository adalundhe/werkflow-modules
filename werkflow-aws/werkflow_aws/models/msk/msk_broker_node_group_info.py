import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool,
)

from typing import Literal
from .msk_cluster_broker_az_distribution import MSKClusterBrokerAZDistribution
from .msk_ebs_storage_info import MSKEBSStorageInfo
from .msk_connectivity_info import MSKConnectivityInfo
from .msk_client_authentication import MSKClientAuthentication
from .msk_current_broker_software_info import MSKCurrentBrokerSoftwareInfo
from .msk_encryption_info import MSKEncryptionInfo
from .msk_enhanced_monitoring import MSKEnhancedMonitoring
from .msk_logging_info import MSKLoggingInfo
from .msk_open_monitoring import MSKOpenMonitoring
from .msk_node_group_state import MSKNodeGroupState
from .msk_state_info import MSKStateInfo
from .msk_storage_mode import MSKStorageMode
from .msk_customer_action_status import MSKCustomerActionStatus


class MSKBrokerNodeGroupInfo(BaseModel):
    BrokerAZDistribution: MSKClusterBrokerAZDistribution = 'DEFAULT'
    ClientSubnets: list[StrictStr]
    InstanceType: StrictStr
    SecurityGroups: list[StrictStr]
    StorageInfo: MSKEBSStorageInfo
    ConnectivityInfo: MSKConnectivityInfo
    ClientAuthentication: MSKClientAuthentication
    ClusterArn: StrictStr
    ClusterName: StrictStr
    CreationTime: datetime.datetime
    CurrentBrokerSoftwareInfo: MSKCurrentBrokerSoftwareInfo
    CurrentVersion: StrictStr
    EncryptionInfo: MSKEncryptionInfo
    EnhancedMonitoring: MSKEnhancedMonitoring
    OpenMonitoring: MSKOpenMonitoring
    LoggingInfo: MSKLoggingInfo
    NumberOfBrokerNodes: StrictInt
    State: MSKNodeGroupState
    StateInfo: MSKStateInfo
    Tags: dict[StrictStr, StrictStr] | None = None
    ZookeeperConnectString: StrictStr
    ZookeeperConnectStringTls: StrictStr
    StorageMode: MSKStorageMode
    CustomerActionStatus: MSKCustomerActionStatus

