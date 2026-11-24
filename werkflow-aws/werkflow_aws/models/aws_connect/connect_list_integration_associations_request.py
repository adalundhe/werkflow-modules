from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListIntegrationAssociationsRequest(BaseModel):
    InstanceId: StrictStr
    IntegrationType: Literal['EVENT', 'VOICE_ID', 'PINPOINT_APP', 'WISDOM_ASSISTANT', 'WISDOM_KNOWLEDGE_BASE', 'WISDOM_QUICK_RESPONSES', 'Q_MESSAGE_TEMPLATES', 'CASES_DOMAIN', 'APPLICATION', 'FILE_SCANNER', 'SES_IDENTITY', 'ANALYTICS_CONNECTOR', 'CALL_TRANSFER_CONNECTOR', 'COGNITO_USER_POOL', 'MESSAGE_PROCESSOR'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    IntegrationArn: StrictStr | None = None
