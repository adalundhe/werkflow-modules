from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListRulesRequest(BaseModel):
    InstanceId: StrictStr
    PublishStatus: Literal['DRAFT', 'PUBLISHED'] | None = None
    EventSourceName: Literal['OnPostCallAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnAfterCallWorkAvailable', 'OnAfterChatWorkAvailable', 'OnEmailAnalysisAvailable', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate', 'OnSalesforceCaseCreate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnCaseCreate', 'OnCaseUpdate', 'OnSlaBreach', 'OnAlertUpdate', 'OnSchedulePublish', 'OnScheduleUpdate', 'OnScheduleTimeOffRequestActivity'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
