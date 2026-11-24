from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSDocDbSettings(BaseModel):
    Username: StrictStr | None = None
    Password: StrictStr | None = None
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    NestingLevel: StrictStr | None = None
    ExtractDocId: StrictBool | None = None
    DocsToInvestigate: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    UseUpdateLookUp: StrictBool | None = None
    ReplicateShardCollections: StrictBool | None = None
