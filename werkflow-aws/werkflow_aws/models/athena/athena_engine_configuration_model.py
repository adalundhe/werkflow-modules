from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .athena_classification import AthenaClassification


class AthenaEngineConfigurationModel(BaseModel):
    CoordinatorDpuSize: StrictInt | None = None
    MaxConcurrentDpus: StrictInt | None = None
    DefaultExecutorDpuSize: StrictInt | None = None
    AdditionalConfigs: dict[StrictStr, StrictStr] | None = None
    SparkProperties: dict[StrictStr, StrictStr] | None = None
    Classifications: list[AthenaClassification] | None = None
