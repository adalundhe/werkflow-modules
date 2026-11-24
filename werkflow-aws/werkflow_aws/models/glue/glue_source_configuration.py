from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_connector_property import GlueConnectorProperty
from .glue_filter_configuration import GlueFilterConfiguration
from .glue_pagination_configuration import GluePaginationConfiguration
from .glue_response_configuration import GlueResponseConfiguration


class GlueSourceConfiguration(BaseModel):
    RequestMethod: StrictStr | None = None
    RequestPath: StrictStr | None = None
    RequestParameters: list[GlueConnectorProperty] | None = None
    ResponseConfiguration: GlueResponseConfiguration | None = None
    PaginationConfiguration: GluePaginationConfiguration | None = None
    FilterConfiguration: GlueFilterConfiguration | None = None
