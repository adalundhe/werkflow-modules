from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_notebook_instance_sort_key import SageMakerNotebookInstanceSortKey
from .sage_maker_notebook_instance_sort_order import SageMakerNotebookInstanceSortOrder
from .sage_maker_notebook_instance_status import SageMakerNotebookInstanceStatus


class SageMakerListNotebookInstancesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortBy: SageMakerNotebookInstanceSortKey | None = None
    SortOrder: SageMakerNotebookInstanceSortOrder | None = None
    NameContains: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | None = None
    CreationTimeAfter: datetime.datetime | None = None
    LastModifiedTimeBefore: datetime.datetime | None = None
    LastModifiedTimeAfter: datetime.datetime | None = None
    StatusEquals: SageMakerNotebookInstanceStatus | None = None
    NotebookInstanceLifecycleConfigNameContains: StrictStr | None = None
    DefaultCodeRepositoryContains: StrictStr | None = None
    AdditionalCodeRepositoryEquals: StrictStr | None = None
