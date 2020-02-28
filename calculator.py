import sys


def calculator(income):
    insurance=0.08+0.02+0.005+0.06
    shouldPay=income*(1-insurance)-5000
    if shouldPay <= 0:
        tax = 0
    elif 0<shouldPay<=3000:
        tax = shouldPay * 0.03
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <= 12000:
        tax = shouldPay * 0.1 - 210 
    elif 12000 < shouldPay <= 25000:
        tax = shouldPay * 0.2 - 1410
    elif 25000 < shouldPay <= 35000:
        tax = shouldPay * 0.25 - 1410
    elif 35000 < shouldPay <= 55000:
        tax = shouldPay * 0.3 - 4410 
    elif 55000 < shouldPay <= 80000:
        tax = shouldPay * 0.35 - 7160 
    else:
        tax = shouldPay * 0.45 -15160
    salary=income*(1-insurance) - tax
    return'{:.2f}'.format(salary)

def main():
    for item in sys.argv[1:]:
        id,income =item.split(':')
        try:
            income=int(income)
        except ValueError:
            print('请在薪资的位置输入数字')
            continue
        print('{}:{}'.format(id,calculator(income)))
if __name__ == '__main__':
    main()
