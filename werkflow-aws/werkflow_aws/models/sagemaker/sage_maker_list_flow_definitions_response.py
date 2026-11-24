from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_flow_definition_summary import SageMakerFlowDefinitionSummary


class SageMakerListFlowDefinitionsResponse(BaseModel):
    FlowDefinitionSummaries: list[SageMakerFlowDefinitionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
