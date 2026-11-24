from __future__ import annotations
from pydantic import BaseModel
from .acm_common_name_filter import ACMCommonNameFilter


class ACMSubjectFilter(BaseModel):
    CommonName: ACMCommonNameFilter | None = None
