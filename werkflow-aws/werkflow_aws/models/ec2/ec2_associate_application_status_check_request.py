from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_custom_tag_key_value_request_pair import EC2CustomTagKeyValueRequestPair


class EC2AssociateApplicationStatusCheckRequest(BaseModel):
    ApplicationStatusCheckId: StrictStr
    TargetTagAssociations: list[EC2CustomTagKeyValueRequestPair] | None = None
    InstanceIds: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
