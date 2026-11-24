from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag


class TransferDescribedProfile(BaseModel):
    Arn: StrictStr | None = None
    ProfileId: StrictStr | None = None
    ProfileType: StrictStr | None = None
    As2Id: StrictStr | None = None
    CertificateIds: list[StrictStr] | None = None
    Tags: list[TransferTag] | None = None
