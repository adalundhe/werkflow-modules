from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .emr_execution_engine_config import EMRExecutionEngineConfig
from .emr_notebook_s3_location_from_input import EMRNotebookS3LocationFromInput
from .emr_output_notebook_s3_location_from_input import EMROutputNotebookS3LocationFromInput
from .emr_tag import EMRTag


class EMRStartNotebookExecutionRequest(BaseModel):
    ExecutionEngine: EMRExecutionEngineConfig
    ServiceRole: StrictStr
    EditorId: StrictStr | None = None
    RelativePath: StrictStr | None = None
    NotebookExecutionName: StrictStr | None = None
    NotebookParams: StrictStr | None = None
    NotebookInstanceSecurityGroupId: StrictStr | None = None
    Tags: list[EMRTag] | None = None
    NotebookS3Location: EMRNotebookS3LocationFromInput | None = None
    OutputNotebookS3Location: EMROutputNotebookS3LocationFromInput | None = None
    OutputNotebookFormat: Literal['HTML'] | None = None
    EnvironmentVariables: dict[StrictStr, StrictStr] | None = None
