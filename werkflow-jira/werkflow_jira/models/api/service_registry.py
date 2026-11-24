from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_registry_tier import ServiceRegistryTier


class ServiceRegistry(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    organizationId: StrictStr | None = None
    revision: StrictStr | None = None
    serviceTier: ServiceRegistryTier | None = None
