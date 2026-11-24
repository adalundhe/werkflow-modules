from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSRedshiftSettings(BaseModel):
    AcceptAnyDate: StrictBool | None = None
    AfterConnectScript: StrictStr | None = None
    BucketFolder: StrictStr | None = None
    BucketName: StrictStr | None = None
    CaseSensitiveNames: StrictBool | None = None
    CompUpdate: StrictBool | None = None
    ConnectionTimeout: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    DateFormat: StrictStr | None = None
    EmptyAsNull: StrictBool | None = None
    EncryptionMode: StrictStr | None = None
    ExplicitIds: StrictBool | None = None
    FileTransferUploadStreams: StrictInt | None = None
    LoadTimeout: StrictInt | None = None
    MaxFileSize: StrictInt | None = None
    Password: StrictStr | None = None
    Port: StrictInt | None = None
    RemoveQuotes: StrictBool | None = None
    ReplaceInvalidChars: StrictStr | None = None
    ReplaceChars: StrictStr | None = None
    ServerName: StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    ServerSideEncryptionKmsKeyId: StrictStr | None = None
    TimeFormat: StrictStr | None = None
    TrimBlanks: StrictBool | None = None
    TruncateColumns: StrictBool | None = None
    Username: StrictStr | None = None
    WriteBufferSize: StrictInt | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    MapBooleanAsBoolean: StrictBool | None = None
