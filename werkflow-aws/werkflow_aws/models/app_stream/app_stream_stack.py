from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_agent_access_config import AppStreamAgentAccessConfig
from .app_stream_application_settings_response import AppStreamApplicationSettingsResponse
from .app_stream_content_redirection import AppStreamContentRedirection
from .app_stream_stack_error import AppStreamStackError
from .app_stream_storage_connector import AppStreamStorageConnector
from .app_stream_streaming_experience_settings import AppStreamStreamingExperienceSettings
from .app_stream_user_setting import AppStreamUserSetting
from .app_stream_web_authn_redirection import AppStreamWebAuthnRedirection


class AppStreamStack(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    StorageConnectors: list[AppStreamStorageConnector] | None = None
    RedirectURL: StrictStr | None = None
    FeedbackURL: StrictStr | None = None
    StackErrors: list[AppStreamStackError] | None = None
    UserSettings: list[AppStreamUserSetting] | None = None
    ApplicationSettings: AppStreamApplicationSettingsResponse | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    EmbedHostDomains: list[StrictStr] | None = None
    StreamingExperienceSettings: AppStreamStreamingExperienceSettings | None = None
    ContentRedirection: AppStreamContentRedirection | None = None
    WebAuthnRedirection: AppStreamWebAuthnRedirection | None = None
    AgentAccessConfig: AppStreamAgentAccessConfig | None = None
    StorageConnectorAuthentication: StrictStr | None = None
