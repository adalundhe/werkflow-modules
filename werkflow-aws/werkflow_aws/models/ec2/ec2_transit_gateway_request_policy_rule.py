from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_request_policy_rule_meta_data import EC2TransitGatewayRequestPolicyRuleMetaData


class EC2TransitGatewayRequestPolicyRule(BaseModel):
    SourceCidrBlock: StrictStr | None = None
    SourcePortRange: StrictStr | None = None
    DestinationCidrBlock: StrictStr | None = None
    DestinationPortRange: StrictStr | None = None
    Protocol: StrictStr | None = None
    MetaData: EC2TransitGatewayRequestPolicyRuleMetaData | None = None
