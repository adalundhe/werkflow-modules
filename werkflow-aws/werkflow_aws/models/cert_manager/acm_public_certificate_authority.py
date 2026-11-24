from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMPublicCertificateAuthority(BaseModel):
    AllowedKeyAlgorithms: list[StrictStr] | None = None
