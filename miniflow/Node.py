class Node(object):
    def __init__(self, inbound_nodes):
        # Nodes from which this Node receives values.
        self.inbound_nodes = inbound_nodes
        # Nodes to which this Node brodcast results.
        self.outbound_nodes = []

        # Append myself as a outbound_node to all input nodes.
        for input_node in self.inbound_nodes:
            input_node.outbound_nodes.append(self)

        # Resulting value
        self.value = None

    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_nodes` and store
        the result in self.value
        :return:
        """

    raise NotImplemented


class Input(Node):
    def __init__(self):

    # An Input node has no inbound nodes, so no need to pass anything
    # further.

    # NOTE: Input node is the only node where the value may be passed as an
    # argument to forward(). All other node implementations should get the
    # value of the previous node from self.inbound_nodes.
    def forward(self, value=None):
        if value is not None:
            self.value = value
