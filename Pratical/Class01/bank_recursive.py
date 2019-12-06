#!/usr/bin/env python3

import math

    def profit(cap):
        for i in range(1, 26):
            cap *= i
            cap -= 1

        print("{:.2e}".format(cap))
