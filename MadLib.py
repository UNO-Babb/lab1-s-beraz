#MadLib.py
#Name: Skye Beraz
#Date: 9/1/2024
#Assignment: Lab 1

def main():
	print("Madlib")
	NAME1 = input("Give me a name. ")
	NAME2 = input("Give me another name, make sure it's different than the first! ")
	ADJ1 = input("Give me an adjective. HINT: An adjective is a descriptive word, like SMELLY or PINK. ")
	ADJ2 = input("Give me another adjective. ")
	NOUN1 = input("Give me a noun. HINT: A noun is a person, place, or a thing, like BOTTLE or SCHOOL. ")
	VERBED1 = input("Give me a verb ending in -ed. HINT: A verb is an action, like JUMP or SWIM. ")
	BODY1 = input("Give me a part of the body. ")
	ADJ3 = input("Give me another adjective. ")
	JOBTITLE1 = input("Give me a job title, like CASHIER or EXECUTIVE ASSISTANT. ")
	VERB1 = input("Give me a verb that does not end in -ed or -ing. ")
	VERB2 = input("Give me another verb that does not end in -ed or -ing. ")
	LOCATION1 = input("Give me a location. ")
	TIME1 = input("Give me a time of day. ")
	NUMBER1 = input("Give me a number, any number you want. ")
	ADJ4 = input("Give me another adjective. ")
	ANIMAL1 = input("Give me an animal. ")
	LOCATION2 = input("Give me a different location. ")
	VERBED2 = input("Give me another verb ending in -ed. ")
	LOCATION3 = input("Give me a different location. ")
	NUMBER2 = input("Give me another number, but make it proper. IE: 2nd, 1st, 58th, 69th, etc. ")
	BODY2 = input("Give me another part of the body. ")
	print("Okay, that's all I need! Finally I can tell the story of two best friends,", NAME1, "and", NAME2 + ".")

#Written story
	print("Did you hear what", NAME1, "said to", NAME2 + "?") 
	print("I heard", NAME1, "called", NAME2, "a", ADJ1, ADJ2, NOUN1 + "!")
	print("So", NAME2, VERBED1, NAME1, "right across the", BODY1 + ". It was", ADJ3 + ".")
	print("I just can't believe the", JOBTITLE1, "didn't", VERB1, "over and", VERB2 + ". Like, isn't that what", JOBTITLE1 + "'s are for?")
	print("Can you believe that all of this happened at", LOCATION1, "just before", TIME1 + "?")
	print("I think", NAME1, "and", NAME2, "have fought over", NUMBER1, "times just this year.")
	print("Last year,", NAME1, "brought their", ADJ4, ANIMAL1, "with her to", LOCATION2, "and set it loose on", NAME2 + ".")
	print("It", VERBED2, "them!")
	print("I heard it sent", NAME2, "to the", LOCATION3, "with", NUMBER2 + "-degree burns all over her", BODY2 + "!")
	print("... I just can't believe they're both still best friends. Like, who does that to a person?")

if __name__ == '__main__':
	main()