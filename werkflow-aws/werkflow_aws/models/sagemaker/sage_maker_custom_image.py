from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCustomImage(BaseModel):
    ImageName: StrictStr | None = None
    ImageVersionNumber: StrictInt | None = None
    AppImageConfigName: StrictStr | None = None
