from graphviz import *
from src.api.functions import *


def visualize_ast(ast, output_path='test-output/result.gv'):
    graph = Graph(comment="AST result")
    traverse_ast(ast, graph)
    graph.render(output_path, format='png', view=False)


def get_node_label(node):
    label = node['type']
    infos = node['info']
    if infos is not None:
        for info in infos:
            label = label + "\n" + str(info) + ": " + str(infos[info])
    return label


node_counter = 0


def traverse_ast(ast, graph, parent_counter=None):
    global node_counter
    node_counter += 1
    node_label = get_node_label(ast)
    now_counter = node_counter

    graph.node(str(now_counter), node_label)
    if parent_counter is not None:
        graph.edge(str(parent_counter), str(now_counter))

    if 'children' not in ast:
        return

    for i, child in enumerate(ast['children']):
        traverse_ast(child, graph, now_counter)


if __name__ == "__main__":
    file_path = '../backend/parser/input/4.in'
    ast = get_ast(file_path)
    visualize_ast(ast)
