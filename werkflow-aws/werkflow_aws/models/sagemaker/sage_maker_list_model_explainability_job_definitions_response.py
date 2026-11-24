from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_job_definition_summary import SageMakerMonitoringJobDefinitionSummary


class SageMakerListModelExplainabilityJobDefinitionsResponse(BaseModel):
    JobDefinitionSummaries: list[SageMakerMonitoringJobDefinitionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
