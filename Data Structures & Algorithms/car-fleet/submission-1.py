class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []
        
        for car in cars:
            fleet = (target - car[0])/car[1]
            if not stack or fleet > stack[-1]:
                stack.append(fleet)

        return len(stack)