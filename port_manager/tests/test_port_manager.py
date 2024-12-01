import os
import unittest
from port_manager import port_manager

class TestPortManager(unittest.TestCase):
    def setUp(self):
        self.dummy_port_plan = [
            "NGINX:80",
            "Android Emulator:5554",
            "Genymotion Emulator:6080",
        ]
        self.expected_port_map = {
            "NGINX": 80,
            "Android Emulator": 5554,
            "Genymotion Emulator": 6080,
        }

    def test_load_port_plan(self):
        with open("port_manager/port_plan.md", "w") as f:
            f.write("\n".join(self.dummy_port_plan))
        port_plan = port_manager.load_port_plan()
        self.assertEqual(port_plan, self.dummy_port_plan)

    def test_assign_ports(self):
        with open("port_manager/port_plan.md", "w") as f:
            f.write("\n".join(self.dummy_port_plan))
        port_manager.assign_ports()
        port_map = port_manager.load_port_map()
        self.assertEqual(port_map, self.expected_port_map)

    def tearDown(self):
        # Clean up test files
        if os.path.exists("port_manager/port_plan.md"):
            os.remove("port_manager/port_plan.md")
        if os.path.exists("port_manager/port_map.json"):
            os.remove("port_manager/port_map.json")

if __name__ == "__main__":
    unittest.main()
