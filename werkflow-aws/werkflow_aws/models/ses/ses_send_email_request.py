from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_configuration_overrides import SESConfigurationOverrides
from .ses_destination import SESDestination
from .ses_email_content import SESEmailContent
from .ses_list_management_options import SESListManagementOptions
from .ses_message_tag import SESMessageTag


class SESSendEmailRequest(BaseModel):
    Content: SESEmailContent
    FromEmailAddress: StrictStr | None = None
    FromEmailAddressIdentityArn: StrictStr | None = None
    Destination: SESDestination | None = None
    ReplyToAddresses: list[StrictStr] | None = None
    FeedbackForwardingEmailAddress: StrictStr | None = None
    FeedbackForwardingEmailAddressIdentityArn: StrictStr | None = None
    EmailTags: list[SESMessageTag] | None = None
    ConfigurationSetName: StrictStr | None = None
    EndpointId: StrictStr | None = None
    TenantName: StrictStr | None = None
    ListManagementOptions: SESListManagementOptions | None = None
    ConfigurationOverrides: SESConfigurationOverrides | None = None
