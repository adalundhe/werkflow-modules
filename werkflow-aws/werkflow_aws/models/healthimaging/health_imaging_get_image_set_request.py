from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingGetImageSetRequest(BaseModel):
    datastoreId: StrictStr
    imageSetId: StrictStr
    versionId: StrictStr | None = None
