from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_asset_type_form_output import GlueAssetTypeFormOutput


class GlueGetAssetTypeResponse(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Forms: dict[StrictStr, GlueAssetTypeFormOutput] | None = None
    ResponseMetadata: dict[str, Any] | None = None
