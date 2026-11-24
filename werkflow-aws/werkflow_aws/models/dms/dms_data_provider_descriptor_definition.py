from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDataProviderDescriptorDefinition(BaseModel):
    DataProviderIdentifier: StrictStr
    SecretsManagerSecretId: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
