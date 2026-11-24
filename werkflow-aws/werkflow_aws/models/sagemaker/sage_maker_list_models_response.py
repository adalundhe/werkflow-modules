from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_summary import SageMakerModelSummary


class SageMakerListModelsResponse(BaseModel):
    Models: list[SageMakerModelSummary] | None = None
    NextToken: StrictStr | None = None
