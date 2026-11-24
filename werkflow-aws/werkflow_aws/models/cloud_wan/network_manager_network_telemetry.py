from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_connection_health import NetworkManagerConnectionHealth


class NetworkManagerNetworkTelemetry(BaseModel):
    RegisteredGatewayArn: StrictStr | None = None
    CoreNetworkId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
    AccountId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    Address: StrictStr | None = None
    Health: NetworkManagerConnectionHealth | None = None
