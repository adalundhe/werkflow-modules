from __future__ import annotations
from pydantic import BaseModel
from .kendra_seed_url_configuration import KendraSeedUrlConfiguration
from .kendra_site_maps_configuration import KendraSiteMapsConfiguration


class KendraUrls(BaseModel):
    SeedUrlConfiguration: KendraSeedUrlConfiguration | None = None
    SiteMapsConfiguration: KendraSiteMapsConfiguration | None = None
