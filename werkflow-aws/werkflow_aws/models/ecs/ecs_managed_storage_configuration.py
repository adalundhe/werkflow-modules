from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSManagedStorageConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None
    fargateEphemeralStorageKmsKeyId: StrictStr | None = None
