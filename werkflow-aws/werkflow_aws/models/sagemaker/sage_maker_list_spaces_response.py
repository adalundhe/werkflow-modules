from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_space_details import SageMakerSpaceDetails


class SageMakerListSpacesResponse(BaseModel):
    Spaces: list[SageMakerSpaceDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
