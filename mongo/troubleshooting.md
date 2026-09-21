# Mongo v6.0.0 immediately exits with featureCompatibilityVersion error
https://www.mongodb.com/community/forums/t/mongo-v6-0-0-immediately-exits-with-featurecompatibilityversion-error/181080/5
``` bash
    "error": "UPGRADE PROBLEM: Found an invalid featureCompatibilityVersion document (ERROR: Location4926900: Invalid featureCompatibilityVersion document in admin.system.version: { _id: \"featureCompatibilityVersion\", version: \"4.4\" }. See https://docs.mongodb.com/master/release-notes/5.0-compatibility/#feature-compatibility. :: caused by :: Invalid feature compatibility version value, expected '5.0' or '5.3' or '6.0. See https://docs.mongodb.com/master/release-notes/5.0-compatibility/#feature-compatibility.). If the current featureCompatibilityVersion is below 5.0, see the documentation on upgrading at https://docs.mongodb.com/master/release-notes/5.0/#upgrade-procedures."
```
I have been able to replicate this error by starting up MongoDB 4.4.15. Once it was running I stopped it. I then started up MongoDB 6.0.0 and pointed it at the same path that the 4.4.15 version wrote its database files to and I got the FCV error and the process stopped. This seems to be what you are seeing.

If you want to save your data, you can fix this, by [downloading the compressed archive of 5.0](https://www.mongodb.com/try/download/community) and extract it. From this extracted folder you can run `./bin/mongod --dbpath <current database path>`. Connect to this instance with mongosh and run `db.adminCommand( { setFeatureCompatibilityVersion: "5.0" } )`. This will change the FCV for you. You can then exit mongosh and then shutdown the mongod instance and finally start your version 6.0.0 server. You will want to change the FCV here as well to be 6.0.
## Is it good practice to update the FCV after each major release of mongo? Is there a reason it doesn’t happen automatically?
I think the reason for that is that if you need to roll back due to a failed upgrade having the FCV automatically change could cause even more problems. It’s better to leave the FCV at the upgraded from version for a bit to make sure things work as planned and then only change that to the upgraded to version.

Also see, https://www.mongodb.com/docs/manual/reference/command/setfeaturecompatibilityversion/#default-values

- (https://stackoverflow.com/questions/75555947/kubernetes-mongodb-operator-invalid-featurecompatibilityversion-document-in-a)
- (https://www.mongodb.com/docs/manual/release-notes/8.0-upgrade-replica-set/)