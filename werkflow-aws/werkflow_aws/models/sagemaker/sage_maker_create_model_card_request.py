from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_model_card_security_config import SageMakerModelCardSecurityConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateModelCardRequest(BaseModel):
    ModelCardName: StrictStr
    Content: StrictStr
    ModelCardStatus: Literal['Draft', 'PendingReview', 'Approved', 'Archived']
    SecurityConfig: SageMakerModelCardSecurityConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
