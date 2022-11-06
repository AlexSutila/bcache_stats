#!/bin/python3

from sys import argv

def dump_stats():
    
    if (len(argv) != 2):
        print('usage: ./dump_stats.py <n>')
        return

    stats = ['cache_hits',
            'cache_misses',
            'bypassed',
            'cache_bypass_hits',
            'cache_bypass_misses',
            'cache_miss_collisions']

    for stat in stats:
        with open('/sys/block/bcache{}/bcache/stats_total/{}'.format(argv[1], stat)) as file:
            print('{}:\t{}'.format(stat, file.readlines()[0]), end='')

if __name__ == "__main__":
    dump_stats()

