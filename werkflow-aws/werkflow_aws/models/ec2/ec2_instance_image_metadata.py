from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_image_metadata import EC2ImageMetadata
from .ec2_instance_state_model import EC2InstanceStateModel
from .ec2_operator_response import EC2OperatorResponse
from .ec2_tag_model import EC2TagModel


class EC2InstanceImageMetadata(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    ZoneId: StrictStr | None = None
    State: EC2InstanceStateModel | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ImageMetadata: EC2ImageMetadata | None = None
    Operator: EC2OperatorResponse | None = None
