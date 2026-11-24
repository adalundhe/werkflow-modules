from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_notebook_instance_lifecycle_hook import SageMakerNotebookInstanceLifecycleHook


class SageMakerDescribeNotebookInstanceLifecycleConfigResponse(BaseModel):
    NotebookInstanceLifecycleConfigArn: StrictStr | None = None
    NotebookInstanceLifecycleConfigName: StrictStr | None = None
    OnCreate: list[SageMakerNotebookInstanceLifecycleHook] | None = None
    OnStart: list[SageMakerNotebookInstanceLifecycleHook] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
