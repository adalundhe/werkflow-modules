from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_notebook_instance_lifecycle_config_summary import SageMakerNotebookInstanceLifecycleConfigSummary


class SageMakerListNotebookInstanceLifecycleConfigsResponse(BaseModel):
    NextToken: StrictStr | None = None
    NotebookInstanceLifecycleConfigs: list[SageMakerNotebookInstanceLifecycleConfigSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
