from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class STSGetScopedCredentialsRequest(BaseModel):
    Policy: StrictStr | None = None
    DurationSeconds: StrictInt | None = None
    MinimumSessionTokenSize: StrictInt | None = None
    ScopedSessionDescription: StrictStr | None = None
