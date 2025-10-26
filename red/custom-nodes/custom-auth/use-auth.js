module.exports = function(RED) {
    function UseAuthNode(config) {
        RED.nodes.createNode(this, config);

        const node = this;
        node.status({});

        // Support Node-RED 0.x send/done signature
        const send = node.send || function() {};
        const done = node.done || function() {};

        node.authNode = RED.nodes.getNode(config.auth);

        if (!node.authNode || !node.authNode.apiKey) {
            node.status({ fill: "red", shape: "ring", text: "missing auth" });
            node.error("Custom Auth config node is missing or has no API key");
            return;
        }

        node.status({ fill: "green", shape: "dot", text: "auth ready" });

        node.on("input", function(msg, _send, _done) {
            const effectiveSend = _send || send;
            const effectiveDone = _done || done;

            msg.apiKey = node.authNode.apiKey;
            effectiveSend(msg);
            effectiveDone();
        });
    }

    RED.nodes.registerType("use-auth", UseAuthNode, {
        credentials: {},
        category: "function",
        color: "#a6bbcf",
        defaults: {
            name: { value: "" },
            auth: { type: "custom-auth", required: true }
        },
        inputs: 1,
        outputs: 1,
        icon: "function.png",
        label: function() {
            return this.name || "use-auth";
        }
    });
};

