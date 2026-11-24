from __future__ import annotations
from pydantic import BaseModel
from .emr_on_demand_resizing_specification import EMROnDemandResizingSpecification
from .emr_spot_resizing_specification import EMRSpotResizingSpecification


class EMRInstanceFleetResizingSpecifications(BaseModel):
    SpotResizeSpecification: EMRSpotResizingSpecification | None = None
    OnDemandResizeSpecification: EMROnDemandResizingSpecification | None = None
