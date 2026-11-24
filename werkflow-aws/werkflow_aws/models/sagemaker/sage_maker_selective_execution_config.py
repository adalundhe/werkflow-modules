from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_selected_step import SageMakerSelectedStep


class SageMakerSelectiveExecutionConfig(BaseModel):
    SelectedSteps: list[SageMakerSelectedStep]
    SourcePipelineExecutionArn: StrictStr | None = None
