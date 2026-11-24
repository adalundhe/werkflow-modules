from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails(BaseModel):
    InCluster: StrictBool | None = None
    ClientBroker: StrictStr | None = None
