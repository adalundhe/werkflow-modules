from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationAndroidApp(BaseModel):
    Package: StrictStr | None = None
    CertificateFingerprint: StrictStr | None = None
