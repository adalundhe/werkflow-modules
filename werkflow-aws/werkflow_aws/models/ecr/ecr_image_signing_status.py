from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRImageSigningStatus(BaseModel):
    signingProfileArn: StrictStr | None = None
    failureCode: StrictStr | None = None
    failureReason: StrictStr | None = None
    status: StrictStr | None = None
