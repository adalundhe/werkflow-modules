from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontPublicKeyConfig(BaseModel):
    CallerReference: StrictStr | None = None
    Name: StrictStr | None = None
    EncodedKey: StrictStr | None = None
    Comment: StrictStr | None = None
