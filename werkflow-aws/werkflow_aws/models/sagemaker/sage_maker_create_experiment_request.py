from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateExperimentRequest(BaseModel):
    ExperimentName: StrictStr
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
