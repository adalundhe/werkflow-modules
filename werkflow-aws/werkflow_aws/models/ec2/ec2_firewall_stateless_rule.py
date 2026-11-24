from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_port_range import EC2PortRange


class EC2FirewallStatelessRule(BaseModel):
    RuleGroupArn: StrictStr | None = None
    Sources: list[StrictStr] | None = None
    Destinations: list[StrictStr] | None = None
    SourcePorts: list[EC2PortRange] | None = None
    DestinationPorts: list[EC2PortRange] | None = None
    Protocols: list[StrictInt] | None = None
    RuleAction: StrictStr | None = None
    Priority: StrictInt | None = None
