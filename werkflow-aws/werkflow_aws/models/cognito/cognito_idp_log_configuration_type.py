from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_cloud_watch_logs_configuration_type import CognitoIDPCloudWatchLogsConfigurationType
from .cognito_idp_firehose_configuration_type import CognitoIDPFirehoseConfigurationType
from .cognito_idps3_configuration_type import CognitoIDPS3ConfigurationType


class CognitoIDPLogConfigurationType(BaseModel):
    LogLevel: StrictStr | None = None
    EventSource: StrictStr | None = None
    CloudWatchLogsConfiguration: CognitoIDPCloudWatchLogsConfigurationType | None = None
    S3Configuration: CognitoIDPS3ConfigurationType | None = None
    FirehoseConfiguration: CognitoIDPFirehoseConfigurationType | None = None
