from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_flex_cost_allocation_policy_document import EC2InstanceFlexCostAllocationPolicyDocument
from .ec2_nat_flex_cost_allocation_policy_document import EC2NatFlexCostAllocationPolicyDocument
from .ec2_pcx_flex_cost_allocation_policy_document import EC2PcxFlexCostAllocationPolicyDocument
from .ec2_tag_model import EC2TagModel


class EC2FlexCostAllocationPolicyDescription(BaseModel):
    FcaPolicyId: StrictStr | None = None
    FcaPolicyArn: StrictStr | None = None
    NetworkResourceType: StrictStr | None = None
    NatFcaPolicyDocument: EC2NatFlexCostAllocationPolicyDocument | None = None
    InstanceFcaPolicyDocument: EC2InstanceFlexCostAllocationPolicyDocument | None = None
    PcxFcaPolicyDocument: EC2PcxFlexCostAllocationPolicyDocument | None = None
    ShowBackEnabled: StrictBool | None = None
    OwnerAccount: StrictStr | None = None
    Description: StrictStr | None = None
    LatestVersion: StrictInt | None = None
    VersionExpectedEffectiveAt: datetime.datetime | StrictStr | None = None
    PolicyCreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ManagedBy: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
