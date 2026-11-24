from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCreateModelResponse(BaseModel):
    ModelArn: StrictStr | None = None
