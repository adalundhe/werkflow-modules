from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse


class EC2VolumeModification(BaseModel):
    VolumeId: StrictStr | None = None
    ModificationState: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    TargetSize: StrictInt | None = None
    TargetIops: StrictInt | None = None
    TargetVolumeType: StrictStr | None = None
    TargetThroughput: StrictInt | None = None
    TargetMultiAttachEnabled: StrictBool | None = None
    OriginalSize: StrictInt | None = None
    OriginalIops: StrictInt | None = None
    OriginalVolumeType: StrictStr | None = None
    OriginalThroughput: StrictInt | None = None
    OriginalMultiAttachEnabled: StrictBool | None = None
    Progress: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
