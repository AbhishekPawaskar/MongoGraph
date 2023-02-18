import datetime
from mongograph import MongoGraph

URL="mongodb+srv://abhi:ihba@cluster0.gzrlkwv.mongodb.net/?retryWrites=true&w=majority"
#URL = "ws://localhost:8182/gremlin"


try:
    client_class = MongoGraph(connection_string=URL)
    print("\ntest 1 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 1 failed "+str(connection_err))

try:
    ack = client_class.is_connected()
    print("\ntest 1a passed\n")
except Exception as connection_err:
    raise RuntimeError("test 1a failed "+str(connection_err))

try:
    id1 = client_class.add_node(label="user",properties={"name":"new name"})
    print("\ntest 2 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 2 failed "+str(connection_err))

try:
    id2 = client_class.add_node(label="user",properties={"name":"new name2"})
    ack = client_class.update_node(properties={"name":"no name"}, label="user", node_id=id2)
    if ack:
        print("\ntest 3 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 3 failed "+str(connection_err))

try:
    eid = client_class.add_edge(label="follow",
                                    from_node_label="user",
                                    to_node_label="user",
                                    from_node_id=id1,
                                    to_node_id=id2,
                                    properties={"name":"hello"})
    if eid:
        print("\ntest 4 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 4 failed "+str(connection_err))

try:
    ack = client_class.update_edge(label="follow", edge_id=eid , properties={"property1":datetime.datetime.now()})
                                    
    if ack:
        print("\ntest 5 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 5 failed "+str(connection_err))

try:
    ack = client_class.delete_edge(edge_id=eid, label="follow")                             
    if ack:
        print("\ntest 6 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 6 failed "+str(connection_err))

try:
    ack1 = client_class.delete_node(node_id=id1, label="user")
    ack2 = client_class.delete_node(node_id=id2, label="user")                           
    if ack1 and ack2:
        print("\ntest 7 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 7 failed "+str(connection_err))

try:
    ack = client_class.close_instance()                      
    if ack:
        print("\ntest 8 passed\n")
except Exception as connection_err:
    raise RuntimeError("test 8 failed "+str(connection_err))

print("test completed")


















