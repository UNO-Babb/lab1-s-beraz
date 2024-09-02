# FirstProgram.py
#Name: Skye Beraz
#Date: 8/30/2024
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello there!")
  #Ask for the user's name
  name = input("What is your name? My name is: ")
  #Use the user's name in the program.
  print("It's nice to meet you", name,"!")
  #Ask the user for their age.
  age = int(input("How old are you? I am: "))
  #Tell the user what year they were born in.
  print(name, ", if you have not had your birthday yet this year, you would have been born in the year", 2023-age)
  #Assume that they have not had their birthday yet this year.

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
