from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDataProviderDescriptor(BaseModel):
    SecretsManagerSecretId: StrictStr | None = None
    SecretsManagerAccessRoleArn: StrictStr | None = None
    DataProviderName: StrictStr | None = None
    DataProviderArn: StrictStr | None = None
