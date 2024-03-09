class SitesService:
    """
    Service class for managing items on sites.
    """

    def __init__(self, sites_repository, message_broker):
        """
        Initialize SitesService with repositories and message broker.

        Args:
        - sites_repository: Repository for managing site data.
        - message_broker: Message broker for communication.
        """
        self.sites_repository = sites_repository
        self.message_broker = message_broker

    def delete_items(self, site_id: str, item_ids: Set[str]) -> bool:
        """
        Deletes items from the site.

        Args:
        - site_id: ID of the site.
        - item_ids: Set of item IDs to be deleted.

        Returns:
        - bool: True if deletion successful, False otherwise.
        """
        file_ids = self.sites_repository.get_file_ids_for_items(item_ids)
        success = self.sites_repository.remove_item_relationships(site_id, item_ids)

        if success:
            self.message_broker.publish_deleted_files(file_ids)

        return success

