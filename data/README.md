# Data

The BBC Good Food sitemap has a separate sitemap for each day which links to the recipes which have been added or updated on that day. My original plan was to have two jobs.

1. An initial job which would scrape all the recipes on the site.

2. A daily cron job to scrape the new and update recipes from the previous day.

I never got around to implementing the second job and I currently have no intention to. This is because the sitemap seems to change regularly making the scraper jobs frustrating to maintain.

For now I just have static data from the last time I ran the full scraper. This has been exported using `mysqldump` into `WhatsIn.sql` in this directory. This file can be executed to populate the database.

```shell
mysql --user root --password mysql < WhatsIn.sql
```

This directory is mounted to `/docker-entrypoint-initdb.d` in the mysql container which will automatically execute it when the container started for the first time. See [Initializing a fresh instance](https://hub.docker.com/_/mysql/).