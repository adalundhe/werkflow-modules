from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_output_parameter import SageMakerOutputParameter


class SageMakerLambdaStepMetadata(BaseModel):
    Arn: StrictStr | None = None
    OutputParameters: list[SageMakerOutputParameter] | None = None
