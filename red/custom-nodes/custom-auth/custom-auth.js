module.exports = function(RED) {
    function CustomAuthNode(config) {
        RED.nodes.createNode(this, config);
        this.name = config.name;
        const credentials = this.credentials || {};
        this.apiKey = credentials.apiKey;
    }

    RED.nodes.registerType("custom-auth", CustomAuthNode, {
        credentials: {
            apiKey: { type: "password" }
        }
    });
};
