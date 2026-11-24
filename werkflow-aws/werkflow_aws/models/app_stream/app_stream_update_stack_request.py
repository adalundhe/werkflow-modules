from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_agent_access_config_for_update import AppStreamAgentAccessConfigForUpdate
from .app_stream_application_settings import AppStreamApplicationSettings
from .app_stream_content_redirection import AppStreamContentRedirection
from .app_stream_storage_connector import AppStreamStorageConnector
from .app_stream_streaming_experience_settings import AppStreamStreamingExperienceSettings
from .app_stream_user_setting import AppStreamUserSetting
from .app_stream_web_authn_redirection import AppStreamWebAuthnRedirection


class AppStreamUpdateStackRequest(BaseModel):
    Name: StrictStr
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    StorageConnectors: list[AppStreamStorageConnector] | None = None
    DeleteStorageConnectors: StrictBool | None = None
    RedirectURL: StrictStr | None = None
    FeedbackURL: StrictStr | None = None
    AttributesToDelete: list[Literal['STORAGE_CONNECTORS', 'STORAGE_CONNECTOR_HOMEFOLDERS', 'STORAGE_CONNECTOR_GOOGLE_DRIVE', 'STORAGE_CONNECTOR_ONE_DRIVE', 'REDIRECT_URL', 'FEEDBACK_URL', 'THEME_NAME', 'USER_SETTINGS', 'EMBED_HOST_DOMAINS', 'IAM_ROLE_ARN', 'ACCESS_ENDPOINTS', 'STREAMING_EXPERIENCE_SETTINGS', 'CONTENT_REDIRECTION', 'WEB_AUTHN_REDIRECTION', 'AGENT_ACCESS_CONFIG', 'STORAGE_CONNECTOR_AUTHENTICATION', 'AGENT_ACCESS_CONFIG_KMS_KEY_ARN']] | None = None
    UserSettings: list[AppStreamUserSetting] | None = None
    ApplicationSettings: AppStreamApplicationSettings | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    EmbedHostDomains: list[StrictStr] | None = None
    StreamingExperienceSettings: AppStreamStreamingExperienceSettings | None = None
    ContentRedirection: AppStreamContentRedirection | None = None
    WebAuthnRedirection: AppStreamWebAuthnRedirection | None = None
    AgentAccessConfig: AppStreamAgentAccessConfigForUpdate | None = None
    StorageConnectorAuthentication: Literal['FORCE_REAUTHENTICATION', 'REUSE_CREDENTIALS'] | None = None
