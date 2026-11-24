from __future__ import annotations
from pydantic import BaseModel
from .msk_broker_type_upgrade_info import MSKBrokerTypeUpgradeInfo
from .msk_cluster_operation_step import MSKClusterOperationStep
from .msk_mutable_cluster_info import MSKMutableClusterInfo
from .msk_vpc_connection_info import MSKVpcConnectionInfo


class MSKClusterOperationV2Provisioned(BaseModel):
    BrokerTypeUpgradeInfo: MSKBrokerTypeUpgradeInfo | None = None
    OperationSteps: list[MSKClusterOperationStep] | None = None
    SourceClusterInfo: MSKMutableClusterInfo | None = None
    TargetClusterInfo: MSKMutableClusterInfo | None = None
    VpcConnectionInfo: MSKVpcConnectionInfo | None = None
