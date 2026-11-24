from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerNetworkResource(BaseModel):
    RegisteredGatewayArn: StrictStr | None = None
    CoreNetworkId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
    AccountId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    Definition: StrictStr | None = None
    DefinitionTimestamp: datetime.datetime | StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
