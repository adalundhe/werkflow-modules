from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2ImportKeyPairRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyName: StrictStr
    PublicKeyMaterial: StrictBytes | BinaryIO | StrictStr
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
