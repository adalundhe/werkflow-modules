from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRSubjectIdentifier(BaseModel):
    imageDigest: StrictStr
