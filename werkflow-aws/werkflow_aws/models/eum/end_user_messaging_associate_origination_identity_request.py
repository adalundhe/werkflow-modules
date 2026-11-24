from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingAssociateOriginationIdentityRequest(BaseModel):
    PoolId: StrictStr
    OriginationIdentity: StrictStr
    IsoCountryCode: StrictStr | None = None
    ClientToken: StrictStr | None = None
