from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerModelPackageGroup(BaseModel):
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageGroupArn: StrictStr | None = None
    ModelPackageGroupDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    ModelPackageGroupStatus: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
