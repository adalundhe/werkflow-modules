from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSMongoDbSettings(BaseModel):
    Username: StrictStr | None = None
    Password: StrictStr | None = None
    ServerName: StrictStr | None = None
    Port: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    AuthType: StrictStr | None = None
    AuthMechanism: StrictStr | None = None
    NestingLevel: StrictStr | None = None
    ExtractDocId: StrictStr | None = None
    DocsToInvestigate: StrictStr | None = None
    AuthSource: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    SecretsManagerSecretId: StrictStr | None = None
    UseUpdateLookUp: StrictBool | None = None
    ReplicateShardCollections: StrictBool | None = None
