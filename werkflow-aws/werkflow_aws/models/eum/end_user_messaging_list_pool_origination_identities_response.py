from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_origination_identity_metadata import EndUserMessagingOriginationIdentityMetadata


class EndUserMessagingListPoolOriginationIdentitiesResponse(BaseModel):
    PoolArn: StrictStr | None = None
    PoolId: StrictStr | None = None
    OriginationIdentities: list[EndUserMessagingOriginationIdentityMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
