from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsec2_security_group import RDSEC2SecurityGroup
from .rdsip_range import RDSIPRange


class RDSDBSecurityGroup(BaseModel):
    OwnerId: StrictStr | None = None
    DBSecurityGroupName: StrictStr | None = None
    DBSecurityGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    EC2SecurityGroups: list[RDSEC2SecurityGroup] | None = None
    IPRanges: list[RDSIPRange] | None = None
    DBSecurityGroupArn: StrictStr | None = None
