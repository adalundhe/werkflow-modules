from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .open_search_package_configuration import OpenSearchPackageConfiguration
from .open_search_plugin_properties import OpenSearchPluginProperties


class OpenSearchPackageVersionHistory(BaseModel):
    PackageVersion: StrictStr | None = None
    CommitMessage: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    PluginProperties: OpenSearchPluginProperties | None = None
    PackageConfiguration: OpenSearchPackageConfiguration | None = None
