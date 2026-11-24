from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKEncryptionInTransitModel(BaseModel):
    ClientBroker: StrictStr | None = None
    InCluster: StrictBool | None = None
