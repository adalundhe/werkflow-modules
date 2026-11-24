from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClarifyShapBaselineConfig(BaseModel):
    MimeType: StrictStr | None = None
    ShapBaseline: StrictStr | None = None
    ShapBaselineUri: StrictStr | None = None
