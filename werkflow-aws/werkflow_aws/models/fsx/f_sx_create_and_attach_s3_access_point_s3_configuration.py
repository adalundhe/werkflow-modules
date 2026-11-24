from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_s3_access_point_vpc_configuration import FSxS3AccessPointVpcConfiguration


class FSxCreateAndAttachS3AccessPointS3Configuration(BaseModel):
    VpcConfiguration: FSxS3AccessPointVpcConfiguration | None = None
    Policy: StrictStr | None = None
