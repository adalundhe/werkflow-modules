from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKKafkaClusterEncryptionInTransit(BaseModel):
    EncryptionType: StrictStr | None = None
    RootCaCertificate: StrictStr | None = None
