from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_update_web_app_endpoint_details import TransferUpdateWebAppEndpointDetails
from .transfer_update_web_app_identity_provider_details import TransferUpdateWebAppIdentityProviderDetails
from .transfer_web_app_units import TransferWebAppUnits


class TransferUpdateWebAppRequest(BaseModel):
    WebAppId: StrictStr
    IdentityProviderDetails: TransferUpdateWebAppIdentityProviderDetails | None = None
    AccessEndpoint: StrictStr | None = None
    WebAppUnits: TransferWebAppUnits | None = None
    EndpointDetails: TransferUpdateWebAppEndpointDetails | None = None
