from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_tag_model import AWSS3TagModel


class AWSS3IntelligentTieringAndOperator(BaseModel):
    Prefix: StrictStr | None = None
    Tags: list[AWSS3TagModel] | None = None
