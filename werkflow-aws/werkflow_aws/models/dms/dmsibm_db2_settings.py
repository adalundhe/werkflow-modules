from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSIBMDb2Settings(BaseModel):
    DatabaseName: StrictStr | None = None
    Password: StrictStr | None = None
    Port: StrictInt | None = None
    ServerName: StrictStr | None = None
    SetDataCaptureChanges: StrictBool | None = None
    CurrentLsn: StrictStr | None = None
    MaxKBytesPerRead: StrictInt | None = None
    Username: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    LoadTimeout: StrictInt | None = None
    WriteBufferSize: StrictInt | None = None
    MaxFileSize: StrictInt | None = None
    KeepCsvFiles: StrictBool | None = None
