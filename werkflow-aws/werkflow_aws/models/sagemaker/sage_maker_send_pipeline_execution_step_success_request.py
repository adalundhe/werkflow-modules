from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_output_parameter import SageMakerOutputParameter


class SageMakerSendPipelineExecutionStepSuccessRequest(BaseModel):
    CallbackToken: StrictStr
    OutputParameters: list[SageMakerOutputParameter] | None = None
    ClientRequestToken: StrictStr | None = None
