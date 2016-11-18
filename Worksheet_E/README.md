(a)
~~~~
S2 = 0
S3 = S0
	
While S3 != 0:
	S2 += S1
	S3 -= 1
~~~~
(b)


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
