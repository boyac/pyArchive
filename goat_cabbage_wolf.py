# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-29 13:31:48
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-29 17:32:23

import itertools

def broccoli():
    """
    A farmer is to ferry across a river a goat, a cabbage, and a wolf.
    Besides the farmer himself, the boat allows him to carry only
    one of them at a time. Without supervision, the goat will gobble
    the cabbage whereas the wolf will not hesitate to feast on the goat.
    """

    total = ['g','c','w'] # all items to be carried over
    goat_cabbage = ['g','c'] # not allow sequence
    goat_wolf = ['g','w'] # not allow sequence


    # STEP 1  get respective permutations of total, goat_cabbage, goat_wolf
    # STEP 2 iterate over permutations of total(per_to) and goat_cabbage(goat_c), 
                # return the difference (差集), then append to item of goat_c
    # STEP 3 iterate over permutations of total(per_to) and goat_wolf(goat_w), 
                # return the difference (差集), then append to item of goat_w
    # STEP 4 iterate over permutations per_to and goat_c, 
                # return the difference (差集) 
    # STEP 5 iterate over permutations per_to and goat_w
                # return the difference (差集)
    # STEP 6 final result, of combined result of STEP 4 & STEP 5
