from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CustomColors(BaseModel):
    AccentColor: StrictStr | None = None
    BackgroundColor: StrictStr | None = None
    ErrorValidationColor: StrictStr | None = None
    HeaderColor: StrictStr | None = None
    NavigationColor: StrictStr | None = None
    TextColor: StrictStr | None = None
