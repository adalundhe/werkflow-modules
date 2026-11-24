from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDisassociateOriginationIdentityRequest(BaseModel):
    PoolId: StrictStr
    OriginationIdentity: StrictStr
    IsoCountryCode: StrictStr | None = None
    ClientToken: StrictStr | None = None
