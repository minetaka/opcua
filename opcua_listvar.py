from opcua import Client
from opcua import ua
import argparse
import os.path

class MkdirFileType(argparse.FileType):
    def __call__(self, string):
        if string and "w" in self._mode:
            if os.path.dirname(string):
                os.makedirs(os.path.dirname(string), exist_ok=True)
        return super().__call__(string)


class AllowablePort(object):
    def __init__(self, minvalue=None, maxvalue=None, vtype='integer'):
        self.min = minvalue
        self.max = maxvalue
        self.type = vtype

    def __contains__(self, val):
        ret = True
        if self.min is not None:
            ret = ret and (val >= self.min)

        if self.max is not None:
            ret = ret and (val <= self.max)

        return ret

    def __iter__(self):
        low = self.min
        if low is None:
            low = "-inf"
        high = self.max
        if high is None:
            high = "+inf"
        L1 = self.type
        L2 = " {} <= x <= {}".format(low, high)
        return iter((L1, L2))

def GetNode(level, node):
    try:
        level += 1
        indent = ' ' * 4 * level

        for child in node.get_children():
            node = client.get_node(child)
            nodeclass = node.get_node_class()
            name = (str(node.get_browse_name()).replace('QualifiedName(','')).replace(')','')

            if nodeclass == ua.NodeClass.Object:
                print('{}{}/'.format(indent, name), file=args.file)
                GetNode(level, node)

            elif nodeclass == ua.NodeClass.ObjectType:
                print('{}{}/'.format(indent, name), file=args.file)
                GetNode(level, node)

            elif nodeclass == ua.NodeClass.Variable:
                val = str(node.get_value())
                cont = ''
                if len(val) > 120:
                    cont = '.....'
                val = val[:120]
                print('{}{}[{}{}]'.format(indent, name, val, cont), file=args.file)

            elif nodeclass == ua.NodeClass.VariableType:
                val = str(node.get_value())
                cont = ''
                if len(val) > 30:
                    cont = '.....'
                val = val[:20]
                print('{}{}[{}{}]'.format(indent, name, val, cont), file=args.file)

            else:
                pass
    except:
        pass

    finally:
        level -= 1

if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--server', type=str, default='192.168.1.51', help='OPC Server IP address, Default=localhost')
        parser.add_argument('-p', '--port', type=int, default=4840, choices=AllowablePort(minvalue=1024,maxvalue=65535), help='Port number, Default=4840')
        fpath = os.path.dirname(__file__) + os.path.sep + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
        parser.add_argument('-f', '--file', type=MkdirFileType(mode='w', encoding='shift_jis'), default=fpath, help='Text file pathname, Default=./opcua_listvar.txt')

        args = parser.parse_args()

        url = 'opc.tcp://'
        url += args.server
        url += ':' + str(args.port)

        try:
            client = Client(url) # connect using a user
            client.connect()
            root = client.get_root_node()

            level = -1
            GetNode(level, root)
 
        except:
            print("Connection Failed")
            
        else:
            client.disconnect()
    
    except:
        pass

    else:
        print('Terminated')
