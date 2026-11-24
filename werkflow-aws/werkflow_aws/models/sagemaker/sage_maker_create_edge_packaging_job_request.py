from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_edge_output_config import SageMakerEdgeOutputConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateEdgePackagingJobRequest(BaseModel):
    EdgePackagingJobName: StrictStr
    CompilationJobName: StrictStr
    ModelName: StrictStr
    ModelVersion: StrictStr
    RoleArn: StrictStr
    OutputConfig: SageMakerEdgeOutputConfig
    ResourceKey: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
