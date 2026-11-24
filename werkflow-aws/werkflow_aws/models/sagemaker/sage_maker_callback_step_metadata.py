from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_output_parameter import SageMakerOutputParameter


class SageMakerCallbackStepMetadata(BaseModel):
    CallbackToken: StrictStr | None = None
    SqsQueueUrl: StrictStr | None = None
    OutputParameters: list[SageMakerOutputParameter] | None = None
