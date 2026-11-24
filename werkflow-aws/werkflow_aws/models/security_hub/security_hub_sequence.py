from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_actor import SecurityHubActor
from .security_hub_indicator import SecurityHubIndicator
from .security_hub_network_endpoint import SecurityHubNetworkEndpoint
from .security_hub_signal import SecurityHubSignal


class SecurityHubSequence(BaseModel):
    Uid: StrictStr | None = None
    Actors: list[SecurityHubActor] | None = None
    Endpoints: list[SecurityHubNetworkEndpoint] | None = None
    Signals: list[SecurityHubSignal] | None = None
    SequenceIndicators: list[SecurityHubIndicator] | None = None
