from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_edge_output_config import SageMakerEdgeOutputConfig
from .sage_maker_edge_preset_deployment_output import SageMakerEdgePresetDeploymentOutput


class SageMakerDescribeEdgePackagingJobResponse(BaseModel):
    EdgePackagingJobArn: StrictStr | None = None
    EdgePackagingJobName: StrictStr | None = None
    CompilationJobName: StrictStr | None = None
    ModelName: StrictStr | None = None
    ModelVersion: StrictStr | None = None
    RoleArn: StrictStr | None = None
    OutputConfig: SageMakerEdgeOutputConfig | None = None
    ResourceKey: StrictStr | None = None
    EdgePackagingJobStatus: StrictStr | None = None
    EdgePackagingJobStatusMessage: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ModelArtifact: StrictStr | None = None
    ModelSignature: StrictStr | None = None
    PresetDeploymentOutput: SageMakerEdgePresetDeploymentOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
