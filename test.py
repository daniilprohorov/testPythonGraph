#!/usr/bin/python3

import string
#name of file
file_name = 'tree-task.dot'

#alf = set([chr(letter) for letter in range(ord('A'), ord('Z'))])
alf = set(string.ascii_uppercase)


#take only strings with '->'
def fileParse(file_name):
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('FileNotFound')
        exit(1)
    str_f = [line for line in f if '->' in line]
    return str_f


#take only latters being in 'alf' set
def lineParse(lines):
    out_lines = []
    for line in lines:
        out_lines.append([char for char in line if char in alf])
    return out_lines


# create a dictionary
# 'key_letter' : [array_of_nodes]
# example:  'A' : ['B', 'C', 'D'] 
def createGraph(lines):
    g = dict()
    for line in lines:
        if line[0] in g.keys():
            g[line[0]].append(line[1])
        else:
            g[line[0]] = list(line[1])
    return g


# output Graph like in task
def printGraph(g):
    if g:

        #list for storing key, before concat
        key_str = []

        #list of keys in dict
        keys = list(g.keys())

        #output list
        out = []

        def _printGraph(key, key_str):
            if key in keys:
                keys.remove(key)
                key_str.append(key)

                #list for nodes that not in key of dict 
                local_out = []
                for node in g[key]:
                    if node in keys:
                        _printGraph(node, key_str)
                        key_str.remove(node)
                    else:
                        local_out.append(node)
                        out.append(key_str + local_out)
                        local_out.remove(node)

        _printGraph(keys[0], key_str)

        for line in out:
            print(''.join(line))

    else:
        print('Graph is empty')

printGraph(createGraph(lineParse(fileParse(file_name))))
