from __future__ import annotations
from pydantic import BaseModel
from .security_lake_data_lake_lifecycle_expiration import SecurityLakeDataLakeLifecycleExpiration
from .security_lake_data_lake_lifecycle_transition import SecurityLakeDataLakeLifecycleTransition


class SecurityLakeDataLakeLifecycleConfiguration(BaseModel):
    expiration: SecurityLakeDataLakeLifecycleExpiration | None = None
    transitions: list[SecurityLakeDataLakeLifecycleTransition] | None = None
