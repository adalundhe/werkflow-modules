from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListFunctionVersionsByCapacityProviderRequest(BaseModel):
    CapacityProviderName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
