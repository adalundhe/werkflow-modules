from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKEncryptionAtRestModel(BaseModel):
    DataVolumeKMSKeyId: StrictStr | None = None
