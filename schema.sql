CREATE TABLE "sites"(
    "id" UUID PRIMARY KEY NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "opened_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "closed_at" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "status" VARCHAR(255) NOT NULL
);

CREATE TABLE "items"(
    "id" UUID PRIMARY KEY NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "description" VARCHAR(255) NOT NULL
);

CREATE TABLE "sites_items"(
    "site_id" UUID NOT NULL,
    "item_id" UUID NOT NULL,
    PRIMARY KEY("site_id", "item_id"),
    FOREIGN KEY("site_id") REFERENCES "sites"("id"),
    FOREIGN KEY("item_id") REFERENCES "items"("id")
);

CREATE TABLE "files"(
    "id" UUID PRIMARY KEY NOT NULL,
    "uploaded_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "file_name" VARCHAR(255) NOT NULL,
    "file_size" BIGINT NOT NULL,
    "content_type" VARCHAR(255) NOT NULL
);

CREATE TABLE "items_files"(
    "item_id" UUID NOT NULL,
    "file_id" UUID NOT NULL,
    PRIMARY KEY("item_id", "file_id"),
    FOREIGN KEY("item_id") REFERENCES "items"("id"),
    FOREIGN KEY("file_id") REFERENCES "files"("id")
);

CREATE TABLE "files_events"(
    "id" UUID PRIMARY KEY NOT NULL,
    "file_id" UUID NOT NULL,
    "action" VARCHAR(255) NOT NULL,
    FOREIGN KEY("file_id") REFERENCES "files"("id")
);