from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerTrialComponentParameterValue(BaseModel):
    StringValue: StrictStr | None = None
    NumberValue: StrictFloat | StrictInt | None = None
