from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_flex_cost_allocation_policy_document import EC2InstanceFlexCostAllocationPolicyDocument
from .ec2_nat_flex_cost_allocation_policy_document import EC2NatFlexCostAllocationPolicyDocument
from .ec2_pcx_flex_cost_allocation_policy_document import EC2PcxFlexCostAllocationPolicyDocument
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateNetworkingFlexCostAllocationPolicyRequest(BaseModel):
    NetworkResourceType: Literal['natgw', 'pcx', 'ec2']
    NatFcaPolicyDocument: EC2NatFlexCostAllocationPolicyDocument | None = None
    InstanceFcaPolicyDocument: EC2InstanceFlexCostAllocationPolicyDocument | None = None
    PcxFcaPolicyDocument: EC2PcxFlexCostAllocationPolicyDocument | None = None
    ShowBackEnabled: StrictBool | None = None
    Description: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
