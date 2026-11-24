from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_rds_db_subnet_group_subnet import SecurityHubAwsRdsDbSubnetGroupSubnet


class SecurityHubAwsRdsDbSubnetGroup(BaseModel):
    DbSubnetGroupName: StrictStr | None = None
    DbSubnetGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetGroupStatus: StrictStr | None = None
    Subnets: list[SecurityHubAwsRdsDbSubnetGroupSubnet] | None = None
    DbSubnetGroupArn: StrictStr | None = None
