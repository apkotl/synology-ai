FROM nodered/node-red:latest


# Arguments from docker-compose
ARG ARG_SETTINGS_FILE=settings.js

# Copy package.json to the WORKDIR so npm builds all
# of your added nodes modules for Node-RED
#WORKDIR /data
#COPY package.json /data
#RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production
#WORKDIR /usr/src/node-red

# Copy _your_ Node-RED project files into place
# NOTE: This will only work if you DO NOT later mount /data as an external volume.
#       If you need to use an external volume for persistence then
#       copy your settings and flows files to that volume instead.
#COPY ${ARG_SETTINGS_FILE} /data/settings.js
#COPY flows_cred.json /data/flows_cred.json
#COPY flows.json /data/flows.json