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
from cryptography.hazmat.primitives import hashes, hmac
import struct
import pmt

class HMAC_verify(gr.basic_block):
    """
    docstring for block HMAC_verify
    """
    def __init__(self,key,hash_funct):
        gr.basic_block.__init__(self,
            name="HMAC_verify",
            in_sig=[],
            out_sig=[])
            
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.message_port_register_out(pmt.intern('out'))
        
        self.key=b'<key>'
        self.hash_funct=hash_funct 
        
    def handle_msg(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        packet = bytes(pmt.u8vector_elements(msg))
        packet_message = struct.unpack('>I', bytes(packet[:-64]))[0]
        packet_signature = struct.unpack('>I', bytes(packet[-64:]))[0]
        key = b'test key'
        h = hmac.HMAC(key, hashes.SHA256())
        h.update(packet_message)
        h_copy = h.copy() # get a copy of `h' to be reused
        packet_signature=h_copy.finalize()
        if signature == packet_signature:
            if self.verbose:
                print('HMAC OK')
            self.message_port_pub(pmt.intern('ok'), pmt.cons(pmt.PMT_NIL, pmt.init_u8vector(len(packet_message), packet_message)))
        else:
            if self.verbose:
                print('HMAC failed')
            self.message_port_pub(pmt.intern('fail'), pmt.cons(pmt.PMT_NIL, pmt.init_u8vector(len(packet_message), packet_message)))
                
    #def forecast(self, noutput_items, ninput_items_required):
    #    #setup size of input_items[i] for work call
    #    for i in range(len(ninput_items_required)):
    #        ninput_items_required[i] = noutput_items

    #def general_work(self, input_items, output_items):
    #    output_items[0][:] = input_items[0]
    #    consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
    #    return len(output_items[0])
