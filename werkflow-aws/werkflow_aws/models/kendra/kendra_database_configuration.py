from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_acl_configuration import KendraAclConfiguration
from .kendra_column_configuration import KendraColumnConfiguration
from .kendra_connection_configuration import KendraConnectionConfiguration
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration
from .kendra_sql_configuration import KendraSqlConfiguration


class KendraDatabaseConfiguration(BaseModel):
    DatabaseEngineType: StrictStr | None = None
    ConnectionConfiguration: KendraConnectionConfiguration | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    ColumnConfiguration: KendraColumnConfiguration | None = None
    AclConfiguration: KendraAclConfiguration | None = None
    SqlConfiguration: KendraSqlConfiguration | None = None
