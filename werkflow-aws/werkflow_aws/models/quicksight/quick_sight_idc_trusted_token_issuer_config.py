from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightIdcTrustedTokenIssuerConfig(BaseModel):
    IdcTrustedTokenIssuerArn: StrictStr | None = None
