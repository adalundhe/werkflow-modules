from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_adapter_version_dataset_config import TextractAdapterVersionDatasetConfig
from .textract_adapter_version_evaluation_metric import TextractAdapterVersionEvaluationMetric
from .textract_output_config import TextractOutputConfig


class TextractGetAdapterVersionResponse(BaseModel):
    AdapterId: StrictStr | None = None
    AdapterVersion: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FeatureTypes: list[StrictStr] | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    DatasetConfig: TextractAdapterVersionDatasetConfig | None = None
    KMSKeyId: StrictStr | None = None
    OutputConfig: TextractOutputConfig | None = None
    EvaluationMetrics: list[TextractAdapterVersionEvaluationMetric] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
