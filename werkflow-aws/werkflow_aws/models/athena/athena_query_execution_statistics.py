from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .athena_result_reuse_information_model import AthenaResultReuseInformationModel


class AthenaQueryExecutionStatistics(BaseModel):
    EngineExecutionTimeInMillis: StrictInt | None = None
    DataScannedInBytes: StrictInt | None = None
    DataManifestLocation: StrictStr | None = None
    TotalExecutionTimeInMillis: StrictInt | None = None
    QueryQueueTimeInMillis: StrictInt | None = None
    ServicePreProcessingTimeInMillis: StrictInt | None = None
    QueryPlanningTimeInMillis: StrictInt | None = None
    ServiceProcessingTimeInMillis: StrictInt | None = None
    ResultReuseInformation: AthenaResultReuseInformationModel | None = None
    DpuCount: StrictFloat | StrictInt | None = None
