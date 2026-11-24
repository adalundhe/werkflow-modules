from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2IpamPolicy(BaseModel):
    OwnerId: StrictStr | None = None
    IpamPolicyId: StrictStr | None = None
    IpamPolicyArn: StrictStr | None = None
    IpamPolicyRegion: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    IpamId: StrictStr | None = None
