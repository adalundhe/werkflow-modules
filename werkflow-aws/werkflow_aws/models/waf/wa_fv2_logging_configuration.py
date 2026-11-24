from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .wa_fv2_field_to_match import WAFv2FieldToMatch
from .wa_fv2_logging_filter import WAFv2LoggingFilter


class WAFv2LoggingConfiguration(BaseModel):
    ResourceArn: StrictStr | None = None
    LogDestinationConfigs: list[StrictStr] | None = None
    RedactedFields: list[WAFv2FieldToMatch] | None = None
    ManagedByFirewallManager: StrictBool | None = None
    LoggingFilter: WAFv2LoggingFilter | None = None
    LogType: StrictStr | None = None
    LogScope: StrictStr | None = None
