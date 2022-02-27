# <----- READ ME ----->
# Oh no! Our program has been attacked by a ransomware. We were given an anonymous tip about the potential suspects for the attack. Help us debug this program to find the suspect!

suspect_list = ["Amy", "Felicia", "Tony", "paul", "ivy", "Anthony", "jameson", "Anna"]

# LIST COMPREHENSION
# see how we can implement a for loop with conditions in one line? What do you think this function does?
example_suspect_list = [x for x in suspect_list if x[0].isupper()]


# <----- ACTION NEEDED HERE ----->
# this for loop implementation is producing errors, debug it so that the `official_suspect_list` looks like the `example_suspect_list`
official_suspect_list = []
for i in range(len(suspect_list)):
  if suspect_list[i][0].isupper():
    official_suspect_list.append(suspect_list[i])

# <----- ACTION NEEDED HERE ----->
# We were given a hint that the suspect who broke the code has a name of which is a palindrome (palindrome definition and example: https://examples.yourdictionary.com/palindrome-examples.html). Fix this while loop to find out the culprit
index = 0
culprit = None
while index < len(official_suspect_list):
  curr = official_suspect_list[index]
  ptr = 0
  while ptr < len(curr)//2:
    end = len(curr) - ptr - 1
    if curr[ptr] == curr[end]:
      continue
    else:
      break
    ptr += 1
  culprit = curr
  index += 1
