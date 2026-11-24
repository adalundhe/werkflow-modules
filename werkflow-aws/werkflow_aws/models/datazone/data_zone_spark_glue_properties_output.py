from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_spark_glue_args import DataZoneSparkGlueArgs


class DataZoneSparkGluePropertiesOutput(BaseModel):
    additionalArgs: DataZoneSparkGlueArgs | None = None
    glueConnectionName: StrictStr | None = None
    glueConnectionNames: list[StrictStr] | None = None
    glueVersion: StrictStr | None = None
    idleTimeout: StrictInt | None = None
    javaVirtualEnv: StrictStr | None = None
    numberOfWorkers: StrictInt | None = None
    pythonVirtualEnv: StrictStr | None = None
    workerType: StrictStr | None = None
