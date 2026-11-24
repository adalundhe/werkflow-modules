from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_layers_list_item import LambdaLayersListItem


class LambdaListLayersResponse(BaseModel):
    NextMarker: StrictStr | None = None
    Layers: list[LambdaLayersListItem] | None = None
