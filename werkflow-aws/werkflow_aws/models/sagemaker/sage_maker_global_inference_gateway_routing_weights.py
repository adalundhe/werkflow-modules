from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SageMakerGlobalInferenceGatewayRoutingWeights(BaseModel):
    KVHeadroom: StrictFloat | StrictInt | None = None
    QueueDepth: StrictFloat | StrictInt | None = None
    RegionProximity: StrictFloat | StrictInt | None = None
    ErrorRate: StrictFloat | StrictInt | None = None
