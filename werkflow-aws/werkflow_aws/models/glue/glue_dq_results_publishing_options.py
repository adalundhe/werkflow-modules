from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDQResultsPublishingOptions(BaseModel):
    EvaluationContext: StrictStr | None = None
    ResultsS3Prefix: StrictStr | None = None
    CloudWatchMetricsEnabled: StrictBool | None = None
    ResultsPublishingEnabled: StrictBool | None = None
