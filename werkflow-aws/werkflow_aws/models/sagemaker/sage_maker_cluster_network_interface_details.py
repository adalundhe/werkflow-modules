from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterNetworkInterfaceDetails(BaseModel):
    InterfaceType: StrictStr | None = None
