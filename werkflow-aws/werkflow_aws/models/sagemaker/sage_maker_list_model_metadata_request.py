from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_metadata_search_expression import SageMakerModelMetadataSearchExpression


class SageMakerListModelMetadataRequest(BaseModel):
    SearchExpression: SageMakerModelMetadataSearchExpression | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
