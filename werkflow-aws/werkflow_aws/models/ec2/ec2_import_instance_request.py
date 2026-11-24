from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_disk_image import EC2DiskImage
from .ec2_import_instance_launch_specification import EC2ImportInstanceLaunchSpecification


class EC2ImportInstanceRequest(BaseModel):
    Platform: Literal['Windows']
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    LaunchSpecification: EC2ImportInstanceLaunchSpecification | None = None
    DiskImages: list[EC2DiskImage] | None = None
