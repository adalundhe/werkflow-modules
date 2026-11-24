from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2ExportToS3TaskSpecification(BaseModel):
    DiskImageFormat: Literal['VMDK', 'RAW', 'VHD'] | None = None
    ContainerFormat: Literal['ova'] | None = None
    S3Bucket: StrictStr | None = None
    S3Prefix: StrictStr | None = None
