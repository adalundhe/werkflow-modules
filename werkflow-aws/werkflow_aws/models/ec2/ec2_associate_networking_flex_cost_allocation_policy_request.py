from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_flex_cost_allocation_network_resource_scope import EC2FlexCostAllocationNetworkResourceScope


class EC2AssociateNetworkingFlexCostAllocationPolicyRequest(BaseModel):
    FcaPolicyId: StrictStr
    NetworkResourceIds: list[StrictStr] | None = None
    NetworkResourceScope: EC2FlexCostAllocationNetworkResourceScope | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
