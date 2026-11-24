from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListCapacityProvidersRequest(BaseModel):
    State: Literal['Pending', 'Active', 'Failed', 'Deleting'] | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
