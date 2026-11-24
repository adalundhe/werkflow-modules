from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_network_acl_association import EC2NetworkAclAssociation
from .ec2_network_acl_entry import EC2NetworkAclEntry
from .ec2_tag_model import EC2TagModel


class EC2NetworkAcl(BaseModel):
    Associations: list[EC2NetworkAclAssociation] | None = None
    Entries: list[EC2NetworkAclEntry] | None = None
    IsDefault: StrictBool | None = None
    NetworkAclId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    VpcId: StrictStr | None = None
    OwnerId: StrictStr | None = None
