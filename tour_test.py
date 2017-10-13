"""CSC148 Assignment 1: Tour of Anne Hoy Unit Tests

=== CSC148 Winter 2017 ===
Diane Horton, David Liu, Danny Heap
Department of Computer Science,
University of Toronto

Note: this file is for support purposes only.
"""

# Copyright 2013, 2014, 2017, Gary Baumgartner, Dustin Wehr,
# Danny Heap, Bogdan Simion, Jacqueline Smith, Dan Zingaro
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


import unittest
from hypothesis import given
from hypothesis.strategies import integers, text

import time
from toah_model import TOAHModel
import tour


class TestTOAH(unittest.TestCase):
    """Unit tests for Assignment 1."""

    def setUp(self):
        self.toah = TOAHModel(4)
        self.optimals = [0, 1, 3, 5, 9, 13, 17, 25, 33, 41, 49, 65, 81, 97, 113, 129, 161, 193, 225, 257, 289,
                         321, 385, 449, 513, 577, 641, 705, 769, 897, 1025, 1153, 1281, 1409, 1537, 1665, 1793,
                         2049, 2305, 2561, 2817, 3073, 3329, 3585, 3841, 4097, 4609, 5121, 5633]

    def test_all_cheeses(self):
        for i in range(0, len(self.optimals)):
            self.toah = TOAHModel(4)
            self.toah.fill_first_stool(i)
            tour.tour_of_four_stools(self.toah)
            self.assertEqual(self.toah.number_of_moves(), self.optimals[i])

    def test_0_cheeses(self):
        self.toah.fill_first_stool(0)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[0])

    def test_1_cheeses(self):
        self.toah.fill_first_stool(1)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[1])

    def test_2_cheeses(self):
        self.toah.fill_first_stool(2)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[2])

    def test_3_cheeses(self):
        self.toah.fill_first_stool(3)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[3])

    def test_4_cheeses(self):
        self.toah.fill_first_stool(4)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[4])

    def test_5_cheeses(self):
        self.toah.fill_first_stool(5)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[5])

    def test_6_cheeses(self):
        self.toah.fill_first_stool(6)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[6])

    def test_7_cheeses(self):
        self.toah.fill_first_stool(7)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[7])

    def test_8_cheeses(self):
        self.toah.fill_first_stool(8)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[8])

    def test_9_cheeses(self):
        self.toah.fill_first_stool(9)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[9])

    def test_10_cheeses(self):
        self.toah.fill_first_stool(10)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[10])

    def test_11_cheeses(self):
        self.toah.fill_first_stool(11)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[11])

    def test_12_cheeses(self):
        self.toah.fill_first_stool(12)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[12])

    def test_13_cheeses(self):
        self.toah.fill_first_stool(13)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[13])

    def test_14_cheeses(self):
        self.toah.fill_first_stool(14)
        tour.tour_of_four_stools(self.toah)
        self.assertEqual(self.toah.number_of_moves(), self.optimals[14])

if __name__ == '__main__':
    unittest.main()
