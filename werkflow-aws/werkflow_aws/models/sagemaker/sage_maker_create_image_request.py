from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateImageRequest(BaseModel):
    ImageName: StrictStr
    RoleArn: StrictStr
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
