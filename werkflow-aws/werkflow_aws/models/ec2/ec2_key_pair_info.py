from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag import EC2Tag


class EC2KeyPairInfo(BaseModel):
    KeyPairId: StrictStr | None = None
    KeyFingerprint: StrictStr | None = None
    KeyName: StrictStr | None = None
    KeyType: StrictStr | None = None
    PublicKey: StrictStr | None = None
    CreateTime: datetime.datetime | None = None
    Tags: list[EC2Tag] | None = None
