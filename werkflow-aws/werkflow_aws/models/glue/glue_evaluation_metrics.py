from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_find_matches_metrics import GlueFindMatchesMetrics


class GlueEvaluationMetrics(BaseModel):
    TransformType: StrictStr | None = None
    FindMatchesMetrics: GlueFindMatchesMetrics | None = None
