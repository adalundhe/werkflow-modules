from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_online_store_security_config import SageMakerOnlineStoreSecurityConfig
from .sage_maker_ttl_duration import SageMakerTtlDuration


class SageMakerOnlineStoreConfig(BaseModel):
    SecurityConfig: SageMakerOnlineStoreSecurityConfig | None = None
    EnableOnlineStore: StrictBool | None = None
    TtlDuration: SageMakerTtlDuration | None = None
    StorageType: StrictStr | None = None
