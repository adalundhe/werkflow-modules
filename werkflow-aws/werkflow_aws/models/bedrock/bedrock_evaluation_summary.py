from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_evaluation_inference_config_summary import BedrockEvaluationInferenceConfigSummary


class BedrockEvaluationSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    status: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    jobType: StrictStr | None = None
    evaluationTaskTypes: list[StrictStr] | None = None
    modelIdentifiers: list[StrictStr] | None = None
    ragIdentifiers: list[StrictStr] | None = None
    evaluatorModelIdentifiers: list[StrictStr] | None = None
    customMetricsEvaluatorModelIdentifiers: list[StrictStr] | None = None
    inferenceConfigSummary: BedrockEvaluationInferenceConfigSummary | None = None
    applicationType: StrictStr | None = None
