from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSOracleSettings(BaseModel):
    AddSupplementalLogging: StrictBool | None = None
    ArchivedLogDestId: StrictInt | None = None
    AdditionalArchivedLogDestId: StrictInt | None = None
    ExtraArchivedLogDestIds: list[StrictInt] | None = None
    AllowSelectNestedTables: StrictBool | None = None
    ParallelAsmReadThreads: StrictInt | None = None
    ReadAheadBlocks: StrictInt | None = None
    AccessAlternateDirectly: StrictBool | None = None
    UseAlternateFolderForOnline: StrictBool | None = None
    OraclePathPrefix: StrictStr | None = None
    UsePathPrefix: StrictStr | None = None
    ReplacePathPrefix: StrictBool | None = None
    EnableHomogenousTablespace: StrictBool | None = None
    DirectPathNoLog: StrictBool | None = None
    ArchivedLogsOnly: StrictBool | None = None
    AsmPassword: StrictStr | None = None
    AsmServer: StrictStr | None = None
    AsmUser: StrictStr | None = None
    CharLengthSemantics: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DirectPathParallelLoad: StrictBool | None = None
    FailTasksOnLobTruncation: StrictBool | None = None
    NumberDatatypeScale: StrictInt | None = None
    Password: StrictStr | None = None
    Port: StrictInt | None = None
    ReadTableSpaceName: StrictBool | None = None
    RetryInterval: StrictInt | None = None
    SecurityDbEncryption: StrictStr | None = None
    SecurityDbEncryptionName: StrictStr | None = None
    ServerName: StrictStr | None = None
    SpatialDataOptionToGeoJsonFunctionName: StrictStr | None = None
    StandbyDelayTime: StrictInt | None = None
    Username: StrictStr | None = None
    UseBFile: StrictBool | None = None
    UseDirectPathFullLoad: StrictBool | None = None
    UseLogminerReader: StrictBool | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    SecretsManagerOracleAsmAccessRoleArn: StrictStr | None = None
    SecretsManagerOracleAsmSecretId: StrictStr | None = None
    TrimSpaceInChar: StrictBool | None = None
    ConvertTimestampWithZoneToUTC: StrictBool | None = None
    OpenTransactionWindow: StrictInt | None = None
    AuthenticationMethod: StrictStr | None = None
