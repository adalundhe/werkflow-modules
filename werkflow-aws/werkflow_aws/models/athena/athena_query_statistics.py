from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)
from .athena_result_reuse_information import AthenaResultReuseInformation


class AthenaQueryStatistics(BaseModel):
    EngineExecutionTimeInMillis: StrictInt
    DataScannedInBytes: StrictInt
    DataManifestLocation: StrictStr
    TotalExecutionTimeInMillis: StrictInt
    QueryQueueTimeInMillis: StrictInt
    ServicePreProcessingTimeInMillis: StrictInt
    QueryPlanningTimeInMillis: StrictInt
    ServiceProcessingTimeInMillis: StrictInt
    ResultReuseInformation: AthenaResultReuseInformation