from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_alias_list_entry import KMSAliasListEntry


class KMSListAliasesResponse(BaseModel):
    Aliases: list[KMSAliasListEntry] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
