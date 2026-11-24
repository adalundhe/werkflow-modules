from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CopyVolumesRequest(BaseModel):
    SourceVolumeId: StrictStr
    Iops: StrictInt | None = None
    Size: StrictInt | None = None
    VolumeType: Literal['standard', 'io1', 'io2', 'gp2', 'sc1', 'st1', 'gp3'] | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    MultiAttachEnabled: StrictBool | None = None
    Throughput: StrictInt | None = None
    ClientToken: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
