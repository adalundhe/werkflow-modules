from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDerivedInformation(BaseModel):
    DerivedDataInputConfig: StrictStr | None = None
