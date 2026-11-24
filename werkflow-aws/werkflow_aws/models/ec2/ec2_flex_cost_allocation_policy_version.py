from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_flex_cost_allocation_policy_document import EC2InstanceFlexCostAllocationPolicyDocument
from .ec2_nat_flex_cost_allocation_policy_document import EC2NatFlexCostAllocationPolicyDocument
from .ec2_pcx_flex_cost_allocation_policy_document import EC2PcxFlexCostAllocationPolicyDocument


class EC2FlexCostAllocationPolicyVersion(BaseModel):
    FcaPolicyId: StrictStr | None = None
    Version: StrictInt | None = None
    NetworkResourceType: StrictStr | None = None
    NatFcaPolicyDocument: EC2NatFlexCostAllocationPolicyDocument | None = None
    InstanceFcaPolicyDocument: EC2InstanceFlexCostAllocationPolicyDocument | None = None
    PcxFcaPolicyDocument: EC2PcxFlexCostAllocationPolicyDocument | None = None
    ShowBackEnabled: StrictBool | None = None
    Description: StrictStr | None = None
    ExpectedEffectiveAt: datetime.datetime | StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
