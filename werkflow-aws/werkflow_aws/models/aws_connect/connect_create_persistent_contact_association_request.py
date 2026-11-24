from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectCreatePersistentContactAssociationRequest(BaseModel):
    InstanceId: StrictStr
    InitialContactId: StrictStr
    RehydrationType: Literal['ENTIRE_PAST_SESSION', 'FROM_SEGMENT']
    SourceContactId: StrictStr
    ClientToken: StrictStr | None = None
