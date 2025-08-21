"""gRPC Server for Streaming"""

from concurrent import futures
import time

import grpc

from src.proto import streaming_pb2
from src.proto import streaming_pb2_grpc


class StreamingServiceImpl(streaming_pb2_grpc.StreamingServiceServicer):
    """Implementation of Streaming Service"""

    def StreamData(self,
                   request: streaming_pb2.StreamRequest,
                   context: grpc.ServicerContext):
        count = request.count
        print(f'Streaming {count} messages...')

        try:
            for i in range(count):
                if i == count - 1:
                    status = streaming_pb2.ResponseStatus.DONE
                else:
                    status = streaming_pb2.ResponseStatus.OK
                message = f'Message {i + 1}/{count}'

                response = streaming_pb2.StreamResponse(
                    message=message,
                    sequence_number=i + 1,
                    timestamp=int(time.time() * 1000),
                    status=status)
                yield response
        except Exception as e:
            error_response = streaming_pb2.StreamResponse(
                message=f'Error occurred: {str(e)}',
                sequence_number=-1,
                timestamp=int(time.time() * 1000),
                status=streaming_pb2.ResponseStatus.ERROR
            )
            yield error_response


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_StreamingServiceServicer_to_server(
        StreamingServiceImpl(),
        server)
    listen_addr = '127.0.0.1:50051'
    server.add_insecure_port(listen_addr)

    print('Starting gRPC server on port 50051...')
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print('\nShutting down...')
        server.stop(grace=5)


if __name__ == '__main__':
    run()
