from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerNotebookInstanceLifecycleConfigSummary(BaseModel):
    NotebookInstanceLifecycleConfigName: StrictStr | None = None
    NotebookInstanceLifecycleConfigArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
