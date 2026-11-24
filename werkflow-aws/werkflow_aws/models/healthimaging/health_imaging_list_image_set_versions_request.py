from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class HealthImagingListImageSetVersionsRequest(BaseModel):
    datastoreId: StrictStr
    imageSetId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
