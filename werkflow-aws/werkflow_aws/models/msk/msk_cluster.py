import datetime
from pydantic import BaseModel, StrictInt, StrictStr

from .msk_broker_node_group_info import MSKBrokerNodeGroupInfo
from .msk_client_authentication import MSKClientAuthentication
from .msk_current_broker_software_info import MSKCurrentBrokerSoftwareInfo
from .msk_customer_action_status import MSKCustomerActionStatus
from .msk_encryption_info import MSKEncryptionInfo
from .msk_enhanced_monitoring import MSKEnhancedMonitoring
from .msk_logging_info import MSKLoggingInfo
from .msk_node_group_state import MSKNodeGroupState
from .msk_open_monitoring import MSKOpenMonitoring
from .msk_state_info import MSKStateInfo
from .msk_storage_mode import MSKStorageMode


class MSKCluster(BaseModel):
    ActiveOperationArn: StrictStr | None = None
    BrokerNodeGroupInfo: MSKBrokerNodeGroupInfo | None = None
    ClientAuthentication: MSKClientAuthentication | None = None
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    CurrentBrokerSoftwareInfo: MSKCurrentBrokerSoftwareInfo | None = None
    CurrentVersion: StrictStr | None = None
    EncryptionInfo: MSKEncryptionInfo | None = None
    EnhancedMonitoring: MSKEnhancedMonitoring | None = None
    OpenMonitoring: MSKOpenMonitoring | None = None
    LoggingInfo: MSKLoggingInfo | None = None
    NumberOfBrokerNodes: StrictInt | None = None
    State: MSKNodeGroupState | None = None
    StateInfo: MSKStateInfo | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ZookeeperConnectString: StrictStr | None = None
    ZookeeperConnectStringTls: StrictStr | None = None
    StorageMode: MSKStorageMode | None = None
    CustomerActionStatus: MSKCustomerActionStatus | None = None
