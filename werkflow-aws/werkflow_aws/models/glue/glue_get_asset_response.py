from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_asset_form_entry import GlueAssetFormEntry
from .glue_iterable_form_entry import GlueIterableFormEntry


class GlueGetAssetResponse(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    AssetTypeId: StrictStr | None = None
    GlossaryTerms: list[StrictStr] | None = None
    Forms: dict[StrictStr, GlueAssetFormEntry] | None = None
    Attachments: dict[StrictStr, GlueAssetFormEntry] | None = None
    IterableForms: dict[StrictStr, GlueIterableFormEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
