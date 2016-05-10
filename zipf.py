# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

import math
import glob
import sys

import matplotlib
import matplotlib.pyplot as plot

xs = [math.log(rank) for rank in range(1, 1000)]
# matplotlib.rc('font', family='Arial')
matplotlib.rc('legend', fontsize='small')
plot.xlabel('log(rank)')
plot.ylabel('log(frequency)')
plot.title("A crude investigation of Zipf's law for some Sanskrit texts")

def plot_frequency(work_name):
    (real_name, ascii_name) = work_name
    rank = 0
    ys = []
    filename = glob.glob('DCS-*-%s.frequency' % real_name)[0]
    for line in open(filename).readlines():
        rank += 1
        if rank > len(xs):
            break
        line = line.decode('utf-8')
        parts = line.split('\t')
        word = parts[0]
        frequency = int(parts[1])
        # print 'The %d-th most frequent word (%s) occurs %d times' % (rank, word, frequency)
        ys.append(math.log(frequency))
    plot.plot(xs, ys, ':', label=ascii_name)

# files = glob.glob('DCS-*.frequency')
# for f in reversed(files):
#     parts = f.split('-')
#     work = parts[-1].split('.')[0]
#     print work

for work_name in [('Mahābhārata', 'Mahabharata'),
                  ('Rāmāyaṇa', 'Ramayana'), # 'Liṅgapurāṇa', 'Aṣṭāṅgahṛdayasaṃhitā',
                  ('Bṛhatkathāślokasaṃgraha', 'Brihatkathashlokasangraha'),
                  # 'Kūrmapurāṇa',
                  ('Manusmṛti', 'Manusmriti'), # 'Chāndogyopaniṣad',
                  ('Kāmasūtra', 'Kamasutra'),
                  ('Daśakumāracarita', 'Dashakumaracharita'),
                  ('Kumārasaṃbhava', 'Kumarasambhava')]:
    plot_frequency(work_name)

plot.legend(loc='upper right')

plot.savefig('zipf-sanskrit.png')
