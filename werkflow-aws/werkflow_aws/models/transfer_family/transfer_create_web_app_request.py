from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_tag import TransferTag
from .transfer_web_app_endpoint_details import TransferWebAppEndpointDetails
from .transfer_web_app_identity_provider_details import TransferWebAppIdentityProviderDetails
from .transfer_web_app_units import TransferWebAppUnits


class TransferCreateWebAppRequest(BaseModel):
    IdentityProviderDetails: TransferWebAppIdentityProviderDetails
    AccessEndpoint: StrictStr | None = None
    WebAppUnits: TransferWebAppUnits | None = None
    Tags: list[TransferTag] | None = None
    WebAppEndpointPolicy: Literal['FIPS', 'STANDARD'] | None = None
    EndpointDetails: TransferWebAppEndpointDetails | None = None
