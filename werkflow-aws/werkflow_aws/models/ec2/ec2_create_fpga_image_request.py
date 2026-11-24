from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_storage_location import EC2StorageLocation
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateFpgaImageRequest(BaseModel):
    InputStorageLocation: EC2StorageLocation
    DryRun: StrictBool | None = None
    LogsStorageLocation: EC2StorageLocation | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
