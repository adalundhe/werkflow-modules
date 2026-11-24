from werkflow_aws.models.simpledb import (
    SimpleDBBatchDeleteAttributesRequest,
    SimpleDBBatchDeleteAttributesResponse,
    SimpleDBBatchPutAttributesRequest,
    SimpleDBBatchPutAttributesResponse,
    SimpleDBCreateDomainRequest,
    SimpleDBCreateDomainResponse,
    SimpleDBDeleteAttributesRequest,
    SimpleDBDeleteAttributesResponse,
    SimpleDBDeleteDomainRequest,
    SimpleDBDeleteDomainResponse,
    SimpleDBDomainMetadataRequest,
    SimpleDBDomainMetadataResponse,
    SimpleDBGetAttributesRequest,
    SimpleDBGetAttributesResponse,
    SimpleDBListDomainsRequest,
    SimpleDBListDomainsResponse,
    SimpleDBPutAttributesRequest,
    SimpleDBPutAttributesResponse,
    SimpleDBSelectRequest,
    SimpleDBSelectResponse,
)
from werkflow_aws.types.simpledb_client import SimpleDBClient
from .base import AWSBaseService


class AWSSimpleDB(AWSBaseService[SimpleDBClient]):
    service_name = 'simpledb'
    boto3_service_name = 'sdb'

    def __init__(self) -> None:
        super().__init__(service_name='simpledb', boto3_service_name='sdb')

    async def batch_delete_attributes(
        self,
        request: SimpleDBBatchDeleteAttributesRequest,
    ) -> SimpleDBBatchDeleteAttributesResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_attributes, request, SimpleDBBatchDeleteAttributesResponse)

    async def batch_put_attributes(
        self,
        request: SimpleDBBatchPutAttributesRequest,
    ) -> SimpleDBBatchPutAttributesResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_attributes, request, SimpleDBBatchPutAttributesResponse)

    async def create_domain(
        self,
        request: SimpleDBCreateDomainRequest,
    ) -> SimpleDBCreateDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_domain, request, SimpleDBCreateDomainResponse)

    async def delete_attributes(
        self,
        request: SimpleDBDeleteAttributesRequest,
    ) -> SimpleDBDeleteAttributesResponse:
        client = self._require_client()
        return await self._execute(client.delete_attributes, request, SimpleDBDeleteAttributesResponse)

    async def delete_domain(
        self,
        request: SimpleDBDeleteDomainRequest,
    ) -> SimpleDBDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, SimpleDBDeleteDomainResponse)

    async def domain_metadata(
        self,
        request: SimpleDBDomainMetadataRequest,
    ) -> SimpleDBDomainMetadataResponse:
        client = self._require_client()
        return await self._execute(client.domain_metadata, request, SimpleDBDomainMetadataResponse)

    async def get_attributes(
        self,
        request: SimpleDBGetAttributesRequest,
    ) -> SimpleDBGetAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_attributes, request, SimpleDBGetAttributesResponse)

    async def list_domains(
        self,
        request: SimpleDBListDomainsRequest | None = None,
    ) -> SimpleDBListDomainsResponse:
        client = self._require_client()
        return await self._execute(client.list_domains, request, SimpleDBListDomainsResponse)

    async def list_domains_paginated(
        self,
        request: SimpleDBListDomainsRequest | None = None,
    ) -> list[SimpleDBListDomainsResponse]:
        return await self._paginate('list_domains', request, SimpleDBListDomainsResponse)

    async def put_attributes(
        self,
        request: SimpleDBPutAttributesRequest,
    ) -> SimpleDBPutAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_attributes, request, SimpleDBPutAttributesResponse)

    async def select(
        self,
        request: SimpleDBSelectRequest,
    ) -> SimpleDBSelectResponse:
        client = self._require_client()
        return await self._execute(client.select, request, SimpleDBSelectResponse)

    async def select_paginated(
        self,
        request: SimpleDBSelectRequest,
    ) -> list[SimpleDBSelectResponse]:
        return await self._paginate('select', request, SimpleDBSelectResponse)
