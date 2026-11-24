from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_attachment_ena_srd_specification import EC2AttachmentEnaSrdSpecification


class EC2NetworkInterfaceAttachment(BaseModel):
    AttachTime: datetime.datetime | StrictStr | None = None
    AttachmentId: StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
    DeviceIndex: StrictInt | None = None
    NetworkCardIndex: StrictInt | None = None
    InstanceId: StrictStr | None = None
    InstanceOwnerId: StrictStr | None = None
    Status: StrictStr | None = None
    EnaSrdSpecification: EC2AttachmentEnaSrdSpecification | None = None
    EnaQueueCount: StrictInt | None = None
