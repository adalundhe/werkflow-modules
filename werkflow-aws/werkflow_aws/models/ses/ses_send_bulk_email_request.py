from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_bulk_email_content import SESBulkEmailContent
from .ses_bulk_email_entry import SESBulkEmailEntry
from .ses_configuration_overrides import SESConfigurationOverrides
from .ses_message_tag import SESMessageTag


class SESSendBulkEmailRequest(BaseModel):
    DefaultContent: SESBulkEmailContent
    BulkEmailEntries: list[SESBulkEmailEntry]
    FromEmailAddress: StrictStr | None = None
    FromEmailAddressIdentityArn: StrictStr | None = None
    ReplyToAddresses: list[StrictStr] | None = None
    FeedbackForwardingEmailAddress: StrictStr | None = None
    FeedbackForwardingEmailAddressIdentityArn: StrictStr | None = None
    DefaultEmailTags: list[SESMessageTag] | None = None
    ConfigurationSetName: StrictStr | None = None
    EndpointId: StrictStr | None = None
    TenantName: StrictStr | None = None
    ConfigurationOverrides: SESConfigurationOverrides | None = None
