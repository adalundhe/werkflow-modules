from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncCustomSecretConfig(BaseModel):
    SecretArn: StrictStr | None = None
    SecretAccessRoleArn: StrictStr | None = None
