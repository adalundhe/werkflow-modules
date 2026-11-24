from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSOracleDataProviderSettings(BaseModel):
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    SslMode: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    AsmServer: StrictStr | None = None
    SecretsManagerOracleAsmSecretId: StrictStr | None = None
    SecretsManagerOracleAsmAccessRoleArn: StrictStr | None = None
    SecretsManagerSecurityDbEncryptionSecretId: StrictStr | None = None
    SecretsManagerSecurityDbEncryptionAccessRoleArn: StrictStr | None = None
    S3Path: StrictStr | None = None
    S3AccessRoleArn: StrictStr | None = None
