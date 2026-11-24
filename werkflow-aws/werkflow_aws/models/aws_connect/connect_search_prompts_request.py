from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_prompt_search_criteria import ConnectPromptSearchCriteria
from .connect_prompt_search_filter import ConnectPromptSearchFilter


class ConnectSearchPromptsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectPromptSearchFilter | None = None
    SearchCriteria: ConnectPromptSearchCriteria | None = None
