from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .kendra_document_attribute import KendraDocumentAttribute
from .kendra_hierarchical_principal import KendraHierarchicalPrincipal
from .kendra_principal import KendraPrincipal
from .kendra_s3_path import KendraS3Path


class KendraDocument(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Id: StrictStr
    Title: StrictStr | None = None
    Blob: StrictBytes | BinaryIO | StrictStr | None = None
    S3Path: KendraS3Path | None = None
    Attributes: list[KendraDocumentAttribute] | None = None
    AccessControlList: list[KendraPrincipal] | None = None
    HierarchicalAccessControlList: list[KendraHierarchicalPrincipal] | None = None
    ContentType: Literal['PDF', 'HTML', 'MS_WORD', 'PLAIN_TEXT', 'PPT', 'RTF', 'XML', 'XSLT', 'MS_EXCEL', 'CSV', 'JSON', 'MD'] | None = None
    AccessControlConfigurationId: StrictStr | None = None
