from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class NetworkManagerNetworkResourceSummary(BaseModel):
    RegisteredGatewayArn: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Definition: StrictStr | None = None
    NameTag: StrictStr | None = None
    IsMiddlebox: StrictBool | None = None
