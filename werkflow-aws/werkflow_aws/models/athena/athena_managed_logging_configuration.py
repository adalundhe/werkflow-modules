from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AthenaManagedLoggingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    KmsKey: StrictStr | None = None
