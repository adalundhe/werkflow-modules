from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_distribution_data import GlueDistributionData


class GlueDataQualityAnalyzerResult(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    EvaluationMessage: StrictStr | None = None
    EvaluatedMetrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    EvaluatedDistributions: dict[StrictStr, GlueDistributionData] | None = None
