from __future__ import annotations
from pydantic import BaseModel
from .awss3_filter_rule import AWSS3FilterRule


class AWSS3S3KeyFilter(BaseModel):
    FilterRules: list[AWSS3FilterRule] | None = None
