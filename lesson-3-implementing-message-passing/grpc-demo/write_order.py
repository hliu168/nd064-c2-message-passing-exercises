import grpc
import computer_orders_pb2
import computer_orders_pb2_grpc

print("Sending sample payload")

channel = grpc.insecure_channel("localhost:5005")
stub = computer_orders_pb2_grpc.OrderServiceStub(channel)

order = computer_orders_pb2.OrderMessage(
	id = "2222",
	created_by = "USER123",
	status = computer_orders_pb2.OrderMessage.Status.QUEUED,
	created_at = "2020-03-12",
	equipment = [ computer_orders_pb2.OrderMessage.Equipment.KEYBOARD ]
)

response = stub.Create(order)
