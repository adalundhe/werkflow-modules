from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailHostKeyAttributes(BaseModel):
    algorithm: StrictStr | None = None
    publicKey: StrictStr | None = None
    witnessedAt: datetime.datetime | StrictStr | None = None
    fingerprintSHA1: StrictStr | None = None
    fingerprintSHA256: StrictStr | None = None
    notValidBefore: datetime.datetime | StrictStr | None = None
    notValidAfter: datetime.datetime | StrictStr | None = None
