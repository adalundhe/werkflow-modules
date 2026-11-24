from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruKMSServerSideEncryptionIntegration(BaseModel):
    KMSKeyId: StrictStr | None = None
    OptInStatus: StrictStr | None = None
    Type: StrictStr | None = None
