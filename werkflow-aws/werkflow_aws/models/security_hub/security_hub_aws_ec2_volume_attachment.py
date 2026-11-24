from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEc2VolumeAttachment(BaseModel):
    AttachTime: StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
    InstanceId: StrictStr | None = None
    Status: StrictStr | None = None
