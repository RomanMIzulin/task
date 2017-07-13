
# Написать программу, которая будет вычислять сумму 3 способами (while, for, рекурсия) следующего массива чисел – [3, 1, 5, 7, 9].

ar = [3,1,5,7,9];
print(ar[0]);
sum =0;
i = 0;
while i<5:
	sum+=ar[i]
	i=i+1

print(sum);

sum =0;
for x in range(5):
	sum+=ar[x]

print(sum);


def summury(ar,i =0,sum=0):
	sum+=ar[i];
	i = i+1;
	if i==5:
		return sum
	else:
		summury(ar,i,sum)

summury(ar);
print(sum);