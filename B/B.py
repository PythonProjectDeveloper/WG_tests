class MovingElement(object):

    def __init__(self, start_point, end_point, location, direction, time, path):
        self.__start_point = start_point
        self.__end_point = end_point
        self.__location = location
        self.__direction = direction
        self.__time = time
        self.__path = path
        self.__speed = path / time

    @property
    def start_point(self):
        return self.__start_point

    @property
    def end_point(self):
        return self.__end_point

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def time(self):
        return self.__time

    @property
    def path(self):
        return self.__path

    @property
    def speed(self):
        return self.__speed

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    def move(self):
        self.location += self.path * self.direction


class Shuttle(MovingElement):
    def turn(self):
        self.direction *= -1


class Employee(MovingElement):
    pass


class PathTimeCalculator:

    def __init__(self):

        # enter the data
        first_input = raw_input().split(' ')
        second_input = raw_input().split(' ')
        third_input = raw_input().split(' ')

        if len(first_input) != 3 or \
           len(second_input) != 2 or \
           len(third_input) != 2:
            raise ValueError

        # distribute the received data
        shtl_end_point, emp_start_point, emp_end_point = map(int, first_input)
        shtl_time, emp_time = map(float, second_input)
        shtl_location, shtl_direction = map(int, third_input)
        shtl_start_point = 0

        # check the received data
        if not (2 <= shtl_end_point <= 1000 and
                0 <= emp_start_point <= shtl_end_point and
                0 <= emp_end_point <= shtl_end_point and
                emp_start_point != emp_end_point):
            raise ValueError

        if not (1 <= shtl_time <= 1000 and 1 <= emp_time <= 1000):
            raise ValueError

        if not (1 <= shtl_location <= shtl_end_point - 1):
            raise ValueError

        if shtl_direction != -1 and shtl_direction != 1:
            raise ValueError

        # create the moving elements
        path = 1
        emp_direction = 1 if emp_start_point < emp_end_point else -1
        self.__shuttle = Shuttle(start_point=shtl_start_point,
                                 end_point=shtl_end_point,
                                 location=shtl_location,
                                 direction=shtl_direction,
                                 time=shtl_time,
                                 path=path)

        self.__employee = Employee(start_point=emp_start_point,
                                   end_point=emp_end_point,
                                   location=emp_start_point,
                                   direction=emp_direction,
                                   time=emp_time,
                                   path=path)

    @property
    def employee(self):
        return self.__employee

    @property
    def shuttle(self):
        return self.__shuttle

    def calculate_distance(self):
        """
        Return the distance between the shuttle and the employee

        Returns:
            int: the distance between the shuttle and the employee
        """

        distance = 0
        while True:
            if self.shuttle.direction > 0 and self.shuttle.location == self.shuttle.end_point or \
               self.shuttle.direction < 0 and self.shuttle.location == self.shuttle.start_point:
                self.shuttle.turn()

            if self.shuttle.location == self.employee.location and \
               self.shuttle.direction == self.employee.direction:
                return distance

            distance += 1
            self.shuttle.move()

    def calculate_path_time(self):
        """
        Return the time spent on the path.

        Returns:
            float: the minimum time for which the worker can reach the given point
        """

        # the full path that needs to be overcome
        emp_full_path = abs(self.employee.start_point - self.employee.end_point)

        # if the shuttle is slower than the employee then we go on foot
        if self.shuttle.time >= self.employee.time:
            return emp_full_path * self.employee.time

        # if the shuttle and the worker are at the same point,
        # and their direction is the same then we go on the shuttle.
        if self.employee.direction == self.shuttle.direction and \
           self.employee.location == self.shuttle.location:
            return emp_full_path * self.shuttle.time

        distance = self.calculate_distance()
        approach_speed = self.shuttle.speed - self.employee.speed
        # time through which the shuttle and employee cross
        convergence_time = distance / approach_speed
        # how long the employee passed before crossing with the shuttle
        emp_walked = convergence_time / self.employee.time

        # if by the time the employee and the shuttle intersect,
        # the employee will reach the destination then we walk
        if emp_walked >= emp_full_path:
            return emp_full_path * self.employee.time

        return (distance + emp_full_path) * self.shuttle.time


def main():
    try:
        ptc = PathTimeCalculator()
        time = ptc.calculate_path_time()

        print int(time)

    except ValueError:
        pass

    except Exception:
        pass


if __name__ == '__main__':
    main()
