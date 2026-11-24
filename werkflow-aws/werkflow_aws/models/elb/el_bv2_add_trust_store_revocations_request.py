from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_revocation_content import ELBv2RevocationContent


class ELBv2AddTrustStoreRevocationsRequest(BaseModel):
    TrustStoreArn: StrictStr
    RevocationContents: list[ELBv2RevocationContent] | None = None
