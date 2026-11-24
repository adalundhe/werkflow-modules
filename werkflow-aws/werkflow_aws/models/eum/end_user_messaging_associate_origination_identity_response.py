from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingAssociateOriginationIdentityResponse(BaseModel):
    PoolArn: StrictStr | None = None
    PoolId: StrictStr | None = None
    OriginationIdentityArn: StrictStr | None = None
    OriginationIdentity: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
