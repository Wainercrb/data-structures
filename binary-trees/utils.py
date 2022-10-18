def print_tree(root):
    '''Print the object as plan text'''
    f = open('result.txt','w+')
    result = ''
    quene = []
    quene.append(root)
    
    while len(quene) != 0:
        node = quene[0]

        if node.left == None:
            ll = '-'
        else:
            ll = node.left.value
        if node.right == None:
            rr = '-'
        else:
            rr = node.right.value

        result += '  {n}  \n _|_ \n|   |\n{l}   {r}\n==========='.format(n = node.value, l = ll, r = rr) + '\n'
        quene.pop(0)

        if node.left != None:
            quene.append(node.left)
        if node.right != None:
            quene.append(node.right)

    f.write(result)