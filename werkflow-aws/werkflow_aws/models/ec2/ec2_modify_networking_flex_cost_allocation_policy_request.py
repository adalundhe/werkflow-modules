from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_flex_cost_allocation_policy_document import EC2InstanceFlexCostAllocationPolicyDocument
from .ec2_nat_flex_cost_allocation_policy_document import EC2NatFlexCostAllocationPolicyDocument
from .ec2_pcx_flex_cost_allocation_policy_document import EC2PcxFlexCostAllocationPolicyDocument


class EC2ModifyNetworkingFlexCostAllocationPolicyRequest(BaseModel):
    FcaPolicyId: StrictStr
    NatFcaPolicyDocument: EC2NatFlexCostAllocationPolicyDocument | None = None
    InstanceFcaPolicyDocument: EC2InstanceFlexCostAllocationPolicyDocument | None = None
    PcxFcaPolicyDocument: EC2PcxFlexCostAllocationPolicyDocument | None = None
    ShowBackEnabled: StrictBool | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
