#!/usr/bin/env python
# 
# Copyright 2012 Communications Engineering Lab (CEL) / Karlsruhe Institute of Technology (KIT)
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
#

from gnuradio import gr, gr_unittest
import lte
#import lte_swig
import scipy.io
import os
from pylab import *


class qa_hier_sss_sync_cc (gr_unittest.TestCase):

    def setUp (self):
        print "begin test!"
        self.tb = gr.top_block ()
        
        offset = 43223
        fftl = 512
        cpl = 144 *fftl /2048
        cpl0 = 160 *fftl /2048
        slotl = 7*fftl+6+cpl+cpl0
        cell_id = 124
        N_rb_dl = 6

        intu = [1.0] *100*fftl
        self.src  = gr.vector_source_c(intu,False,1)
        self.tag  = lte.tag_symbol_cc(offset,fftl)
        self.sss = lte.hier_sss_sync_cc(fftl)
        self.snk = gr.vector_sink_c(1)
        
        self.tb.connect(self.src,self.tag,self.sss,self.snk)

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
    
        print "test run!"
        # set up fg
        self.tb.run ()
        # check data
        print "get test data"
        res = self.snk.data()
        
        '''
        corr_vec = self.sss.calc.get_corr_vec()
        plot(corr_vec)
        show()
        
        print "get_cell_id"
        print "cell_id = " + str(self.sss.get_cell_id())
        print "test finished"
        '''

if __name__ == '__main__':
    gr_unittest.main ()
            
