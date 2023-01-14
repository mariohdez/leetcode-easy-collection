from data_structures.node import Node

class DeleteNodeSolution:
    def deleteNode(self, node: Node):
        nextNode = node.next

        node.val = nextNode.val

        node.next = nextNode.next
        nextNode.next = None