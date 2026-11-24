from werkflow_aws.models.location_service import (
    LocationAssociateTrackerConsumerRequest,
    LocationAssociateTrackerConsumerResponse,
    LocationBatchDeleteDevicePositionHistoryRequest,
    LocationBatchDeleteDevicePositionHistoryResponse,
    LocationBatchDeleteGeofenceRequest,
    LocationBatchDeleteGeofenceResponse,
    LocationBatchEvaluateGeofencesRequest,
    LocationBatchEvaluateGeofencesResponse,
    LocationBatchGetDevicePositionRequest,
    LocationBatchGetDevicePositionResponse,
    LocationBatchPutGeofenceRequest,
    LocationBatchPutGeofenceResponse,
    LocationBatchUpdateDevicePositionRequest,
    LocationBatchUpdateDevicePositionResponse,
    LocationCalculateRouteMatrixRequest,
    LocationCalculateRouteMatrixResponse,
    LocationCalculateRouteRequest,
    LocationCalculateRouteResponse,
    LocationCancelJobRequest,
    LocationCancelJobResponse,
    LocationCreateGeofenceCollectionRequest,
    LocationCreateGeofenceCollectionResponse,
    LocationCreateKeyRequest,
    LocationCreateKeyResponse,
    LocationCreateMapRequest,
    LocationCreateMapResponse,
    LocationCreatePlaceIndexRequest,
    LocationCreatePlaceIndexResponse,
    LocationCreateRouteCalculatorRequest,
    LocationCreateRouteCalculatorResponse,
    LocationCreateTrackerRequest,
    LocationCreateTrackerResponse,
    LocationDeleteGeofenceCollectionRequest,
    LocationDeleteGeofenceCollectionResponse,
    LocationDeleteKeyRequest,
    LocationDeleteKeyResponse,
    LocationDeleteMapRequest,
    LocationDeleteMapResponse,
    LocationDeletePlaceIndexRequest,
    LocationDeletePlaceIndexResponse,
    LocationDeleteRouteCalculatorRequest,
    LocationDeleteRouteCalculatorResponse,
    LocationDeleteTrackerRequest,
    LocationDeleteTrackerResponse,
    LocationDescribeGeofenceCollectionRequest,
    LocationDescribeGeofenceCollectionResponse,
    LocationDescribeKeyRequest,
    LocationDescribeKeyResponse,
    LocationDescribeMapRequest,
    LocationDescribeMapResponse,
    LocationDescribePlaceIndexRequest,
    LocationDescribePlaceIndexResponse,
    LocationDescribeRouteCalculatorRequest,
    LocationDescribeRouteCalculatorResponse,
    LocationDescribeTrackerRequest,
    LocationDescribeTrackerResponse,
    LocationDisassociateTrackerConsumerRequest,
    LocationDisassociateTrackerConsumerResponse,
    LocationForecastGeofenceEventsRequest,
    LocationForecastGeofenceEventsResponse,
    LocationGetDevicePositionHistoryRequest,
    LocationGetDevicePositionHistoryResponse,
    LocationGetDevicePositionRequest,
    LocationGetDevicePositionResponse,
    LocationGetGeofenceRequest,
    LocationGetGeofenceResponse,
    LocationGetJobRequest,
    LocationGetJobResponse,
    LocationGetMapGlyphsRequest,
    LocationGetMapGlyphsResponse,
    LocationGetMapSpritesRequest,
    LocationGetMapSpritesResponse,
    LocationGetMapStyleDescriptorRequest,
    LocationGetMapStyleDescriptorResponse,
    LocationGetMapTileRequest,
    LocationGetMapTileResponse,
    LocationGetPlaceRequest,
    LocationGetPlaceResponse,
    LocationListDevicePositionsRequest,
    LocationListDevicePositionsResponse,
    LocationListGeofenceCollectionsRequest,
    LocationListGeofenceCollectionsResponse,
    LocationListGeofencesRequest,
    LocationListGeofencesResponse,
    LocationListJobsRequest,
    LocationListJobsResponse,
    LocationListKeysRequest,
    LocationListKeysResponse,
    LocationListMapsRequest,
    LocationListMapsResponse,
    LocationListPlaceIndexesRequest,
    LocationListPlaceIndexesResponse,
    LocationListRouteCalculatorsRequest,
    LocationListRouteCalculatorsResponse,
    LocationListTagsForResourceRequest,
    LocationListTagsForResourceResponse,
    LocationListTrackerConsumersRequest,
    LocationListTrackerConsumersResponse,
    LocationListTrackersRequest,
    LocationListTrackersResponse,
    LocationPutGeofenceRequest,
    LocationPutGeofenceResponse,
    LocationSearchPlaceIndexForPositionRequest,
    LocationSearchPlaceIndexForPositionResponse,
    LocationSearchPlaceIndexForSuggestionsRequest,
    LocationSearchPlaceIndexForSuggestionsResponse,
    LocationSearchPlaceIndexForTextRequest,
    LocationSearchPlaceIndexForTextResponse,
    LocationStartJobRequest,
    LocationStartJobResponse,
    LocationTagResourceRequest,
    LocationTagResourceResponse,
    LocationUntagResourceRequest,
    LocationUntagResourceResponse,
    LocationUpdateGeofenceCollectionRequest,
    LocationUpdateGeofenceCollectionResponse,
    LocationUpdateKeyRequest,
    LocationUpdateKeyResponse,
    LocationUpdateMapRequest,
    LocationUpdateMapResponse,
    LocationUpdatePlaceIndexRequest,
    LocationUpdatePlaceIndexResponse,
    LocationUpdateRouteCalculatorRequest,
    LocationUpdateRouteCalculatorResponse,
    LocationUpdateTrackerRequest,
    LocationUpdateTrackerResponse,
    LocationVerifyDevicePositionRequest,
    LocationVerifyDevicePositionResponse,
)
from werkflow_aws.types.location_service_client import LocationClient
from .base import AWSBaseService


class AWSLocation(AWSBaseService[LocationClient]):
    service_name = 'location-service'
    boto3_service_name = 'location'

    def __init__(self) -> None:
        super().__init__(service_name='location-service', boto3_service_name='location')

    async def associate_tracker_consumer(
        self,
        request: LocationAssociateTrackerConsumerRequest,
    ) -> LocationAssociateTrackerConsumerResponse:
        client = self._require_client()
        return await self._execute(client.associate_tracker_consumer, request, LocationAssociateTrackerConsumerResponse)

    async def batch_delete_device_position_history(
        self,
        request: LocationBatchDeleteDevicePositionHistoryRequest,
    ) -> LocationBatchDeleteDevicePositionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_device_position_history, request, LocationBatchDeleteDevicePositionHistoryResponse)

    async def batch_delete_geofence(
        self,
        request: LocationBatchDeleteGeofenceRequest,
    ) -> LocationBatchDeleteGeofenceResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_geofence, request, LocationBatchDeleteGeofenceResponse)

    async def batch_evaluate_geofences(
        self,
        request: LocationBatchEvaluateGeofencesRequest,
    ) -> LocationBatchEvaluateGeofencesResponse:
        client = self._require_client()
        return await self._execute(client.batch_evaluate_geofences, request, LocationBatchEvaluateGeofencesResponse)

    async def batch_get_device_position(
        self,
        request: LocationBatchGetDevicePositionRequest,
    ) -> LocationBatchGetDevicePositionResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_device_position, request, LocationBatchGetDevicePositionResponse)

    async def batch_put_geofence(
        self,
        request: LocationBatchPutGeofenceRequest,
    ) -> LocationBatchPutGeofenceResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_geofence, request, LocationBatchPutGeofenceResponse)

    async def batch_update_device_position(
        self,
        request: LocationBatchUpdateDevicePositionRequest,
    ) -> LocationBatchUpdateDevicePositionResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_device_position, request, LocationBatchUpdateDevicePositionResponse)

    async def calculate_route(
        self,
        request: LocationCalculateRouteRequest,
    ) -> LocationCalculateRouteResponse:
        client = self._require_client()
        return await self._execute(client.calculate_route, request, LocationCalculateRouteResponse)

    async def calculate_route_matrix(
        self,
        request: LocationCalculateRouteMatrixRequest,
    ) -> LocationCalculateRouteMatrixResponse:
        client = self._require_client()
        return await self._execute(client.calculate_route_matrix, request, LocationCalculateRouteMatrixResponse)

    async def cancel_job(
        self,
        request: LocationCancelJobRequest,
    ) -> LocationCancelJobResponse:
        client = self._require_client()
        return await self._execute(client.cancel_job, request, LocationCancelJobResponse)

    async def create_geofence_collection(
        self,
        request: LocationCreateGeofenceCollectionRequest,
    ) -> LocationCreateGeofenceCollectionResponse:
        client = self._require_client()
        return await self._execute(client.create_geofence_collection, request, LocationCreateGeofenceCollectionResponse)

    async def create_key(
        self,
        request: LocationCreateKeyRequest,
    ) -> LocationCreateKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_key, request, LocationCreateKeyResponse)

    async def create_map(
        self,
        request: LocationCreateMapRequest,
    ) -> LocationCreateMapResponse:
        client = self._require_client()
        return await self._execute(client.create_map, request, LocationCreateMapResponse)

    async def create_place_index(
        self,
        request: LocationCreatePlaceIndexRequest,
    ) -> LocationCreatePlaceIndexResponse:
        client = self._require_client()
        return await self._execute(client.create_place_index, request, LocationCreatePlaceIndexResponse)

    async def create_route_calculator(
        self,
        request: LocationCreateRouteCalculatorRequest,
    ) -> LocationCreateRouteCalculatorResponse:
        client = self._require_client()
        return await self._execute(client.create_route_calculator, request, LocationCreateRouteCalculatorResponse)

    async def create_tracker(
        self,
        request: LocationCreateTrackerRequest,
    ) -> LocationCreateTrackerResponse:
        client = self._require_client()
        return await self._execute(client.create_tracker, request, LocationCreateTrackerResponse)

    async def delete_geofence_collection(
        self,
        request: LocationDeleteGeofenceCollectionRequest,
    ) -> LocationDeleteGeofenceCollectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_geofence_collection, request, LocationDeleteGeofenceCollectionResponse)

    async def delete_key(
        self,
        request: LocationDeleteKeyRequest,
    ) -> LocationDeleteKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_key, request, LocationDeleteKeyResponse)

    async def delete_map(
        self,
        request: LocationDeleteMapRequest,
    ) -> LocationDeleteMapResponse:
        client = self._require_client()
        return await self._execute(client.delete_map, request, LocationDeleteMapResponse)

    async def delete_place_index(
        self,
        request: LocationDeletePlaceIndexRequest,
    ) -> LocationDeletePlaceIndexResponse:
        client = self._require_client()
        return await self._execute(client.delete_place_index, request, LocationDeletePlaceIndexResponse)

    async def delete_route_calculator(
        self,
        request: LocationDeleteRouteCalculatorRequest,
    ) -> LocationDeleteRouteCalculatorResponse:
        client = self._require_client()
        return await self._execute(client.delete_route_calculator, request, LocationDeleteRouteCalculatorResponse)

    async def delete_tracker(
        self,
        request: LocationDeleteTrackerRequest,
    ) -> LocationDeleteTrackerResponse:
        client = self._require_client()
        return await self._execute(client.delete_tracker, request, LocationDeleteTrackerResponse)

    async def describe_geofence_collection(
        self,
        request: LocationDescribeGeofenceCollectionRequest,
    ) -> LocationDescribeGeofenceCollectionResponse:
        client = self._require_client()
        return await self._execute(client.describe_geofence_collection, request, LocationDescribeGeofenceCollectionResponse)

    async def describe_key(
        self,
        request: LocationDescribeKeyRequest,
    ) -> LocationDescribeKeyResponse:
        client = self._require_client()
        return await self._execute(client.describe_key, request, LocationDescribeKeyResponse)

    async def describe_map(
        self,
        request: LocationDescribeMapRequest,
    ) -> LocationDescribeMapResponse:
        client = self._require_client()
        return await self._execute(client.describe_map, request, LocationDescribeMapResponse)

    async def describe_place_index(
        self,
        request: LocationDescribePlaceIndexRequest,
    ) -> LocationDescribePlaceIndexResponse:
        client = self._require_client()
        return await self._execute(client.describe_place_index, request, LocationDescribePlaceIndexResponse)

    async def describe_route_calculator(
        self,
        request: LocationDescribeRouteCalculatorRequest,
    ) -> LocationDescribeRouteCalculatorResponse:
        client = self._require_client()
        return await self._execute(client.describe_route_calculator, request, LocationDescribeRouteCalculatorResponse)

    async def describe_tracker(
        self,
        request: LocationDescribeTrackerRequest,
    ) -> LocationDescribeTrackerResponse:
        client = self._require_client()
        return await self._execute(client.describe_tracker, request, LocationDescribeTrackerResponse)

    async def disassociate_tracker_consumer(
        self,
        request: LocationDisassociateTrackerConsumerRequest,
    ) -> LocationDisassociateTrackerConsumerResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_tracker_consumer, request, LocationDisassociateTrackerConsumerResponse)

    async def forecast_geofence_events(
        self,
        request: LocationForecastGeofenceEventsRequest,
    ) -> LocationForecastGeofenceEventsResponse:
        client = self._require_client()
        return await self._execute(client.forecast_geofence_events, request, LocationForecastGeofenceEventsResponse)

    async def forecast_geofence_events_paginated(
        self,
        request: LocationForecastGeofenceEventsRequest,
    ) -> list[LocationForecastGeofenceEventsResponse]:
        return await self._paginate('forecast_geofence_events', request, LocationForecastGeofenceEventsResponse)

    async def get_device_position(
        self,
        request: LocationGetDevicePositionRequest,
    ) -> LocationGetDevicePositionResponse:
        client = self._require_client()
        return await self._execute(client.get_device_position, request, LocationGetDevicePositionResponse)

    async def get_device_position_history(
        self,
        request: LocationGetDevicePositionHistoryRequest,
    ) -> LocationGetDevicePositionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_device_position_history, request, LocationGetDevicePositionHistoryResponse)

    async def get_device_position_history_paginated(
        self,
        request: LocationGetDevicePositionHistoryRequest,
    ) -> list[LocationGetDevicePositionHistoryResponse]:
        return await self._paginate('get_device_position_history', request, LocationGetDevicePositionHistoryResponse)

    async def get_geofence(
        self,
        request: LocationGetGeofenceRequest,
    ) -> LocationGetGeofenceResponse:
        client = self._require_client()
        return await self._execute(client.get_geofence, request, LocationGetGeofenceResponse)

    async def get_job(
        self,
        request: LocationGetJobRequest,
    ) -> LocationGetJobResponse:
        client = self._require_client()
        return await self._execute(client.get_job, request, LocationGetJobResponse)

    async def get_map_glyphs(
        self,
        request: LocationGetMapGlyphsRequest,
    ) -> LocationGetMapGlyphsResponse:
        client = self._require_client()
        return await self._execute(client.get_map_glyphs, request, LocationGetMapGlyphsResponse)

    async def get_map_sprites(
        self,
        request: LocationGetMapSpritesRequest,
    ) -> LocationGetMapSpritesResponse:
        client = self._require_client()
        return await self._execute(client.get_map_sprites, request, LocationGetMapSpritesResponse)

    async def get_map_style_descriptor(
        self,
        request: LocationGetMapStyleDescriptorRequest,
    ) -> LocationGetMapStyleDescriptorResponse:
        client = self._require_client()
        return await self._execute(client.get_map_style_descriptor, request, LocationGetMapStyleDescriptorResponse)

    async def get_map_tile(
        self,
        request: LocationGetMapTileRequest,
    ) -> LocationGetMapTileResponse:
        client = self._require_client()
        return await self._execute(client.get_map_tile, request, LocationGetMapTileResponse)

    async def get_place(
        self,
        request: LocationGetPlaceRequest,
    ) -> LocationGetPlaceResponse:
        client = self._require_client()
        return await self._execute(client.get_place, request, LocationGetPlaceResponse)

    async def list_device_positions(
        self,
        request: LocationListDevicePositionsRequest,
    ) -> LocationListDevicePositionsResponse:
        client = self._require_client()
        return await self._execute(client.list_device_positions, request, LocationListDevicePositionsResponse)

    async def list_device_positions_paginated(
        self,
        request: LocationListDevicePositionsRequest,
    ) -> list[LocationListDevicePositionsResponse]:
        return await self._paginate('list_device_positions', request, LocationListDevicePositionsResponse)

    async def list_geofence_collections(
        self,
        request: LocationListGeofenceCollectionsRequest | None = None,
    ) -> LocationListGeofenceCollectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_geofence_collections, request, LocationListGeofenceCollectionsResponse)

    async def list_geofence_collections_paginated(
        self,
        request: LocationListGeofenceCollectionsRequest | None = None,
    ) -> list[LocationListGeofenceCollectionsResponse]:
        return await self._paginate('list_geofence_collections', request, LocationListGeofenceCollectionsResponse)

    async def list_geofences(
        self,
        request: LocationListGeofencesRequest,
    ) -> LocationListGeofencesResponse:
        client = self._require_client()
        return await self._execute(client.list_geofences, request, LocationListGeofencesResponse)

    async def list_geofences_paginated(
        self,
        request: LocationListGeofencesRequest,
    ) -> list[LocationListGeofencesResponse]:
        return await self._paginate('list_geofences', request, LocationListGeofencesResponse)

    async def list_jobs(
        self,
        request: LocationListJobsRequest | None = None,
    ) -> LocationListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, LocationListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: LocationListJobsRequest | None = None,
    ) -> list[LocationListJobsResponse]:
        return await self._paginate('list_jobs', request, LocationListJobsResponse)

    async def list_keys(
        self,
        request: LocationListKeysRequest | None = None,
    ) -> LocationListKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_keys, request, LocationListKeysResponse)

    async def list_keys_paginated(
        self,
        request: LocationListKeysRequest | None = None,
    ) -> list[LocationListKeysResponse]:
        return await self._paginate('list_keys', request, LocationListKeysResponse)

    async def list_maps(
        self,
        request: LocationListMapsRequest | None = None,
    ) -> LocationListMapsResponse:
        client = self._require_client()
        return await self._execute(client.list_maps, request, LocationListMapsResponse)

    async def list_maps_paginated(
        self,
        request: LocationListMapsRequest | None = None,
    ) -> list[LocationListMapsResponse]:
        return await self._paginate('list_maps', request, LocationListMapsResponse)

    async def list_place_indexes(
        self,
        request: LocationListPlaceIndexesRequest | None = None,
    ) -> LocationListPlaceIndexesResponse:
        client = self._require_client()
        return await self._execute(client.list_place_indexes, request, LocationListPlaceIndexesResponse)

    async def list_place_indexes_paginated(
        self,
        request: LocationListPlaceIndexesRequest | None = None,
    ) -> list[LocationListPlaceIndexesResponse]:
        return await self._paginate('list_place_indexes', request, LocationListPlaceIndexesResponse)

    async def list_route_calculators(
        self,
        request: LocationListRouteCalculatorsRequest | None = None,
    ) -> LocationListRouteCalculatorsResponse:
        client = self._require_client()
        return await self._execute(client.list_route_calculators, request, LocationListRouteCalculatorsResponse)

    async def list_route_calculators_paginated(
        self,
        request: LocationListRouteCalculatorsRequest | None = None,
    ) -> list[LocationListRouteCalculatorsResponse]:
        return await self._paginate('list_route_calculators', request, LocationListRouteCalculatorsResponse)

    async def list_tags_for_resource(
        self,
        request: LocationListTagsForResourceRequest,
    ) -> LocationListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, LocationListTagsForResourceResponse)

    async def list_tracker_consumers(
        self,
        request: LocationListTrackerConsumersRequest,
    ) -> LocationListTrackerConsumersResponse:
        client = self._require_client()
        return await self._execute(client.list_tracker_consumers, request, LocationListTrackerConsumersResponse)

    async def list_tracker_consumers_paginated(
        self,
        request: LocationListTrackerConsumersRequest,
    ) -> list[LocationListTrackerConsumersResponse]:
        return await self._paginate('list_tracker_consumers', request, LocationListTrackerConsumersResponse)

    async def list_trackers(
        self,
        request: LocationListTrackersRequest | None = None,
    ) -> LocationListTrackersResponse:
        client = self._require_client()
        return await self._execute(client.list_trackers, request, LocationListTrackersResponse)

    async def list_trackers_paginated(
        self,
        request: LocationListTrackersRequest | None = None,
    ) -> list[LocationListTrackersResponse]:
        return await self._paginate('list_trackers', request, LocationListTrackersResponse)

    async def put_geofence(
        self,
        request: LocationPutGeofenceRequest,
    ) -> LocationPutGeofenceResponse:
        client = self._require_client()
        return await self._execute(client.put_geofence, request, LocationPutGeofenceResponse)

    async def search_place_index_for_position(
        self,
        request: LocationSearchPlaceIndexForPositionRequest,
    ) -> LocationSearchPlaceIndexForPositionResponse:
        client = self._require_client()
        return await self._execute(client.search_place_index_for_position, request, LocationSearchPlaceIndexForPositionResponse)

    async def search_place_index_for_suggestions(
        self,
        request: LocationSearchPlaceIndexForSuggestionsRequest,
    ) -> LocationSearchPlaceIndexForSuggestionsResponse:
        client = self._require_client()
        return await self._execute(client.search_place_index_for_suggestions, request, LocationSearchPlaceIndexForSuggestionsResponse)

    async def search_place_index_for_text(
        self,
        request: LocationSearchPlaceIndexForTextRequest,
    ) -> LocationSearchPlaceIndexForTextResponse:
        client = self._require_client()
        return await self._execute(client.search_place_index_for_text, request, LocationSearchPlaceIndexForTextResponse)

    async def start_job(
        self,
        request: LocationStartJobRequest,
    ) -> LocationStartJobResponse:
        client = self._require_client()
        return await self._execute(client.start_job, request, LocationStartJobResponse)

    async def tag_resource(
        self,
        request: LocationTagResourceRequest,
    ) -> LocationTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, LocationTagResourceResponse)

    async def untag_resource(
        self,
        request: LocationUntagResourceRequest,
    ) -> LocationUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, LocationUntagResourceResponse)

    async def update_geofence_collection(
        self,
        request: LocationUpdateGeofenceCollectionRequest,
    ) -> LocationUpdateGeofenceCollectionResponse:
        client = self._require_client()
        return await self._execute(client.update_geofence_collection, request, LocationUpdateGeofenceCollectionResponse)

    async def update_key(
        self,
        request: LocationUpdateKeyRequest,
    ) -> LocationUpdateKeyResponse:
        client = self._require_client()
        return await self._execute(client.update_key, request, LocationUpdateKeyResponse)

    async def update_map(
        self,
        request: LocationUpdateMapRequest,
    ) -> LocationUpdateMapResponse:
        client = self._require_client()
        return await self._execute(client.update_map, request, LocationUpdateMapResponse)

    async def update_place_index(
        self,
        request: LocationUpdatePlaceIndexRequest,
    ) -> LocationUpdatePlaceIndexResponse:
        client = self._require_client()
        return await self._execute(client.update_place_index, request, LocationUpdatePlaceIndexResponse)

    async def update_route_calculator(
        self,
        request: LocationUpdateRouteCalculatorRequest,
    ) -> LocationUpdateRouteCalculatorResponse:
        client = self._require_client()
        return await self._execute(client.update_route_calculator, request, LocationUpdateRouteCalculatorResponse)

    async def update_tracker(
        self,
        request: LocationUpdateTrackerRequest,
    ) -> LocationUpdateTrackerResponse:
        client = self._require_client()
        return await self._execute(client.update_tracker, request, LocationUpdateTrackerResponse)

    async def verify_device_position(
        self,
        request: LocationVerifyDevicePositionRequest,
    ) -> LocationVerifyDevicePositionResponse:
        client = self._require_client()
        return await self._execute(client.verify_device_position, request, LocationVerifyDevicePositionResponse)
