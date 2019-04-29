"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

"not understood properly"
"""

def avoidObstacles(inputArray):
	obstacles = sorted(inputArray)
	step_size = 2
	ending_length = max(obstacles)
	status =["Obstacle"]
	jumps = round(ending_length / step_size) + 1

	while "Obstacle" in status:
		status = []
		for i in range(1,jumps):
			if i * step_size in obstacles:
				step_size += 1
				jumps = round(ending_length / step_size) + 1
				status.append("Obstacle")
			else:
				status.append("Clear")
	return step_size