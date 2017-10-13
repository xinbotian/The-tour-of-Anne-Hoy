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
def move_cheeses(model, n, source, intermediate, destination):
    """Move n cheeses from source to destination
    **stolen from Danny Heap's dope lecture**

    @param int n:
    @param int source:
    @param int intermediate:
    @param int destination:
    @rtype: None

    >>> mod = TOAHModel(3)
    >>> mod.fill_first_stool(3)
    >>> move_cheeses(mod, 3, 0, 1, 2)
    >>> mod._stools
    [[], [], [1, 2, 3]]
    """
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
    return count






def tour_of_four_stools_testing(model, n, m, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.
    we assume n > m

    @type n: number of cheese
    @type m: number of cheese intermediate stool
    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    count = 0
    # lets move n cheeses to a holding stool
    count += move_cheeses(model, m, 0, 1, 2)
    count += move_cheeses(model, n-m, 0, 1, 3)
    count += move_cheeses(model, m, 2, 0, 3)
    return count






if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    for c in range(4, 10):
        print('num_cheese', c)
        # for n in range(2,7):
        # for n in range(2, min([7,c])):
        for n in range(1, c - 1):
            print('num_cheese intermed', n)
            mod = TOAHModel(4)
            mod.fill_first_stool(c)
            print(tour_of_four_stools_testing(mod,
                                              c, n))

