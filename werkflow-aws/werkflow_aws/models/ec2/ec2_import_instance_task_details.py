from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_import_instance_volume_detail_item import EC2ImportInstanceVolumeDetailItem


class EC2ImportInstanceTaskDetails(BaseModel):
    Description: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Platform: StrictStr | None = None
    Volumes: list[EC2ImportInstanceVolumeDetailItem] | None = None
