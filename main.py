from Serie_4.math_utils import divisors

divisors_dict = divisors(1, 500)

for num in divisors_dict:
  print("Número: ", num, " - ", divisors_dict[num][0], " - ", divisors_dict[num][1])