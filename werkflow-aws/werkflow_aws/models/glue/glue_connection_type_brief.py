from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_capabilities import GlueCapabilities
from .glue_connection_type_variant import GlueConnectionTypeVariant


class GlueConnectionTypeBrief(BaseModel):
    ConnectionType: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Vendor: StrictStr | None = None
    Description: StrictStr | None = None
    Categories: list[StrictStr] | None = None
    Capabilities: GlueCapabilities | None = None
    LogoUrl: StrictStr | None = None
    ConnectionTypeVariants: list[GlueConnectionTypeVariant] | None = None
