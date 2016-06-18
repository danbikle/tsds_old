#!/bin/bash

# sqlite_csv.bash

# This script should load /tmp/allpredictions.csv into a sqlite table.

# I should build a simple sql script:

cd /tmp/

cat > /tmp/sqlite_csv.sql <<EOF
--
-- sqlite_csv.sql
--

-- This script should load allpredictions.csv into a Sqlite table.

-- Demo:
-- sqlite3 -init sqlite_csv.sql sqlite_csv.db

.echo on
drop table   allpredictions;
create table allpredictions
EOF

# The tricky part to this script is getting a list of all the column names copied into a sql script:

curl www.spy611.com/csv/allpredictions.csv > allpredictions.csv
head -1 allpredictions.csv |\
    sed '1s/^/(/'          |\
    sed '1s/,/ string,/g'  |\
    sed '1s/$/ string);/' > cols.txt

# Now I should have a list of column names.
# I should add the names to the script:
cat cols.txt >> /tmp/sqlite_csv.sql

cat >> /tmp/sqlite_csv.sql <<EOF

.separator ,
.import /tmp/allpredictions_nh.csv allpredictions

-- I should run some interesting queries:

select count(*) from allpredictions;
select min(pctlead), avg(pctlead), max(pctlead) from allpredictions;
select min(pctlead), avg(pctlead), max(pctlead) from allpredictions where pctlag1 < -1.0;
select min(pctlead), avg(pctlead), max(pctlead) from allpredictions where pctlag1 >  1.0;

.quit

EOF

# I should remove column names from CSV:
cat /tmp/allpredictions.csv | sed 1d > /tmp/allpredictions_nh.csv

# I should run the sql now:
sqlite3 sqlite_csv.db <<EOF
.read sqlite_csv.sql
EOF

exit
