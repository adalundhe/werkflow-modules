from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_asset_type_item import GlueAssetTypeItem


class GlueListAssetTypesResponse(BaseModel):
    Items: list[GlueAssetTypeItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
