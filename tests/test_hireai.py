import unittest
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

class TestHireAI(unittest.TestCase):
    def test_root(self):
        res = client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("HireAI", res.json()["service"])

    def test_get_problems(self):
        res = client.get("/api/problems/fullstack")
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.json()["problems"]), 0)

    def test_evaluate_optimal_code(self):
        payload = {
            "role": "fullstack",
            "problemId": 2,
            "userCode": "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "spokenExplanation": "I am using a hash map to achieve single-pass O(N) time complexity."
        }
        res = client.post("/api/evaluate", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(data["overallScore"], 80)
        self.assertIn("Hire", data["verdict"])

if __name__ == "__main__":
    unittest.main()
