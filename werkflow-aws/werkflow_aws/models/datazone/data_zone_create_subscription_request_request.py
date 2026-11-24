from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_accepted_asset_scope import DataZoneAcceptedAssetScope
from .data_zone_asset_permission import DataZoneAssetPermission
from .data_zone_form_input import DataZoneFormInput
from .data_zone_subscribed_listing_input import DataZoneSubscribedListingInput
from .data_zone_subscribed_principal_input import DataZoneSubscribedPrincipalInput


class DataZoneCreateSubscriptionRequestRequest(BaseModel):
    domainIdentifier: StrictStr
    subscribedPrincipals: list[DataZoneSubscribedPrincipalInput]
    subscribedListings: list[DataZoneSubscribedListingInput]
    requestReason: StrictStr
    clientToken: StrictStr | None = None
    metadataForms: list[DataZoneFormInput] | None = None
    assetPermissions: list[DataZoneAssetPermission] | None = None
    assetScopes: list[DataZoneAcceptedAssetScope] | None = None
