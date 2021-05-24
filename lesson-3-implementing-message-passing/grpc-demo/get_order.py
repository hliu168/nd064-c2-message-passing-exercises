import grpc
import computer_orders_pb2
import computer_orders_pb2_grpc

print("Sending sample payload")

channel = grpc.insecure_channel("localhost:5005")
stub = computer_orders_pb2_grpc.OrderServiceStub(channel)

response = stub.Get(computer_orders_pb2.Empty())
print(response)
