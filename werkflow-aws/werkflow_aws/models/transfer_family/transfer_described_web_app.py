from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_described_web_app_endpoint_details import TransferDescribedWebAppEndpointDetails
from .transfer_described_web_app_identity_provider_details import TransferDescribedWebAppIdentityProviderDetails
from .transfer_tag import TransferTag
from .transfer_web_app_units import TransferWebAppUnits


class TransferDescribedWebApp(BaseModel):
    Arn: StrictStr | None = None
    WebAppId: StrictStr | None = None
    DescribedIdentityProviderDetails: TransferDescribedWebAppIdentityProviderDetails | None = None
    AccessEndpoint: StrictStr | None = None
    WebAppEndpoint: StrictStr | None = None
    WebAppUnits: TransferWebAppUnits | None = None
    Tags: list[TransferTag] | None = None
    WebAppEndpointPolicy: StrictStr | None = None
    EndpointType: StrictStr | None = None
    DescribedEndpointDetails: TransferDescribedWebAppEndpointDetails | None = None
