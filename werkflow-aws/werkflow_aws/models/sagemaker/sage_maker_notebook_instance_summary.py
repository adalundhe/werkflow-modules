from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_instance_type import SageMakerInstanceType
from .sage_maker_notebook_instance_status import SageMakerNotebookInstanceStatus


class SageMakerNotebookInstanceSummary(BaseModel):
    NotebookInstanceName: StrictStr | None = None
    NotebookInstanceArn: StrictStr | None = None
    NotebookInstanceStatus: SageMakerNotebookInstanceStatus | None = None
    Url: StrictStr | None = None
    InstanceType: SageMakerInstanceType | None = None
    CreationTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    NotebookInstanceLifecycleConfigName: StrictStr | None = None
    DefaultCodeRepository: StrictStr | None = None
    AdditionalCodeRepositories: list[StrictStr] | None = None
