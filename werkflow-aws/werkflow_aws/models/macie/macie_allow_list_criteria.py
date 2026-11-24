from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_s3_words_list import MacieS3WordsList


class MacieAllowListCriteria(BaseModel):
    regex: StrictStr | None = None
    s3WordsList: MacieS3WordsList | None = None
