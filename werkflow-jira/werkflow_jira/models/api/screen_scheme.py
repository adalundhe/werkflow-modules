from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
from .screen_types import ScreenTypes


class ScreenScheme(BaseModel):
    description: StrictStr | None = None
    id: StrictInt | None = None
    issueTypeScreenSchemes: PageBeanIssueTypeScreenScheme | None = None
    name: StrictStr | None = None
    screens: ScreenTypes | None = None
