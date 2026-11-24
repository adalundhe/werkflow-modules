from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRTransitioningImageTotalCount(BaseModel):
    targetStorageClass: StrictStr | None = None
    imageTotalCount: StrictInt | None = None
