from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_contact_lens_channel_configuration import ConnectContactLensChannelConfiguration
from .connect_contact_lens_redaction_configuration import ConnectContactLensRedactionConfiguration
from .connect_contact_lens_sentiment_configuration import ConnectContactLensSentimentConfiguration
from .connect_contact_lens_summary_configuration import ConnectContactLensSummaryConfiguration


class ConnectConversationalAnalyticsConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    LanguageLocale: StrictStr | None = None
    LanguageLocales: list[StrictStr] | None = None
    ChannelConfiguration: ConnectContactLensChannelConfiguration | None = None
    RedactionConfiguration: ConnectContactLensRedactionConfiguration | None = None
    SummaryConfiguration: ConnectContactLensSummaryConfiguration | None = None
    SentimentConfiguration: ConnectContactLensSentimentConfiguration | None = None
