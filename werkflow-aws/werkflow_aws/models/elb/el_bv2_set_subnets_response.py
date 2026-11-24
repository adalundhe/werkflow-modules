from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_availability_zone import ELBv2AvailabilityZone


class ELBv2SetSubnetsResponse(BaseModel):
    AvailabilityZones: list[ELBv2AvailabilityZone] | None = None
    IpAddressType: StrictStr | None = None
    EnablePrefixForIpv6SourceNat: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
