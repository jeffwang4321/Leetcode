class Solution:
  def clockHands(self, hour: int, minutes: int) -> float:
    DegreesPerHour = 30
    DegreesPerMinute = 6
    MinutesPerHour = 60
    DegreesInHalfCircle = 180
    DegreesInCircle = 360

    # hourHandAngle = hour * DegreesPerHour

    # Part 2: If the minute hand is at 30, the hour hand would be halfway to the next number
    hourHandAngle = (hour * DegreesPerHour) + (minutes / MinutesPerHour * DegreesPerHour)
    minuteHandAngle = minutes * DegreesPerMinute

    angleBetweenClockHands = abs(hourHandAngle - minuteHandAngle)
    isAngleLessThanAHalfCircle = angleBetweenClockHands < DegreesInHalfCircle
    
    return angleBetweenClockHands if isAngleLessThanAHalfCircle else DegreesInCircle - angleBetweenClockHands



# python .\clockHands.py
if __name__ == "__main__":
  s1 = Solution()
  print(s1.clockHands(12, 30))
  print(s1.clockHands(3, 30))
  print(s1.clockHands(12, 00))

