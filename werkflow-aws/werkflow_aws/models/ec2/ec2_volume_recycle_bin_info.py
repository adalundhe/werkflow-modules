from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse


class EC2VolumeRecycleBinInfo(BaseModel):
    VolumeId: StrictStr | None = None
    VolumeType: StrictStr | None = None
    State: StrictStr | None = None
    Size: StrictInt | None = None
    Iops: StrictInt | None = None
    Throughput: StrictInt | None = None
    OutpostArn: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    SourceVolumeId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    RecycleBinEnterTime: datetime.datetime | StrictStr | None = None
    RecycleBinExitTime: datetime.datetime | StrictStr | None = None
