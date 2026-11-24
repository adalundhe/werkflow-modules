from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyCreateThreatIntelSetRequest(BaseModel):
    DetectorId: StrictStr
    Name: StrictStr
    Format: Literal['TXT', 'STIX', 'OTX_CSV', 'ALIEN_VAULT', 'PROOF_POINT', 'FIRE_EYE']
    Location: StrictStr
    Activate: StrictBool
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ExpectedBucketOwner: StrictStr | None = None
