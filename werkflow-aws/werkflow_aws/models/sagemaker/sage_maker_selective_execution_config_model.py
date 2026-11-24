from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_selected_step_model import SageMakerSelectedStepModel


class SageMakerSelectiveExecutionConfigModel(BaseModel):
    SourcePipelineExecutionArn: StrictStr | None = None
    SelectedSteps: list[SageMakerSelectedStepModel] | None = None
