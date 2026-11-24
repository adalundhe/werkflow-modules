from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_card_security_config import SageMakerModelCardSecurityConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerModelCard(BaseModel):
    ModelCardArn: StrictStr | None = None
    ModelCardName: StrictStr | None = None
    ModelCardVersion: StrictInt | None = None
    Content: StrictStr | None = None
    ModelCardStatus: StrictStr | None = None
    SecurityConfig: SageMakerModelCardSecurityConfig | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    Tags: list[SageMakerTagModel] | None = None
    ModelId: StrictStr | None = None
    RiskRating: StrictStr | None = None
    ModelPackageGroupName: StrictStr | None = None
