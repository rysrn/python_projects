import random

word_bank = [
    ("stitious", "I'm not superstitious, but I am a little ____."),
    ("bankruptcy", "I didn't say it, I declared it. I declare ____!"),
    ("Scranton", "Dunder Mifflin is a regional paper company based out of ____, Pennsylvania."),
    ("pretzel", "The only day of the year Michael actually enjoys working is ____ Day."),
    ("galactica", "Bears. Beets. Battlestar ____."),
    ("dementors", "According to Prison Mike, the worst thing about prison was the ____."),
    ("chili", "Kevin spent all night prepping his famous secret ____ recipe, only to drop it on the floor."),
    ("toby", "If I had a gun with two bullets and I was in a room with Hitler, Bin Laden, and ____, I would shoot him twice."),
    ("stapler", "Jim started a historic prank war by encasing Dwight's ____ inside a yellow Jello mold."),
    ("beet", "Dwight operates a successful side hustle running a 60-acre ____ farm."),
    ("crossroads", "Threat Level Midnight is an action film masterpiece written and directed by Michael ____."),
    ("parkour", "Andy, Michael, and Dwight kept jumping off desks while screaming ____!"),
    ("chilis", "Pam got banned for life after having a little too much fun at the ____ afterparty."),
    ("jan", "Michael's toxic ex-girlfriend ____ completely destroyed his tiny plasma TV with a Dundee."),
    ("cornell", "Andy Bernard will never let anyone forget that he graduated from ____ University."),
    ("creed", "Nobody steals from ____ Bratton and gets away with it. The last person to do that disappeared."),
    ("bacon", "Michael accidentally grilled his own foot on a George Foreman grill because he wanted to wake up to the smell of ____.")
]

print()
print("~" * 50)
print()
print("    Welcome to Jargon Jumble!")
print("    The Office Themed Word Scramble Game")
print()
print("~" * 50)

ROUNDS =  8
round_num = 1
score = 0
used = []

while round_num <= ROUNDS:
  
  word,hint = random.choice(word_bank)

  while (word, hint) in used:
    word, hint = random.choice(word_bank)
    
    used.append((word, hint))
    
  letters = list(word)
  random.shuffle(letters)
  scrambled_word = "".join(letters).upper()
  
  print()
  print(f"Round {round_num}")
  print()
  print(f"Scrambled: {scrambled_word}")

  guess = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()


  if guess == "hint":
    print()
    print(f"Hint: {hint}")
    print()
    guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()

  if guess == "quit":
    print("Thanks for playing!")
    break
  elif guess == "skip":
    print(f"Skipped! The word was '{word}'.")
  elif guess == word:
    score +=1
    print("✅  Correct!")
  else:
    print(f"❌ Sorry, the word was '{word}'.")
    
  round_num += 1
  
print()
print(f"Final score: {score}/{ROUNDS}")
print()


if score == ROUNDS:  
    print("Regional Manager status unlocked! You are officially the World's Best Boss!")
elif score == ROUNDS - 1:  
    print("Assistant TO the Regional Manager! Dwight would be incredibly proud of your work.")
elif score == ROUNDS - 2:  
    print("Pretty good! Pam gives this round an 8 out of 10. Perfect for the office newsletter.")
elif score == ROUNDS - 3:  
    print("Not bad! You're playing at Scrantonicity levels—a bit messy, but the crowd loves it.")
elif score == ROUNDS - 4:  
    print("It works, but Angela is judging you hard right now. Watch out for corporate audits.")
else:  
    print("'Hi, I'm Date Mike. Nice to meet me.' ...Yeah, let's just pretend this round never happened.")

 
print()
print("Hope to see you again soon!!")
print()
