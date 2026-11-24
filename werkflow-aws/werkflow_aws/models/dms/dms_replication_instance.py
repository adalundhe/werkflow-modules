from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_kerberos_authentication_settings import DMSKerberosAuthenticationSettings
from .dms_replication_pending_modified_values import DMSReplicationPendingModifiedValues
from .dms_replication_subnet_group import DMSReplicationSubnetGroup
from .dms_vpc_security_group_membership import DMSVpcSecurityGroupMembership


class DMSReplicationInstance(BaseModel):
    ReplicationInstanceIdentifier: StrictStr | None = None
    ReplicationInstanceClass: StrictStr | None = None
    ReplicationInstanceStatus: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    InstanceCreateTime: datetime.datetime | StrictStr | None = None
    VpcSecurityGroups: list[DMSVpcSecurityGroupMembership] | None = None
    AvailabilityZone: StrictStr | None = None
    ReplicationSubnetGroup: DMSReplicationSubnetGroup | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PendingModifiedValues: DMSReplicationPendingModifiedValues | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    ReplicationInstanceArn: StrictStr | None = None
    ReplicationInstancePublicIpAddress: StrictStr | None = None
    ReplicationInstancePrivateIpAddress: StrictStr | None = None
    ReplicationInstancePublicIpAddresses: list[StrictStr] | None = None
    ReplicationInstancePrivateIpAddresses: list[StrictStr] | None = None
    ReplicationInstanceIpv6Addresses: list[StrictStr] | None = None
    PubliclyAccessible: StrictBool | None = None
    SecondaryAvailabilityZone: StrictStr | None = None
    FreeUntil: datetime.datetime | StrictStr | None = None
    DnsNameServers: StrictStr | None = None
    NetworkType: StrictStr | None = None
    KerberosAuthenticationSettings: DMSKerberosAuthenticationSettings | None = None
