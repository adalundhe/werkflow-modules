from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_instance_identity import DataPipelineInstanceIdentity


class DataPipelinePollForTaskRequest(BaseModel):
    workerGroup: StrictStr
    hostname: StrictStr | None = None
    instanceIdentity: DataPipelineInstanceIdentity | None = None
