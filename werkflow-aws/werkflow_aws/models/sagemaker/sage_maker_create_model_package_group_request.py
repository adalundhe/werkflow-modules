from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_managed_configuration import SageMakerManagedConfiguration
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateModelPackageGroupRequest(BaseModel):
    ModelPackageGroupName: StrictStr
    ModelPackageGroupDescription: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    ManagedConfiguration: SageMakerManagedConfiguration | None = None
