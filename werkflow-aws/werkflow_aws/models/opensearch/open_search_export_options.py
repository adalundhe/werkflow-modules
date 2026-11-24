from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_saved_object_identifier import OpenSearchSavedObjectIdentifier


class OpenSearchExportOptions(BaseModel):
    types: list[StrictStr] | None = None
    objects: list[OpenSearchSavedObjectIdentifier] | None = None
    includeReferencesDeep: StrictBool | None = None
