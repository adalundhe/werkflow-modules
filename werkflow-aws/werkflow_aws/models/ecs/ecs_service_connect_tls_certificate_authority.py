from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceConnectTlsCertificateAuthority(BaseModel):
    awsPcaAuthorityArn: StrictStr | None = None
