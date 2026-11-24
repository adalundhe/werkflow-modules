from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_dq_results_publishing_options import GlueDQResultsPublishingOptions
from .glue_dq_stop_job_on_failure_options import GlueDQStopJobOnFailureOptions


class GlueEvaluateDataQuality(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Ruleset: StrictStr | None = None
    Output: StrictStr | None = None
    PublishingOptions: GlueDQResultsPublishingOptions | None = None
    StopJobOnFailureOptions: GlueDQStopJobOnFailureOptions | None = None
