"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
from toah_model import TOAHModel


# move_cheeses from lecture
# put params in tuples
def move_cheeses(model, n, source, intermediate,
             destination, delay_btw_moves=0.5, animate=False):
    """Move n cheeses from source to destination
    **stolen from Danny Heap's dope lecture**

    @param int n:
    @param int source:
    @param int intermediate:
    @param int destination:
    @rtype: int

    >>> mod = TOAHModel(3)
    >>> mod.fill_first_stool(3)
    >>> move_cheeses(mod, 3, 0, 1, 2)
    >>> [[i for i in j] for j in mod._stools]
    [[], [], [1, 2, 3]]
    """
    #print(animate)
    count = 0
    if n > 1:  # fill this in!
        #move_cheeses(model, n - 1, source, destination, intermediate)
        #move_cheeses(model, 1, source, intermediate, destination)
        #move_cheeses(model, n - 1, intermediate, source, destination)
        count += move_cheeses(model, n - 1, source, destination, intermediate)
        #print(model._stools)
        count += move_cheeses(model, 1, source, intermediate, destination)
        count += move_cheeses(model, n - 1, intermediate, source, destination)

    else:  # just 1 cheese --- leave this out for now!
        # this is the only change
        #print("{} -> {}".format(source, destination))
        model.move(source, destination)
        count += 1
        if animate == True:
            time.sleep(delay_btw_moves)
            print(model)
    return count



def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    if model.get_number_of_stools() < 4:
        print('need a 4th stool human')
    elif model.get_number_of_cheeses() == 0:
        print('need some more cheddar')
    elif model.get_number_of_cheeses() == 1:
        model.move(0, 3)
    else:
        n = len(model._stools[0]) # assume cheese is on the first srool
        # m = max(1, int(n/2))
        m = n - round((2*n+1)**0.5)+1
        count = 0
        # lets move n cheeses to a holding stool
        a = move_cheeses(model, m, 0, 1, 2, animate)
        print("move first " + str(m) + " took " + str(a))
        count += a
        a = move_cheeses(model, n - m, 0, 1, 3, animate)
        print("move interme " + str(n- m) + " took " + str(a))
        count += a
        a = move_cheeses(model, m, 2, 0, 3, animate)
        print("move final " + str(m) + " took " + str(a))
        count += a
        #count += move_cheeses(model, n-m, 0, 1, 2, animate)
        #count += move_cheeses(model, m, 0, 1, 3, animate)
        #count += move_cheeses(model, n-m, 2, 0, 3, animate)
        return count




if __name__ == '__main__':
    #mod = TOAHModel(4)
    #mod.fill_first_stool(5)
    #print(tour_of_four_stools(mod,animate=True))
    #move_cheeses(mod, 8, 0, 1, 2)


    num_cheeses = 100
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        console_animate,
                        delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta

    python_ta.check_all(config="tour_pyta.txt")
