from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_rds_db_security_group_ec2_security_group import SecurityHubAwsRdsDbSecurityGroupEc2SecurityGroup
from .security_hub_aws_rds_db_security_group_ip_range import SecurityHubAwsRdsDbSecurityGroupIpRange


class SecurityHubAwsRdsDbSecurityGroupDetails(BaseModel):
    DbSecurityGroupArn: StrictStr | None = None
    DbSecurityGroupDescription: StrictStr | None = None
    DbSecurityGroupName: StrictStr | None = None
    Ec2SecurityGroups: list[SecurityHubAwsRdsDbSecurityGroupEc2SecurityGroup] | None = None
    IpRanges: list[SecurityHubAwsRdsDbSecurityGroupIpRange] | None = None
    OwnerId: StrictStr | None = None
    VpcId: StrictStr | None = None
