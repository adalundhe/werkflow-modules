from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_initialization_status_details import EC2InitializationStatusDetails
from .ec2_operator_response import EC2OperatorResponse
from .ec2_volume_status_action import EC2VolumeStatusAction
from .ec2_volume_status_attachment_status import EC2VolumeStatusAttachmentStatus
from .ec2_volume_status_event import EC2VolumeStatusEvent
from .ec2_volume_status_info import EC2VolumeStatusInfo


class EC2VolumeStatusItem(BaseModel):
    Actions: list[EC2VolumeStatusAction] | None = None
    AvailabilityZone: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    Events: list[EC2VolumeStatusEvent] | None = None
    VolumeId: StrictStr | None = None
    VolumeStatus: EC2VolumeStatusInfo | None = None
    AttachmentStatuses: list[EC2VolumeStatusAttachmentStatus] | None = None
    InitializationStatusDetails: EC2InitializationStatusDetails | None = None
    AvailabilityZoneId: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
