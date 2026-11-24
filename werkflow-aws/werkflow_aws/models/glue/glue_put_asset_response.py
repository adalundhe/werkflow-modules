from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_asset_form_entry import GlueAssetFormEntry


class GluePutAssetResponse(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    AssetTypeId: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Forms: dict[StrictStr, GlueAssetFormEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
