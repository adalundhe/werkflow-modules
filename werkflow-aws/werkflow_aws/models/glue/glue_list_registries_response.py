from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_registry_list_item import GlueRegistryListItem


class GlueListRegistriesResponse(BaseModel):
    Registries: list[GlueRegistryListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
