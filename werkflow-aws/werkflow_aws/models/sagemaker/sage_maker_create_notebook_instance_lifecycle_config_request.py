from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_notebook_instance_lifecycle_hook import SageMakerNotebookInstanceLifecycleHook
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateNotebookInstanceLifecycleConfigRequest(BaseModel):
    NotebookInstanceLifecycleConfigName: StrictStr
    OnCreate: list[SageMakerNotebookInstanceLifecycleHook] | None = None
    OnStart: list[SageMakerNotebookInstanceLifecycleHook] | None = None
    Tags: list[SageMakerTagModel] | None = None
