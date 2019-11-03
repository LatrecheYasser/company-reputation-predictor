#!/bin/bash
# create automatic backup setting script


## create a backup repo in /var/backups/elasticsearch and insrte this path in elasticsearch.yml
mkdir -p /var/backups/elasticsearch
cat >> /etc/elasticsearch/elasticsearch.yml << EOF
path.repo: ["/var/backups/elasticsearch"]
EOF

## define an Env variable for the upcoming Crul query 
URL_REQ=”http://localhost:9200/_snapshot/my_backup”

curl -m 30 -XPUT $URL_REQ -H ‘Content-Type: application/json’ -d ‘{
 “type”: “fs”,
 “settings”: {
 “location”: “/var/backups/elasticsearch”,
 “compress”: true
 }
}’

backup_index=”articles”
TIMESTAMP=`date +%Y%m%d`#specify the index to backup
#include_global_state: to prevent the cluster global state to be stored as part of the snapshot
curl -XPUT “$URL_REQ/$TIMESTAMP?wait_for_completion=true” -H ‘Content-Type: application/json’ -d ‘{“indices”: “$backup_index”,
 “ignore_unavailable”: true,
 “include_global_state”: false
}’# The amount of snapshots we want to keep.
LIMIT=30# Get a list of snapshots we want to delete omitting the most recent index
SNAPSHOTS=`curl -m 30 -s -XGET “$URL_REQ/_all” -H ‘Content-Type: application/json’ \
 | jq “.snapshots[:-${LIMIT}][].snapshot”`# Loop over the results and delete old snapshots
for SNAPSHOT in $SNAPSHOTS
do
 echo “Deleting snapshot: $SNAPSHOT”
 curl -m 30 -s -XDELETE ‘$URL_REQ/$SNAPSHOT?pretty’
done
echo “Done!”
