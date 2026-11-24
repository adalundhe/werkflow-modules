from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2ImportKeyPairResponse(BaseModel):
    KeyFingerprint: StrictStr | None = None
    KeyName: StrictStr | None = None
    KeyPairId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
