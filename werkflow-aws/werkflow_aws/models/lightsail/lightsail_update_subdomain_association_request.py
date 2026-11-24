from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailUpdateSubdomainAssociationRequest(BaseModel):
    subdomainName: StrictStr
    action: Literal['ASSOCIATE', 'DISASSOCIATE', 'TRANSFER']
    targetResourceArn: StrictStr | None = None
