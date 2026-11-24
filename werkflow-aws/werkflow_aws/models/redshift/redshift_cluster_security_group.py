from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_ec2_security_group import RedshiftEC2SecurityGroup
from .redshift_ip_range import RedshiftIPRange
from .redshift_tag import RedshiftTag


class RedshiftClusterSecurityGroup(BaseModel):
    ClusterSecurityGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    EC2SecurityGroups: list[RedshiftEC2SecurityGroup] | None = None
    IPRanges: list[RedshiftIPRange] | None = None
    Tags: list[RedshiftTag] | None = None
