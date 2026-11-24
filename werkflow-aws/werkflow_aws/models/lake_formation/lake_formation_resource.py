from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_any_resource import LakeFormationAnyResource
from .lake_formation_catalog_resource import LakeFormationCatalogResource
from .lake_formation_data_cells_filter_resource import LakeFormationDataCellsFilterResource
from .lake_formation_data_location_resource import LakeFormationDataLocationResource
from .lake_formation_database_resource import LakeFormationDatabaseResource
from .lake_formation_lf_tag_expression_resource import LakeFormationLFTagExpressionResource
from .lake_formation_lf_tag_key_resource import LakeFormationLFTagKeyResource
from .lake_formation_lf_tag_policy_resource import LakeFormationLFTagPolicyResource
from .lake_formation_rls_policy_resource import LakeFormationRLSPolicyResource
from .lake_formation_table_resource import LakeFormationTableResource
from .lake_formation_table_with_columns_resource import LakeFormationTableWithColumnsResource
from .lake_formation_user_defined_function_resource import LakeFormationUserDefinedFunctionResource


class LakeFormationResource(BaseModel):
    AnyResource: LakeFormationAnyResource | None = None
    Catalog: LakeFormationCatalogResource | None = None
    Database: LakeFormationDatabaseResource | None = None
    Table: LakeFormationTableResource | None = None
    TableWithColumns: LakeFormationTableWithColumnsResource | None = None
    DataLocation: LakeFormationDataLocationResource | None = None
    DataCellsFilter: LakeFormationDataCellsFilterResource | None = None
    LFTag: LakeFormationLFTagKeyResource | None = None
    LFTagPolicy: LakeFormationLFTagPolicyResource | None = None
    LFTagExpression: LakeFormationLFTagExpressionResource | None = None
    RLSPolicy: LakeFormationRLSPolicyResource | None = None
    UserDefinedFunction: LakeFormationUserDefinedFunctionResource | None = None
