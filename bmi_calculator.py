#BMI Calculator.
def BMI_Calculator():
    
    weight=float(input("\nEnter your weight(kg):"))
    height=float(input("Enter your height(m):"))
    
    if(weight<0 and height<0):
        print("Invalid Input!!! Weight and Height should be positive numbers!")
        
    else:
        bmi=weight/(height**2)
        print("\nBMI=",bmi,"kg/m2")
        
        if(bmi<18.5):
            print("Underweight!")
            underweight()
        elif(18.5<=bmi<=24.9):
            print("Normal.")
            normal()
        elif(25<=bmi<=30):
            print("Overweight!")
            overweight()
        else:
            print("Obese!!!")
            obese()

#Information on the program, BMI and its catogries.
def info():
    print("\nAbout Program.")
    print("\n1.Input height and weight should be more than 0.\n2.Input height in meters(m) and weight in kilograms(kg).\n3.This Program calculates BMI according to the given height and weight and catogrizes them into BMI catogries.")
    print("\nBMI")
    bmi()
    print("\nUNDERWEIGHT (BMI <18.5)")
    underweight()
    print("\nNORMAL (BMI 18.5-24.9)")
    normal()
    print("\nOVERWEIGHT (BMI 25-30)")
    overweight()
    print("\nOBESE (BMI 30+)")
    obese()

#About BMI.
def bmi():
    print('''1. What is BMI?
Body Mass Index (BMI) is a numerical measurement that helps classify a person’s body weight relative to their height. It is widely used by healthcare professionals to estimate whether an individual is underweight, normal weight, overweight, or obese. BMI is a simple and quick assessment tool, though it has some limitations.

2. How is BMI Calculated?
BMI is calculated using the following formula:

𝐵𝑀𝐼= Weight(kg)/Height(m)2''')
   
#About Underweight Catogory. 
def underweight():
    print('''\n📉 Meaning: A person in this range has a lower body weight than what is considered healthy.

⚠️ Health Risks:
-Malnutrition and vitamin deficiencies
-Weakened immune system
-Increased risk of osteoporosis (weak bones)
-Muscle loss and weakness
-Fertility issues in women

✅ Possible Causes:
-Poor nutrition
-High metabolism
-Underlying health conditions (e.g., hyperthyroidism, eating disorders)

Solution: A balanced diet with sufficient calories, strength training, and medical advice if necessary.''')

#About Normal Catogory.
def normal():
    print('''\n📊 Meaning: This is considered the healthy weight range for most individuals.

✅ Health Benefits:
-Lower risk of heart disease, diabetes, and high blood pressure
-Good metabolism and body function
-Optimal energy levels

Maintaining this range involves regular physical activity, a nutritious diet, and a balanced lifestyle.''')

#About Overweight Catogory.
def overweight():
    print('''\n📈 Meaning: A person in this range has more body weight than considered ideal for their height.

⚠️ Health Risks:
-Higher risk of heart disease and high blood pressure
-Increased chances of developing type 2 diabetes
-Joint and mobility issues
-Sleep apnea

✅ Possible Causes:
-Poor diet and high-calorie intake
-Lack of physical activity
-Genetics and metabolism
-Stress and hormonal imbalances

Solution: Regular exercise, balanced diet, portion control, and stress management.''')

#About Obese Catogory.
def obese():
    print('''\n🏥 Meaning: A person with obesity has excessive body fat, which can lead to serious health problems.

⚠️ Health Risks:
-Obese Class I (BMI 30 – 34.9): Moderate risk of heart disease, diabetes, and high cholesterol.
-Obese Class II (BMI 35 – 39.9): High risk of severe health conditions like stroke, liver disease, and kidney problems.
-Obese Class III (BMI 40+): Also known as morbid obesity, with an extremely high risk of life-threatening diseases.

✅ Possible Causes:
-Poor diet, high sugar and fat intake
-Genetic predisposition
-Hormonal imbalances (e.g., thyroid issues, PCOS)
-Lack of physical activity

Solution: A structured weight loss plan, medical supervision, lifestyle changes, and in extreme cases, medical interventions like bariatric surgery.''')

def work():
    print('''\nTASKS:
1.Calculate BMI.
2.Information about program and BMI.
3.Exit the program.''')

work()
while True:
    task=int(input("\nEnter your task choice:"))
    if(task==1):
        BMI_Calculator()
        print("\nEnter 4 to check the task list again.")
    elif(task==2):
        info()
        work()
    elif(task==3):
        print("\nThanks for visiting...")
        break
    elif(task==4):
        work()
    else:
        print("Invalid Input!!! Enter the task number given above.")