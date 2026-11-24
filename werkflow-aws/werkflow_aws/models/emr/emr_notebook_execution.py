from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .emr_execution_engine_config import EMRExecutionEngineConfig
from .emr_notebook_s3_location_for_output import EMRNotebookS3LocationForOutput
from .emr_output_notebook_s3_location_for_output import EMROutputNotebookS3LocationForOutput
from .emr_tag import EMRTag


class EMRNotebookExecution(BaseModel):
    NotebookExecutionId: StrictStr | None = None
    EditorId: StrictStr | None = None
    ExecutionEngine: EMRExecutionEngineConfig | None = None
    NotebookExecutionName: StrictStr | None = None
    NotebookParams: StrictStr | None = None
    Status: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Arn: StrictStr | None = None
    OutputNotebookURI: StrictStr | None = None
    LastStateChangeReason: StrictStr | None = None
    NotebookInstanceSecurityGroupId: StrictStr | None = None
    Tags: list[EMRTag] | None = None
    NotebookS3Location: EMRNotebookS3LocationForOutput | None = None
    OutputNotebookS3Location: EMROutputNotebookS3LocationForOutput | None = None
    OutputNotebookFormat: StrictStr | None = None
    EnvironmentVariables: dict[StrictStr, StrictStr] | None = None
