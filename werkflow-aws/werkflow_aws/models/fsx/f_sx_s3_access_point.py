from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_s3_access_point_vpc_configuration import FSxS3AccessPointVpcConfiguration


class FSxS3AccessPoint(BaseModel):
    ResourceARN: StrictStr | None = None
    Alias: StrictStr | None = None
    VpcConfiguration: FSxS3AccessPointVpcConfiguration | None = None
