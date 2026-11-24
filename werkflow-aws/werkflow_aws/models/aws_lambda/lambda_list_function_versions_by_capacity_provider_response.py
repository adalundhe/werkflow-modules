from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_function_versions_by_capacity_provider_list_item import LambdaFunctionVersionsByCapacityProviderListItem


class LambdaListFunctionVersionsByCapacityProviderResponse(BaseModel):
    CapacityProviderArn: StrictStr | None = None
    FunctionVersions: list[LambdaFunctionVersionsByCapacityProviderListItem] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
