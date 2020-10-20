from os import getenv
import unittest
from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
JSON = {
    "1": {
        "1": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 123,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
        "2": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 24,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
        "3": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 24,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
        "4": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 24,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
    },
    "2": {
        "5": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 123,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
        "6": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 24,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
        "7": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 24,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
        "8": {
            "Image": "http://lorempixel.com/640/480/abstract",
            "Inappropriate": False,
            "Sensitive": False,
            "Status": "APPROVED",
            "Complexity": 24,
            "Pages": {
                "1": "http://lorempixel.com/640/480/abstract",
                "2": "http://lorempixel.com/640/480/abstract",
            },
        },
    },
}


security_header = getenv("DS_SECRET_TOKEN")


class TestClustering(TestCase):
    def test_cluster_endpoint(self):
        r = client.post(
            "/cluster",
            json=JSON,
            headers=dict({"authorization": security_header}),
        )
        print("status code: " + str(r.status_code))
        print(r.content)
        self.assertEqual(r.content, b'"{\\"1\\": [[\\"1\\", \\"2\\"]]}"')

