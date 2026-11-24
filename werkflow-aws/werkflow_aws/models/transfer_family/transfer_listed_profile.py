from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferListedProfile(BaseModel):
    Arn: StrictStr | None = None
    ProfileId: StrictStr | None = None
    As2Id: StrictStr | None = None
    ProfileType: StrictStr | None = None
