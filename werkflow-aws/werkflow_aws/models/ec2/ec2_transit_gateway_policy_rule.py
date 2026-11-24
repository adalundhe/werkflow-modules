from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_policy_rule_meta_data import EC2TransitGatewayPolicyRuleMetaData


class EC2TransitGatewayPolicyRule(BaseModel):
    SourceCidrBlock: StrictStr | None = None
    SourcePortRange: StrictStr | None = None
    DestinationCidrBlock: StrictStr | None = None
    DestinationPortRange: StrictStr | None = None
    Protocol: StrictStr | None = None
    MetaData: EC2TransitGatewayPolicyRuleMetaData | None = None
