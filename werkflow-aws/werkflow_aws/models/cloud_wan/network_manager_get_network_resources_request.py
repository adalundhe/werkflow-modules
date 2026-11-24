from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetNetworkResourcesRequest(BaseModel):
    GlobalNetworkId: StrictStr
    CoreNetworkId: StrictStr | None = None
    RegisteredGatewayArn: StrictStr | None = None
    AwsRegion: StrictStr | None = None
    AccountId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
