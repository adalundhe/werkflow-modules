from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_dev_endpoint_custom_libraries import GlueDevEndpointCustomLibraries


class GlueUpdateDevEndpointRequest(BaseModel):
    EndpointName: StrictStr
    PublicKey: StrictStr | None = None
    AddPublicKeys: list[StrictStr] | None = None
    DeletePublicKeys: list[StrictStr] | None = None
    CustomLibraries: GlueDevEndpointCustomLibraries | None = None
    UpdateEtlLibraries: StrictBool | None = None
    DeleteArguments: list[StrictStr] | None = None
    AddArguments: dict[StrictStr, StrictStr] | None = None
