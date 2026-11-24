from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateKeyPairRequest(BaseModel):
    KeyName: StrictStr
    KeyType: Literal['rsa', 'ed25519'] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    KeyFormat: Literal['pem', 'ppk'] | None = None
    DryRun: StrictBool | None = None
