from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse


class EC2EbsInstanceBlockDevice(BaseModel):
    AttachTime: datetime.datetime | StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
    Status: StrictStr | None = None
    VolumeId: StrictStr | None = None
    AssociatedResource: StrictStr | None = None
    VolumeOwnerId: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
    EbsCardIndex: StrictInt | None = None
