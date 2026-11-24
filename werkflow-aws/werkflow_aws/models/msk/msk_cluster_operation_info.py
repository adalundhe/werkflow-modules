from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .msk_broker_type_upgrade_info import MSKBrokerTypeUpgradeInfo
from .msk_cluster_operation_step import MSKClusterOperationStep
from .msk_error_info import MSKErrorInfo
from .msk_mutable_cluster_info import MSKMutableClusterInfo
from .msk_vpc_connection_info import MSKVpcConnectionInfo


class MSKClusterOperationInfo(BaseModel):
    BrokerTypeUpgradeInfo: MSKBrokerTypeUpgradeInfo | None = None
    ClientRequestId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ErrorInfo: MSKErrorInfo | None = None
    OperationArn: StrictStr | None = None
    OperationState: StrictStr | None = None
    OperationSteps: list[MSKClusterOperationStep] | None = None
    OperationType: StrictStr | None = None
    SourceClusterInfo: MSKMutableClusterInfo | None = None
    TargetClusterInfo: MSKMutableClusterInfo | None = None
    VpcConnectionInfo: MSKVpcConnectionInfo | None = None
