from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr
)


class AthenaEngineConfiguration(BaseModel):
    CoordinatorDpuSize: StrictInt
    MaxConcurrentDpus: StrictInt
    DefaultExecutorDpuSize: StrictInt
    AdditionalConfigs: dict[StrictStr, StrictStr]
    SparkProperties: dict[StrictStr, StrictStr]