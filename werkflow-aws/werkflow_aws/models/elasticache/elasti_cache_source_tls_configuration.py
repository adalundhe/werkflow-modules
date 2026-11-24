from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ElastiCacheSourceTlsConfiguration(BaseModel):
    SourceTlsMode: Literal['none', 'verify-ca'] | None = None
    SourceTlsCertificate: StrictStr | None = None
