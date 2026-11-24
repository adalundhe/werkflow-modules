from __future__ import annotations
from pydantic import BaseModel
from .emr_on_demand_provisioning_specification import EMROnDemandProvisioningSpecification
from .emr_spot_provisioning_specification import EMRSpotProvisioningSpecification


class EMRInstanceFleetProvisioningSpecifications(BaseModel):
    SpotSpecification: EMRSpotProvisioningSpecification | None = None
    OnDemandSpecification: EMROnDemandProvisioningSpecification | None = None
