from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_kerberos_authentication_settings import DMSKerberosAuthenticationSettings
from .dms_tag import DMSTag


class DMSCreateReplicationInstanceRequest(BaseModel):
    ReplicationInstanceIdentifier: StrictStr
    ReplicationInstanceClass: StrictStr
    AllocatedStorage: StrictInt | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    AvailabilityZone: StrictStr | None = None
    ReplicationSubnetGroupIdentifier: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    Tags: list[DMSTag] | None = None
    KmsKeyId: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    DnsNameServers: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
    NetworkType: StrictStr | None = None
    KerberosAuthenticationSettings: DMSKerberosAuthenticationSettings | None = None
