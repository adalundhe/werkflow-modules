from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_layer_versions_list_item import LambdaLayerVersionsListItem


class LambdaLayersListItem(BaseModel):
    LayerName: StrictStr | None = None
    LayerArn: StrictStr | None = None
    LatestMatchingVersion: LambdaLayerVersionsListItem | None = None
