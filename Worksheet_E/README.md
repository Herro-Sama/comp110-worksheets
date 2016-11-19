(a)
~~~~
S2 = 0
S3 = S0
	
While S3 != 0:
	S2 += S1
	S3 -= 1
~~~~
(b)
The value of S2 is being increased each loop by whatever S1 is, this means that it will be effectively multiplied by S1, S0 times.

(c)
~~~
def outer():
	S2 = 0
	S3 = S0

def inner():
	S2 += S1
	S3 -= 1
	if S3 != 0:
		inner()
	S1 = S2
	S0 -= 1
	if S0 != 0:
		outer()
		
S0 = 10
S1 = 1
outer()
inner()		
~~~
(d)


(e)
~~~
addi $s0, $zero, 10
addi $s1, $zero, 1
Loop: mul $s1, $s0, $s1
addi $s0, $s0, -1
bne $s0, 0, Loop
~~~
