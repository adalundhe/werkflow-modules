from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_ec2_network_acl_association import SecurityHubAwsEc2NetworkAclAssociation
from .security_hub_aws_ec2_network_acl_entry import SecurityHubAwsEc2NetworkAclEntry


class SecurityHubAwsEc2NetworkAclDetails(BaseModel):
    IsDefault: StrictBool | None = None
    NetworkAclId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    VpcId: StrictStr | None = None
    Associations: list[SecurityHubAwsEc2NetworkAclAssociation] | None = None
    Entries: list[SecurityHubAwsEc2NetworkAclEntry] | None = None
