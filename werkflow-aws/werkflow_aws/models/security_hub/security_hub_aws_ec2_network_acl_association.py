from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2NetworkAclAssociation(BaseModel):
    NetworkAclAssociationId: StrictStr | None = None
    NetworkAclId: StrictStr | None = None
    SubnetId: StrictStr | None = None
