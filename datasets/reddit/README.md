https://www.kaggle.com/vectorinstitute/domainspecific-reddit-data-medical-and-financial

The dataset is organized as a PostgreSQL database dump. In order to restore the dataset, you must have a PostgreSQL server.

You should first create a new database, and use the command below to restore the content to the database using the file ` reddit_data_export.db` downloaded here. 
```bash
pg_restore -h <host of the database server> -p <port of the database server > --no-owner -U postgres -W -d <the new database you created> reddit_data_export.db
```
