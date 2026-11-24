from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSMicrosoftSQLServerSettings(BaseModel):
    Port: StrictInt | None = None
    BcpPacketSize: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    ControlTablesFileGroup: StrictStr | None = None
    Password: StrictStr | None = None
    QuerySingleAlwaysOnNode: StrictBool | None = None
    ReadBackupOnly: StrictBool | None = None
    SafeguardPolicy: StrictStr | None = None
    ServerName: StrictStr | None = None
    Username: StrictStr | None = None
    UseBcpFullLoad: StrictBool | None = None
    UseThirdPartyBackupDevice: StrictBool | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    TrimSpaceInChar: StrictBool | None = None
    TlogAccessMode: StrictStr | None = None
    ForceLobLookup: StrictBool | None = None
    AuthenticationMethod: StrictStr | None = None
