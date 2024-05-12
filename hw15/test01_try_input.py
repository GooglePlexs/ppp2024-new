def numbers_list():

  numbers = []

  count = 0
  total = 0

  while True:
    try:
      x = int(input("X= "))
    except ValueError:
      continue

    if x == -1:
      break

    if x >= 0:
      numbers.append(x)
      count += 1
      total += x

  return numbers, count, total


def main():

  numbers, count, total = numbers_list()

  print(f"입력된 값은 {numbers} 입니다. 총 {count}개의 정수가 입력되었고, 평균은 {total / count:.1f}입니다.")


if __name__ == "__main__":
  main()