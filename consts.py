#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing

# how many CPU cores does this machine have
TOTAL_CORES = multiprocessing.cpu_count()

# no single worker should use more than 30% of the available cores
CPU_CORES_MED = int(TOTAL_CORES * 0.3)   # 30%
CPU_CORES_HIGH = int(TOTAL_CORES * 0.5)  # 50%
CPU_CORES_MAX = int(TOTAL_CORES * 0.9)   # 90%

# default colours for print the graphs
COLOURS = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b15928', '#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f',
           '#cab2d6', '#ffff99']