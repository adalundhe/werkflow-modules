from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_sage_maker_pipeline_parameter import EventBridgeSageMakerPipelineParameter


class EventBridgeSageMakerPipelineParameters(BaseModel):
    PipelineParameterList: list[EventBridgeSageMakerPipelineParameter] | None = None
