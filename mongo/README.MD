# Installing and running MongoDB 
## https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

MongoDB only supports the 64-bit versions of these platforms. To determine which Ubuntu release your host is running, run the following command on the host's terminal:

    cat /etc/lsb-release
Import the public key used by the package management system:

    sudo apt-get install gnupg curl
To import the MongoDB public GPG key, run the following command:

    curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
Create the list file /etc/apt/sources.list.d/mongodb-org-7.0.list for your version of Ubuntu.

    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
Issue the following command to reload the local package database:

    sudo apt-get update
You can install either the latest stable version of MongoDB or a specific version of MongoDB.

    sudo apt-get install -y mongodb-org
You can start the mongod process by issuing the following command:

    sudo systemctl start mongod
If you receive an error similar to the following when starting mongod: Failed to start mongod.service: Unit mongod.service not found. Run the following command first:

    sudo systemctl daemon-reload
Then run the start command above again. Verify that MongoDB has started successfully.

    sudo systemctl status mongod
As needed, you can stop the mongod process by issuing the following command:

    sudo systemctl stop mongod
You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:

    sudo systemctl enable mongod

Start a mongosh session on the same host machine as the mongod. You can run mongosh without any command-line options to connect to a mongod that is running on your localhost with default port 27017.

    mongosh
https://www.mongodb.com/docs/mongodb-shell/

## https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-windows/
Remove MongoDB Community Edition as a Windows Service

    sc.exe delete MongoDB
Create the data directory where MongoDB stores data. MongoDB's default data directory path is the absolute path \data\db on the drive from which you start MongoDB.

To start MongoDB, run mongod.exe.

    "C:\Program Files\MongoDB\Server\8.0\bin\mongod.exe" --dbpath="c:\data\db"
The --dbpath option points to your database directory. If the MongoDB database server is running correctly, the Command Interpreter displays:
``` Bash
[initandlisten] waiting for connections
```
Depending on the 
Windows Defender Firewall
 settings on your Windows host, Windows may display a Security Alert dialog box about blocking "some features" of C:\Program Files\MongoDB\Server\8.0\bin\mongod.exe from communicating on networks.

Open a new Command Interpreter and enter mongosh.exe to connect to MongoDB. By default, MongoDB launches with bindIp set to 127.0.0.1, which binds to the localhost network interface. This means that the mongod.exe can only accept connections from clients that are running on the same machine. Remote clients will not be able to connect to the mongod.exe, and the mongod.exe will not be able to initialize a replica set unless this value is set to a valid network interface.

This value can be configured either:
- in the MongoDB configuration file with bindIp, or
- via the command-line argument --bind_ip

Before you bind your instance to a publicly-accessible IP address, you must secure your cluster from unauthorized access. For a complete list of security recommendations, see [Security Checklist for Self-Managed Deployments](https://www.mongodb.com/docs/v8.0/administration/security-checklist/#std-label-security-checklist). At minimum, consider enabling [authentication](https://www.mongodb.com/docs/v8.0/administration/security-checklist/#std-label-checklist-auth) and [hardening](https://www.mongodb.com/docs/v8.0/core/security-hardening/#std-label-network-config-hardening) network infrastructure.

If you installed MongoDB with the Windows installer (.msi), the .msi automatically upgrades within its release series (e.g. 7.2.1 to 7.2.2). Upgrading a full release series (e.g. 6.0 to 7.0) requires a new installation.

Also see, https://www.mongodb.com/docs/v8.0/reference/configuration-options/#std-label-configuration-options

## mongosh
### https://www.mongodb.com/docs/mongodb-shell/connect/#std-label-mdb-shell-connect

Atlas:

    mongosh "mongodb+srv://YOUR_CLUSTER_NAME.YOUR_HASH.mongodb.net/" --apiVersion YOUR_API_VERSION --username YOUR_USERNAME
Local:

    mongosh "mongodb://localhost:27017"
Remote:

    mongosh "mongodb://mongodb0.example.com:28015"
or:

    mongosh --host mongodb0.example.com --port 28015

Auth:

    mongosh "mongodb://mongodb0.example.com:28015" --username alice --authenticationDatabase admin
### https://www.mongodb.com/docs/mongodb-shell/run-commands/
To display the database you are using, type `db`.

To list the databases available to the user, use the helper `show dbs`. To create a new database, issue the `use <db>` command with the database that you would like to create. For example, the following commands create both the database `myNewDatabase` and the collection `myCollection` using the `insertOne()` operation:
``` Bash
use myNewDatabase
db.myCollection.insertOne( { x: 1 } );
```
If a collection does not exist, MongoDB creates the collection when you first store data for that collection.



