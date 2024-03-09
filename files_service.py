class FilesService:
    def __init__(self, files_repo):
        self.files_repo = files_repo

    def process_deleted_files(self, file_ids: Set[str]):
        """
        Processes deleted files.

        Args:
        - file_ids: Set of file IDs that were deleted.
        """
        for file_id in file_ids:
            file_type = self.files_repo.get_file_type(file_id)
            if file_type == 'static':
                self.files_repo.mark_file_for_permanent_removal(file_id)
            elif file_type == 'preview':
                if not self.files_repo.check_file_associations(file_id):
                    self.files_repo.mark_file_for_permanent_removal(file_id)
            elif file_type == 'production':
                pass  # Production images are skipped for now
