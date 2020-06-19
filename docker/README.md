# Dockerized ARTN-OBS Database

This code requires a database with Q3C indexing enabled. For authorized users
who wish to run this code on a local machine, we can provide:

  - a commpressed tarball of the  docker image (eg., artn_postgres_12_q3c2.tgz)
  - a SQL snapshot of the database at some time (eg., psql.artn.20200619.sql)
  - utilities (eg., psql.backup.sh, psql.cleanup.sh, psql.restore.sh, psql.size.sh)

Obviously, you must have docker installed.

We provide a utility script (docker.template.sh) which you can edit as you see
fit.  The only variable you need to edit should be my_password. If you do not 
edit it, you should be able to do the following:

1. Load the docker container:

    ```bash
      % bash docker.template.sh --command=load --file=artn_postgres_12_q3c2.tgz --dry-run
    ```

If it looks good, repeat the command but omit the `--dry-run` flag.

2. Start the docker container:
 
    ```bash
      % bash docker.template.sh --command=start --name=artn --dry-run
    ```

If it looks good, repeat the command but omit the `--dry-run` flag.

3. Connect to the docker container:


    ```bash
      % bash docker.template.sh --command=connect --name=artn --dry-run
    ```

If it looks good, repeat the command but omit the `--dry-run` flag.

You should now be *inside* the container. The command line prompt should
change to "root@<container-id>:/# ". If so -- and being very careful -- execute
the following commands (with whatever password you chose):

    ```bash
      % root@a6e273172bc7:/# cd /backups
      % root@a6e273172bc7:/# PGPASSWORD=db_secret psql -h localhost -p 5432 -d artn -U artn -c "DROP TABLE IF EXISTS obsreqs;"
      % root@a6e273172bc7:/# PGPASSWORD=db_secret psql -h localhost -p 5432 -d artn -U artn -c "DROP TABLE IF EXISTS users;"
      % root@a6e273172bc7:/# PGPASSWORD=db_secret psql -h localhost -p 5432 -d artn -U artn -c "CREATE EXTENSION q3c;"
      % root@a6e273172bc7:/# bash psql.restore.sh --filename=psql.artn.20200619.sql --authorization=artn:db_secret
      % root@a6e273172bc7:/# bash psql.cleanup.sh
    ```

You should now be good to go!
