"""gRPC Client for Streaming"""

import time

import grpc

from src.proto import streaming_pb2
from src.proto import streaming_pb2_grpc


MESSAGE_COUNT = 5


class DemoClient:
    """Implementation of gRPC Client"""

    def __init__(self, stub: streaming_pb2_grpc.StreamingServiceStub):
        self._stub = stub
    
    def stream_data(self, count=MESSAGE_COUNT):
        try:
            request = streaming_pb2.StreamRequest(count=count)
            response_stream = self._stub.StreamData(request)

            start_time = time.time()

            for response in response_stream:
                if response.status == streaming_pb2.ResponseStatus.OK:
                    received = 'Received'
                elif response.status == streaming_pb2.ResponseStatus.DONE:
                    received = 'Final'
                elif response.status == streaming_pb2.ResponseStatus.ERROR:
                    received = 'Error'
                else:
                    received = 'Unknown'

                print(f'[{received}]: {response.message}')

            end_time = time.time()
            duration = end_time - start_time
            print('-' * 50)
            print(f'Stream completed in {duration:.2f} seconds')
        except grpc.RpcError as e:
            print(f'\nRPC Error occurred:')
            print(f'  Status Code: {e.code()}')
            print(f'  Details: {e.details()}')
        except Exception as e:
            print(f'\nUnexpected error: {str(e)}')


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = streaming_pb2_grpc.StreamingServiceStub(channel)
    client = DemoClient(stub)
    client.stream_data()


if __name__ == '__main__':
    run()
