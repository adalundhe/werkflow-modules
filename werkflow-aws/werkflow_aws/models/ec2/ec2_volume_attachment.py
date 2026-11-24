from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2VolumeAttachment(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    AssociatedResource: StrictStr | None = None
    InstanceOwningService: StrictStr | None = None
    EbsCardIndex: StrictInt | None = None
    VolumeId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Device: StrictStr | None = None
    State: StrictStr | None = None
    AttachTime: datetime.datetime | StrictStr | None = None
