from __future__ import annotations
from pydantic import BaseModel
from .awss3_record_expiration import AWSS3RecordExpiration


class AWSS3JournalTableConfigurationUpdates(BaseModel):
    RecordExpiration: AWSS3RecordExpiration
