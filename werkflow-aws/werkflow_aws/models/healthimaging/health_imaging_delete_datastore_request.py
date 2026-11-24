from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingDeleteDatastoreRequest(BaseModel):
    datastoreId: StrictStr
