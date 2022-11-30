
import rclpy
import rclpy.node
import bh_msgs.srv
import rclpy.client
import bh_msgs.action
import rclpy.action
import time
import rclpy.executors
from collections import defaultdict

def main():
    rclpy.init()

    node = rclpy.node.Node("robot_node")
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(node)
    
    client: rclpy.client.Client = node.create_client(
        bh_msgs.srv.SampleMap, "/sample_map")
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info("Service not available, waiting...")

    def execute_callback(goal_handle: rclpy.action.server.ServerGoalHandle):
        row, col = 0, 0
        step = 0
        visited = defaultdict(lambda: False)
        while rclpy.ok():
            if visited[(row, col)]:
                goal_handle.abort()
                return bh_msgs.action.Simulate.Result(result="Loop!", length=step)
            visited[(row, col)] = True
            future = client.call_async(bh_msgs.srv.SampleMap.Request(row=row, col=col))
            executor.spin_until_future_complete(future)
            value = future.result().value
            if value == "B":
                goal_handle.succeed()
                return bh_msgs.action.Simulate.Result(result="Battery!", length=step)
            elif value == "E":
                goal_handle.abort()
                return bh_msgs.action.Simulate.Result(result="Dead!", length=step)
            elif value == "outside":
                goal_handle.abort()
                return bh_msgs.action.Simulate.Result(result="Outside!", length=step)
            elif value == ">":
                col += 1
            elif value == "<":
                col -= 1
            elif value == "^":
                row -= 1
            elif value == "v":
                row += 1
            goal_handle.publish_feedback(bh_msgs.action.Simulate.Feedback(
                value=value, step=step))
            step += 1
            time.sleep(0.1)

    rclpy.action.ActionServer(node, bh_msgs.action.Simulate, '/simulate',
                              execute_callback)

    executor.spin()

if __name__ == '__main__':
    main()
