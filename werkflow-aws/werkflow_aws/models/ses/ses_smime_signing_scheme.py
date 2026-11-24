from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESSmimeSigningScheme(BaseModel):
    SignatureFormat: StrictStr | None = None
