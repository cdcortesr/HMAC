#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Christian_SpaceConcordia.
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


import numpy
from gnuradio import gr
import pmt
from cryptography.hazmat.primitives import hashes, hmac
import struct

class HMAC_append(gr.basic_block):
    """
    docstring for block HMAC_append
    """
    def __init__(self, key,hash_funct):
        gr.basic_block.__init__(self,
            name="HMAC_append",
            in_sig=[],
            out_sig=[])
        
        self.key=b'<key>'
        self.hash_funct=hash_funct    
            
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.message_port_register_out(pmt.intern('out'))
        
        
    def handle_msg(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        packet = bytes(pmt.u8vector_elements(msg))
        key = b'test key'
        a=hashes.SHA256()
        h=HMAC(packet,key)
        h.update(packet)
        signature = h.finalize()
        packet += struct.pack('>I', signature)
        self.message_port_pub(
            pmt.intern('out'),
            pmt.cons(pmt.PMT_NIL, pmt.init_u8vector(len(packet), packet)))
            
