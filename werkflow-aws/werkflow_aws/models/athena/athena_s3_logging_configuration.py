from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AthenaS3LoggingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    KmsKey: StrictStr | None = None
    LogLocation: StrictStr | None = None
