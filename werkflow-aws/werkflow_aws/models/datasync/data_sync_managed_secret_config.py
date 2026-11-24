from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncManagedSecretConfig(BaseModel):
    SecretArn: StrictStr | None = None
