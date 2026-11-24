from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDataProcessing(BaseModel):
    InputFilter: StrictStr | None = None
    OutputFilter: StrictStr | None = None
    JoinSource: StrictStr | None = None
