def find_lower_limit_for_searching(piles, time):
    '''
    Helps with optimising search area; The logic is following - monkey cannot consume
    all the bananas in given time with speed that is less then average speed, therefore
    lower limit of binary search should be set to average speed

    :param piles: a list consisting of piles wehe the value of pile is its banana capacity
    :param time: time to consume all the bananas
    :return: average speed of banana consumption which can also be refered to as smallest pille
    in the contecst of searching

    >>> find_lower_limit_for_searching([3, 5, 7, 8 , 1, 10, 44, 2, 9], 6)
    14
    '''

    all_bananas = 0
    for pile in piles:
        all_bananas += pile
    smallest_pile = all_bananas // time
    return smallest_pile


def min_eating_speed(piles, time):
    '''
    Implements binary search to determines minimal speed of consumption that satisfies
    task condition

    :param piles: a list consisting of piles wehe the value of pile is its banana capacity
    :param time: time to consume all the bananas (predefined in the task)
    :return: minimal speed

    >>> min_eating_speed([3, 6, 7, 11], 8)
    4
    >>> min_eating_speed([30, 11, 23, 4, 20], 5)
    30
    >>> min_eating_speed([30, 11, 23, 4, 20], 6)
    23
    '''

    biggest_pile = max(piles)
    smallest_pile = find_lower_limit_for_searching(piles, time)
    while smallest_pile < biggest_pile:
        speed = (smallest_pile + biggest_pile) // 2
        if does_speed_satisfy_time_boundary(piles, time, speed):
            biggest_pile = speed
        else:
            smallest_pile = speed + 1
    return int(smallest_pile)


def does_speed_satisfy_time_boundary(piles, max_time, speed):
    '''

    Checks whether or not the consumption time with given speed is bigger
    than time predefined in the task

    :param piles: a list consisting of piles wehe the value of pile is its banana capacity
    :param max_time: time to consume all the bananas (predefined in the task)
    :param speed: consumption speed tht needs checkig
    :return: true if consumption time is less of equal to predefined time
             false if consumption time is bigger than predefined time

    >>> does_speed_satisfy_time_boundary([30, 11, 23, 4, 20], 6, 4)
    False
    >>> does_speed_satisfy_time_boundary([30, 11, 23, 4, 20], 6, 30)
    True
    >>> does_speed_satisfy_time_boundary([30, 11, 23, 4, 20], 6, 23)
    True
    '''

    eating_time = 0
    for pile in piles:
        eating_time += pile // speed + (0 if pile % speed == 0 else 1)
    return eating_time <= max_time


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)