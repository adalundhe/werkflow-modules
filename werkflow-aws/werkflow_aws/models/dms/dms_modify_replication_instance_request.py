from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_kerberos_authentication_settings import DMSKerberosAuthenticationSettings


class DMSModifyReplicationInstanceRequest(BaseModel):
    ReplicationInstanceArn: StrictStr
    AllocatedStorage: StrictInt | None = None
    ApplyImmediately: StrictBool | None = None
    ReplicationInstanceClass: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    ReplicationInstanceIdentifier: StrictStr | None = None
    NetworkType: StrictStr | None = None
    KerberosAuthenticationSettings: DMSKerberosAuthenticationSettings | None = None
