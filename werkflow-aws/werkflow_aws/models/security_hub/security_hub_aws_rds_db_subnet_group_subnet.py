from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_rds_db_subnet_group_subnet_availability_zone import SecurityHubAwsRdsDbSubnetGroupSubnetAvailabilityZone


class SecurityHubAwsRdsDbSubnetGroupSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: SecurityHubAwsRdsDbSubnetGroupSubnetAvailabilityZone | None = None
    SubnetStatus: StrictStr | None = None
