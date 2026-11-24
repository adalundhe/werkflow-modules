from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightWebCrawlerParameters(BaseModel):
    WebCrawlerAuthType: StrictStr | None = None
    UsernameFieldXpath: StrictStr | None = None
    PasswordFieldXpath: StrictStr | None = None
    UsernameButtonXpath: StrictStr | None = None
    PasswordButtonXpath: StrictStr | None = None
    LoginPageUrl: StrictStr | None = None
    WebProxyHostName: StrictStr | None = None
    WebProxyPortNumber: StrictInt | None = None
