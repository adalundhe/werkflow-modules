from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_import_instance_task_details import EC2ImportInstanceTaskDetails
from .ec2_import_volume_task_details import EC2ImportVolumeTaskDetails
from .ec2_tag_model import EC2TagModel


class EC2ConversionTask(BaseModel):
    ConversionTaskId: StrictStr | None = None
    ExpirationTime: StrictStr | None = None
    ImportInstance: EC2ImportInstanceTaskDetails | None = None
    ImportVolume: EC2ImportVolumeTaskDetails | None = None
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
