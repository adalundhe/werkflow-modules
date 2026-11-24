from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeImageVersionRequest(BaseModel):
    ImageName: StrictStr
    Version: StrictInt | None = None
    Alias: StrictStr | None = None
