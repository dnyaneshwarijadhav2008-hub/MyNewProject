# write a function to count vowels in the username 
def vowel_count():
    username = input("Enter your username: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in username if char in vowels)
    print("Number of vowels in username:", count)

vowel_count()
