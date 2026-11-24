from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .emr_notebook_s3_location_for_output import EMRNotebookS3LocationForOutput


class EMRNotebookExecutionSummary(BaseModel):
    NotebookExecutionId: StrictStr | None = None
    EditorId: StrictStr | None = None
    NotebookExecutionName: StrictStr | None = None
    Status: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    NotebookS3Location: EMRNotebookS3LocationForOutput | None = None
    ExecutionEngineId: StrictStr | None = None
