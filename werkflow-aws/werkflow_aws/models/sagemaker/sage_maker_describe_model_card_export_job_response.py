from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_card_export_artifacts import SageMakerModelCardExportArtifacts
from .sage_maker_model_card_export_output_config import SageMakerModelCardExportOutputConfig


class SageMakerDescribeModelCardExportJobResponse(BaseModel):
    ModelCardExportJobName: StrictStr | None = None
    ModelCardExportJobArn: StrictStr | None = None
    Status: StrictStr | None = None
    ModelCardName: StrictStr | None = None
    ModelCardVersion: StrictInt | None = None
    OutputConfig: SageMakerModelCardExportOutputConfig | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastModifiedAt: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ExportArtifacts: SageMakerModelCardExportArtifacts | None = None
    ResponseMetadata: dict[str, Any] | None = None
