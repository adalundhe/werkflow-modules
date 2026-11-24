from __future__ import annotations
from pydantic import BaseModel
from .awss3_tag import AWSS3Tag


class AWSS3Tagging(BaseModel):
    TagSet: list[AWSS3Tag]
