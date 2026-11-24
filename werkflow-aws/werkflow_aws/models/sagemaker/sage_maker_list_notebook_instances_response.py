from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_notebook_instance_summary import SageMakerNotebookInstanceSummary


class SageMakerListNotebookInstancesResponse(BaseModel):
    NextToken: StrictStr | None = None
    NotebookInstances: list[SageMakerNotebookInstanceSummary] | None = None
