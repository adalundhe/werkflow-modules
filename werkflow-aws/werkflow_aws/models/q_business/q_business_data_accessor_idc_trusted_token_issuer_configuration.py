from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDataAccessorIdcTrustedTokenIssuerConfiguration(BaseModel):
    idcTrustedTokenIssuerArn: StrictStr | None = None
