class JobSchedulingService:
    """
    Service class for scheduling jobs related to file removal processes.
    """

    def __init__(self, database, file_servers):
        """
        Initialize JobSchedulingService with database and file servers.

        Args:
        - database: Database connection object.
        - file_servers: List of file servers.
        """
        self.database = database
        self.file_servers = file_servers

    def schedule_jobs(self):
        """
        Schedules jobs for file removal process.

        This method schedules two types of jobs:
        1. Regular Images Removal Job:
           - Removes files marked for permanent removal.
        2. Orphan Images Removal Job:
           - Removes orphan images (production images not associated with any items).

        Note:
        - Regular Images Removal Job has higher priority due to its critical nature.
        """
        # 1. Regular Images Removal Job (Higher Priority)
        self.regular_images_removal_job()

        # 2. Orphan Images Removal Job
        self.orphan_images_removal_job()

    def regular_images_removal_job(self):
        """
        Job for removing regular images marked for permanent removal.
        """
        try:
            batch_size = 100  # Define batch size for batch processing
            files_to_remove = self.database.get_files_for_removal(batch_size)

            while files_to_remove:
                for file_info in files_to_remove:
                    file_id = file_info['file_id']
                    file_path = file_info['file_path']

                    # Remove the file from servers
                    self.file_servers.remove_file(file_path)

                    # Remove record from the files table
                    self.database.remove_file_record(file_id)

                # Fetch the next batch of files for removal
                files_to_remove = self.database.get_files_for_removal(batch_size)
        except Exception as e:
            # Log the exception or handle it appropriately
            print(f"Error in regular images removal job: {str(e)}")

    def orphan_images_removal_job(self):
        """
        Job for removing orphan images (production images not associated with any items).
        """
        try:
            orphan_images = self.database.get_orphan_images()
            for image_id in orphan_images:
                # Remove the orphan image from file servers
                self.file_servers.remove_image(image_id)

                # Remove record from the files table
                self.database.remove_file_record(file_id)
        except Exception as e:
            # Log the exception or handle it appropriately
            print(f"Error in orphan images removal job: {str(e)}")
