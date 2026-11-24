from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cluster_on_demand_options import SageMakerClusterOnDemandOptions
from .sage_maker_cluster_spot_options import SageMakerClusterSpotOptions


class SageMakerClusterCapacityRequirements(BaseModel):
    Spot: SageMakerClusterSpotOptions | None = None
    OnDemand: SageMakerClusterOnDemandOptions | None = None
