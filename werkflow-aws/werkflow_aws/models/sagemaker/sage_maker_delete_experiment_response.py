from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDeleteExperimentResponse(BaseModel):
    ExperimentArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
