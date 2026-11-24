from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_intelligent_tiering_and_operator import AWSS3IntelligentTieringAndOperator
from .awss3_tag_model import AWSS3TagModel


class AWSS3IntelligentTieringFilter(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3TagModel | None = None
    And: AWSS3IntelligentTieringAndOperator | None = None
