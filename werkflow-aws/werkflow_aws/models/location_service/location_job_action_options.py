from __future__ import annotations
from pydantic import BaseModel
from .location_validate_address_action_options import LocationValidateAddressActionOptions


class LocationJobActionOptions(BaseModel):
    ValidateAddress: LocationValidateAddressActionOptions | None = None
