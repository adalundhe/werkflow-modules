from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsEc2NetworkInterfaceAttachment(BaseModel):
    AttachTime: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
    DeviceIndex: StrictInt | None = None
    InstanceId: StrictStr | None = None
    InstanceOwnerId: StrictStr | None = None
    Status: StrictStr | None = None
