class SitesController:
    """
    Controller class for managing site-related operations.
    """

    def __init__(self, sites_service):
        """
        Initialize SitesController with SitesService.

        Args:
        - sites_service: SitesService object for site management operations.
        """
        self.sites_service = sites_service

    async def delete_items(self, site_id: str, payload: ItemsIdsPayload):
        """
        Handles the deletion of items from a site.

        Args:
        - site_id: ID of the site from which items will be deleted.
        - payload: Payload containing items IDs to be deleted.

        Returns:
        - dict: Response indicating the success or failure of the deletion operation.
        """
        try:
            success = await self.sites_service.delete_items(site_id, payload.item_ids)

            if success:
                return {'message': 'Items deleted successfully'}
            else:
                raise HTTPException(status_code=500, detail='Failed to delete items')
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.delete('/sites/{site_id}/items', response_model=dict)
async def delete_items(site_id: str = Path(..., title="The ID of the site to delete items from"),
                       payload: ItemsIdsPayload):
    return await site_controller.delete_items(site_id, payload)
