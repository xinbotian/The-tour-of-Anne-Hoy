"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Tour of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro, Ritu Chaturvedi, Samar Sabie
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
#


class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools
        to hold stools of cheese.

        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M._stools
        [[], [], [], []]
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        >>> M = TOAHModel(0)
        >>> M._stools
        []
        """
        self._move_seq = MoveSequence([])
        #self._stools = [[] for i in number_of_stools]
        self._stools = [[] for i in range(number_of_stools)]
        #self._stools_size = [[i.size for i in j] for j in self._stools]


    # here we build the necessary functions to run toah_model
    # step 1


    def fill_first_stool(self, number_of_cheeses):
        """
        fill the first stool w n_cheese in the corect order

        @param TOAHModel: self
        @param n_cheese:  int
        @rtype: None

        >>> M = TOAHModel(2)
        >>> M.fill_first_stool(5)
        >>> [[i.size for i in j] for j in M._stools]
        [[5, 4, 3, 2, 1], []]
        >>> M = TOAHModel(2)
        >>> M.fill_first_stool(0)
        >>> [[i.size for i in j] for j in M._stools]
        [[], []]
        >>> M = TOAHModel(0)
        >>> M.fill_first_stool(0)
        >>> M._stools
        []
        """
        if ((self.get_number_of_stools() == 0) and
                (number_of_cheeses > 0)):
            print('Need more stools, human')
        else:
            for i in range(number_of_cheeses):
                self._stools[0].append(Cheese(number_of_cheeses-i))


    def move(self, from_, to):
        """
        move the cheese from from_ to to if its smaller than the
        cheese on top of stool to

        @param TOAHModel: self
        @param from_:  int
        @patam to: int
        @rtype: None

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(3)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> [[i.size for i in j] for j in m1._stools]
        [[3], [], [2, 1], []]
        >>> m1._move_seq._moves
        [(0, 1), (0, 2), (1, 2)]
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(3)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> [[i.size for i in j] for j in m2._stools]
        [[3], [], [2, 1], []]

        #>>> m2.move(0,2)
        #>>> m2._move_seq.moves
        #[(0, 3), (0, 2), (3, 2), (0, 2)]
        """
        #if self._stools[to][0] >= self._stools[from_][-1]:
        #if self._stools[to][-1] >= self._stools[from_][-1]:
        #if 0 <= len(self._stools[to]) < len(self._stools[to]):
        self._move_seq.add_move(from_, to)
        if (0 > to) or (to >= self.get_number_of_stools()):
            raise IllegalMoveError('stool index out of range')
        elif len(self._stools[from_]) == 0:
            print('no cheese on this here stool')
        elif len(self._stools[to]) == 0:
            self._stools[to].append(self._stools[from_].pop())
        #elif self._stools[to][-1] >=  self._stools[from_][-1]:
        elif to == from_:
            return None
        elif self._stools[to][-1].size > self._stools[from_][-1].size:
            self._stools[to].append(self._stools[from_].pop())
        else: raise IllegalMoveError('cheese to big')


    def get_number_of_cheeses(self):
        """
        get the total number of cheeses on all stools

        @param TOAHModel: self
        @rtype: int

        >>> M = TOAHModel(2)
        >>> M.fill_first_stool(5)
        >>> M.get_number_of_cheeses()
        5
        >>> M = TOAHModel(2)
        >>> M.fill_first_stool(0)
        >>> M.get_number_of_cheeses()
        0
        """
        return sum([len(i) for i in self._stools])

    def get_number_of_stools(self):
        """
        get the total number of stools

        @param TOAHModel: self
        @rtype: int

        >>> M = TOAHModel(2)
        >>> M.fill_first_stool(5)
        >>> M.get_number_of_stools()
        5
        >>> M = TOAHModel(2)
        >>> M.fill_first_stool(0)
        >>> M.get_number_of_stools()
        0
        """
        return len(self._stools)

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        # n_stools = get_number_of_stools(self)
        n_stools = self.get_number_of_stools()
        if n_stools == other.get_number_of_stools():
            return all([self._stools[i] == other._stools[i] for i in
                        range(n_stools)])
        else:
            return False


















    # here we build the functions to work w the client code
    # step 2 and 3

    def get_cheese_location(self, cheese):
        """
        return the stool which the specified cheese i on

        @param TOAHModel: self
        @param cheese: Cheese
        @rtype: int

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.get_cheese_location(Cheese(1))
        1
        >>> m1.get_cheese_location(Cheese(4))
        0
        >>> m1.move(0, 2)
        >>> m1.get_cheese_location(Cheese(2))
        2
        >>> m1.get_cheese_location(Cheese(9))
        not a valid cheese, human
        """
        if 0 < cheese.size <= self.get_number_of_cheeses():
            j=0
            for i in self._stools:
                if cheese in i:
                    return j
                j+=1
        else:
            print('not a valid cheese, human')
            return None

    def get_top_cheese(self, stool_index):
        """
        return the cheese of class Cheers from the stool in self corresponding to
        stool_index

        @param TOAHModel: self
        @param stool_index: int
        @rtype: Cheese

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.get_top_cheese(0).size
        2
        >>> m1.get_top_cheese(1).size
        1
        >>> m1.move(0, 2)
        >>> m1.get_top_cheese(0).size
        3
        """

        if isinstance(stool_index, int):
            #if len(self._stools[stool_index]) == 0:
            #    print('no cheese here')
            if 0 <= stool_index < self.get_number_of_stools():
                if len(self._stools[stool_index]) == 0:
                    print('no cheese here')
                else: return self._stools[stool_index][-1]
            else:
                print('we dont have that stool dude')
        else:
            print('enter an int as the stool_index')


    def number_of_moves(self):
        """
        return the number of moves we've made in the game

        @param TOAHModel: self
        @rtype: int

        >>> m1 = TOAHModel(4)
        >>> m1.get_number_of_moves()
        0
        >>> m1.fill_first_stool(7)
        >>> m1.get_number_of_moves()
        0
        >>> m1.move(0, 1)
        >>> m1.get_number_of_moves()
        1
        """
        #return len(self._move_seq)
        return len(self._move_seq._moves)

    def add(self, cheese, stool_index):
        """
        add cheese onto stool if the size of cheese is < size of the top cheese on that
        stool

        @param TOAHModel: self
        @param cheese:  Cheese
        @patam stool_index: int
        @rtype: None

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(3)
        >>> m1.move(0, 1)
        >>> m1.add(Cheese(100), 3)
        >>> [[i.size for i in j] for j in m1._stools]
        [[3, 2], [1], [], [100]]
        >>> m1.add(Cheese(1), 0)
        >>> [[i.size for i in j] for j in m1._stools]
        [[3, 2, 1], [1], [], [100]]
        """
        print(stool_index)
        print(((stool_index < 0) or
                (stool_index >= self.get_number_of_stools())))
        if ((stool_index < 0) or
                (stool_index >= self.get_number_of_stools())):
            print('entered')
            raise IllegalMoveError('we dont have that stool')
        elif ((len(self._stools[stool_index]) == 0) and
                (cheese.size > 0)):
            self._stools[stool_index].append(cheese)
        elif 0 < cheese.size < self._stools[stool_index][-1].size:
            self._stools[stool_index].append(cheese)
        else:
            #return raise IllegalMoveError('that cheese is too darn big')
            raise IllegalMoveError('that cheese is too darn big, or <=0')




    # here is the oriniginal funcs from this mod
    def get_move_seq(self):
        """ Return the move sequence

        @type self: TOAHModel
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> toah.get_move_seq() == MoveSequence([])
        True
        """
        return self._move_seq


    def _cheese_at(self, stool_index, stool_height):
        """ Return (stool_height)th from stool_index stool, if possible.

        @type self: TOAHModel
        @type stool_index: int
        @type stool_height: int
        @rtype: Cheese | None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        if 0 <= stool_height < len(self._stools[stool_index]):
            return self._stools[stool_index][stool_height]
        else:
            return None

    def __str__(self):
        """
        Depicts only the current state of the stools and cheese.

        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self:
        @param int size:
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = int(size)

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool
        """
        return self.size == other.size


class IllegalMoveError(Exception):
    """ Exception indicating move that violate TOAHModel
    """
    pass


class MoveSequence(object):
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self:
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # Leave lines below to see what python_ta checks.
    # File toahmodel_pyta.txt must be in same folder.
    import python_ta
    python_ta.check_all(config="toahmodel_pyta.txt")
