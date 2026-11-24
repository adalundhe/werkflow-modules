from __future__ import annotations
from pydantic import BaseModel
from .elasti_cache_secret_manager_auth_config import ElastiCacheSecretManagerAuthConfig


class ElastiCacheSourceAuthenticationConfiguration(BaseModel):
    SecretManagerConfig: ElastiCacheSecretManagerAuthConfig | None = None
