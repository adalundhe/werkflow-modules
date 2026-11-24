from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_metering_policy_rule import EC2TransitGatewayMeteringPolicyRule


class EC2TransitGatewayMeteringPolicyEntry(BaseModel):
    PolicyRuleNumber: StrictStr | None = None
    MeteredAccount: StrictStr | None = None
    State: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    UpdateEffectiveAt: datetime.datetime | StrictStr | None = None
    MeteringPolicyRule: EC2TransitGatewayMeteringPolicyRule | None = None
