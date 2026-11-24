from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ecr_public_registry_alias import ECRPublicRegistryAlias


class ECRPublicRegistry(BaseModel):
    registryId: StrictStr | None = None
    registryArn: StrictStr | None = None
    registryUri: StrictStr | None = None
    verified: StrictBool | None = None
    aliases: list[ECRPublicRegistryAlias] | None = None
