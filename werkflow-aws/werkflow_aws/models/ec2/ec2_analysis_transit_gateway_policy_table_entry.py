from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_port_range import EC2PortRange


class EC2AnalysisTransitGatewayPolicyTableEntry(BaseModel):
    RuleNumber: StrictInt | None = None
    Protocol: StrictStr | None = None
    SourceCidr: StrictStr | None = None
    DestinationCidr: StrictStr | None = None
    SourcePortRange: EC2PortRange | None = None
    DestinationPortRange: EC2PortRange | None = None
    TargetRouteTableId: StrictStr | None = None
