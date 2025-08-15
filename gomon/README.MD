https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

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