from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneAssociateGovernedTermsRequest(BaseModel):
    domainIdentifier: StrictStr
    entityIdentifier: StrictStr
    entityType: Literal['ASSET']
    governedGlossaryTerms: list[StrictStr]
