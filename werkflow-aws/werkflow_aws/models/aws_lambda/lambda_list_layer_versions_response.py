from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_layer_versions_list_item_model import LambdaLayerVersionsListItemModel


class LambdaListLayerVersionsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    LayerVersions: list[LambdaLayerVersionsListItemModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
