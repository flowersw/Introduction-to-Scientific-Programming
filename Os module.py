#!/usr/bin/env python


#Os module

import os
os.mkdir('music')
for i range (1,11):
    open('music/%s+%d.mp3' % ('bach', i), 'w')
    
    
for filename in os.listdir('music'):
    os.rename(filename, 'music/%s_%d.mp3' % ('yinqian', filename.split('.')))
    
    print .listdir('music')