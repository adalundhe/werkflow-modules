from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSPostgreSQLSettings(BaseModel):
    AfterConnectScript: StrictStr | None = None
    CaptureDdls: StrictBool | None = None
    MaxFileSize: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    DdlArtifactsSchema: StrictStr | None = None
    ExecuteTimeout: StrictInt | None = None
    FailTasksOnLobTruncation: StrictBool | None = None
    HeartbeatEnable: StrictBool | None = None
    HeartbeatSchema: StrictStr | None = None
    HeartbeatFrequency: StrictInt | None = None
    Password: StrictStr | None = None
    Port: StrictInt | None = None
    ServerName: StrictStr | None = None
    Username: StrictStr | None = None
    SlotName: StrictStr | None = None
    PluginName: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    TrimSpaceInChar: StrictBool | None = None
    MapBooleanAsBoolean: StrictBool | None = None
    MapJsonbAsClob: StrictBool | None = None
    MapLongVarcharAs: StrictStr | None = None
    DatabaseMode: StrictStr | None = None
    BabelfishDatabaseName: StrictStr | None = None
    DisableUnicodeSourceFilter: StrictBool | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    AuthenticationMethod: StrictStr | None = None
