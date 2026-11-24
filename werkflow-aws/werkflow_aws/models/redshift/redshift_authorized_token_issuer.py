from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAuthorizedTokenIssuer(BaseModel):
    TrustedTokenIssuerArn: StrictStr | None = None
    AuthorizedAudiencesList: list[StrictStr] | None = None
