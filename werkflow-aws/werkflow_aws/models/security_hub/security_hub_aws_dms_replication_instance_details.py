from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_dms_replication_instance_replication_subnet_group_details import SecurityHubAwsDmsReplicationInstanceReplicationSubnetGroupDetails
from .security_hub_aws_dms_replication_instance_vpc_security_groups_details import SecurityHubAwsDmsReplicationInstanceVpcSecurityGroupsDetails


class SecurityHubAwsDmsReplicationInstanceDetails(BaseModel):
    AllocatedStorage: StrictInt | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    AvailabilityZone: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    ReplicationInstanceClass: StrictStr | None = None
    ReplicationInstanceIdentifier: StrictStr | None = None
    ReplicationSubnetGroup: SecurityHubAwsDmsReplicationInstanceReplicationSubnetGroupDetails | None = None
    VpcSecurityGroups: list[SecurityHubAwsDmsReplicationInstanceVpcSecurityGroupsDetails] | None = None
