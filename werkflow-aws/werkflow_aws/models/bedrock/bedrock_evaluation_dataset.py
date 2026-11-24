from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_evaluation_dataset_location import BedrockEvaluationDatasetLocation


class BedrockEvaluationDataset(BaseModel):
    name: StrictStr | None = None
    datasetLocation: BedrockEvaluationDatasetLocation | None = None
