from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSMySQLSettings(BaseModel):
    AfterConnectScript: StrictStr | None = None
    CleanSourceMetadataOnMismatch: StrictBool | None = None
    DatabaseName: StrictStr | None = None
    EventsPollInterval: StrictInt | None = None
    TargetDbType: StrictStr | None = None
    MaxFileSize: StrictInt | None = None
    ParallelLoadThreads: StrictInt | None = None
    Password: StrictStr | None = None
    Port: StrictInt | None = None
    ServerName: StrictStr | None = None
    ServerTimezone: StrictStr | None = None
    Username: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    ExecuteTimeout: StrictInt | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    AuthenticationMethod: StrictStr | None = None
