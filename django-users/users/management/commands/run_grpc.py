import time
from concurrent import futures

import grpc

from django.core.management.base import BaseCommand

from users import auth_pb2_grpc
from users import grpc_services

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('-p', '--port', type=int, default=5000)
        parser.add_argument('-m', '--max-workers', type=int, default=16)

    def handle(self, *args, **options):
        max_workers = options.get('max-workers')
        port = options.get('port')
        grpc_interface = '[::]'
        thread_pool = futures.ThreadPoolExecutor(max_workers=max_workers)
        grpc_server = grpc.server(thread_pool=thread_pool)
        grpc_server.add_insecure_port(grpc_interface + ':' + str(port))

        auth_pb2_grpc.add_AuthControllerServicer_to_server(
            grpc_services.AuthServicer(),
            grpc_server)

        self.stdout.write("Starting server...")
        grpc_server.start()
        self.stdout.write("Server started")

        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            self.stdout.write("\nStopping server...")
            grpc_server.stop(0)

        self.stdout.write("Server stopped")